#!/usr/bin/python

import os
import sys
import time
import jsonpickle

class TaskDescription(object):
    def __init__(self, name, path, startTime):
        self.taskPath = path
        self.taskName = name
        self.startTime = startTime
        self.stopTime = -1
        self.status = ''
        self.todos = []

class App:
    taskList = [TaskDescription]
    jsonName = 'tasks.json'
    argCount = 0
    
    def __init__(self, workingDir):
        self.workingDir = workingDir
        self.jsonPath = self.workingDir + '/%s' % App.jsonName
        self.taskCount = 0

        if os.path.exists(self.workingDir + '/.git/'):
            if not os.path.exists(self.workingDir + '/.gitignore'):
                print('gitignore file not found, creating one.')
                with open('.gitignore', 'w') as f:
                    f.write(self.jsonName)
                    f.close()

    def printTODO(self, id):
        count = 0
        print('Task %d TODOS:' % id)
        for todo in self.taskList[id].todos:
            print('TODO %d. %s' % (count+1, todo))
            count += 1

    def printTask(self, id):
        print('\n')
        print('Task name = %s' % str(self.taskList[id].taskName))
        print('Task start time = %s' % str(self.taskList[id].startTime))
        print('Task stop time = %s' % str(self.taskList[id].stopTime))
        print('Task status = %s' % str(self.taskList[id].status))
        print('\n')
        self.printTODO(id)

    def printTaskList(self):
        print('Total number of tasks: %d' % len(self.taskList))
        for i in range(self.taskCount):
            self.printTask(i)

    def createTasksJSON(self):
        with open(App.jsonName, 'w') as f:
            tasks = jsonpickle.encode(self.taskList)
            f.write(str(tasks))
            f.close() 

    def addTODO(self, id, todo):
        if self.taskCount - 1 < id:
            print('ID is too big, cant add TODO')
            return
        self.taskList[id].todos.append(todo)
        print('Added a new TODO for task ID %d' % id)
        print(todo)

    def removeTODO(self, taskID, todoID):
        if self.taskCount - 1 < taskID:
            print('task ID is too big, cant add TODO')
            return
        if taskID < 0:
            print('task ID cant be below 0!')
            return
        if int(todoID) >= len(self.taskList[taskID].todos):
            print('Invalid todo id')
            return

        self.taskList[taskID].todos.pop(int(todoID))
        print('Removed TODO ID %d from task ID %d' % (int(todoID), int(taskID)))

    def addTask(self, task=None):
        if not task:
            task = TaskDescription(sys.argv[2], os.getcwd(), time.time())
        self.taskList.append(task)
        self.taskCount += 1
        print('Created Task ID = %d' % int(self.taskCount-1))
        return self.taskCount - 1

    def removeTask(self, taskID):
        if taskID >= 0 and taskID < self.taskCount:
            del self.taskList[taskID]
            self.taskCount -= 1
            print('TaskID %d removed!' % taskID)

    def getTaskCount(self):
        count = 0
        for _ in self.taskList:
            count += 1
        return count

    def loadTasks(self):
        # Check for existing tasks.json file
        if not os.path.exists(self.jsonPath):
            print("No tasks.json found! Creating a new one.")
            self.createTasksJSON()

        tasks = [] 
        with open(App.jsonName, 'r') as f:
            file = jsonpickle.decode(f.read())
            for task in file:
                if isinstance(task, TaskDescription):
                    tasks.append(task)

        self.taskList = tasks
        self.taskCount = self.getTaskCount()

    def saveTasks(self):
        if len(self.taskList) <= 0:
            print('Nothing to save, task list is empty')
            return

        with open(App.jsonName, 'w') as f:
            tasks = jsonpickle.encode(self.taskList)
            f.write(str(tasks))
            f.close()

    def getIdFromName(self, name):
        count = 0
        for task in self.taskList:
            count += 1
            if task.taskName == name:
                return count - 1
        return -1

    # Valid args are: create/remove/status/add-todo/remove-todo/list <taskname> (<description>)
    def parseCmdArgs(self, args):
        App.argCount = len(args)
        if App.argCount <= 1:
            print('ERROR: No args given! Usage: app.py <action> <taskname> (<description>) ')
            return
        
        action = args[1]

        # Only action without having to specify task name
        if action == 'list':
            self.printTaskList()
            return

        if App.argCount <= 2:
            print('Only 1 argument given and its not <list>')
            return

        taskname = args[2]
        taskID = self.getIdFromName(taskname) # Will return -1 if not found

        if action == 'create':
            if taskID >= 0:
                print('Task with that name already exists!')
                return
            taskID = self.addTask()
                
        elif action == 'remove':
            if len(self.taskList) < 1:
                print('No task to remove!')
                return
            self.removeTask(taskID)


        elif action == 'status':
            if taskID < 0:
                print('No task with that name!')
            else:
                self.printTask(taskID)

        elif action == 'add-todo':
            if taskID >= 0:
                description = args[3]
                self.addTODO(taskID, description)

        elif action == 'remove-todo':
            description = args[3]
            self.removeTODO(taskID, description)

        elif action == 'pause':
            print('TODO: Pause tasks todo for time tracking')

        elif action == 'continue':
            print('TODO: pause tasks todo for time tracking')

        else:
            print('Unknown action!')
            return


if __name__ == '__main__':
    app = App(os.getcwd())
    app.loadTasks()
    app.parseCmdArgs(sys.argv)
    app.saveTasks()


