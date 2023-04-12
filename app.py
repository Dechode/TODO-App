#!/usr/bin/python3

import os
import sys
import time
import jsonpickle

class TODODescription(object):
    def __init__(self, todoName, startTime = -1) -> None:
        self.todoName = todoName
        self.startTime = startTime
        self.stopTime = -1

    def display(self, id=''):
        print('%s %s' % (str(id), str(self.todoName)))


class TaskDescription(object):
    def __init__(self, name, path, startTime):
        self.taskPath = path 
        self.taskName: str = name
        self.startTime = startTime
        self.stopTime = -1
        self.status = ''
        self.todos: list = []

    def addTODO(self, todo: TODODescription):
        self.todos.append(todo)

    def removeTODO(self, id):
        self.todos.pop(int(id))

    def display(self):
        print('\n')
        print('Task name = %s' % str(self.taskName))
        print('Task start time = %s' % str(self.startTime))
        print('Task stop time = %s' % str(self.stopTime))
        print('Task status = %s' % str(self.status))
        print('\nTODO:s\n')
        todoID = 0
        for todo in self.todos:
            todo.display(todoID)
            todoID += 1

class App:
    taskList = [TaskDescription]
    jsonName = 'tasks.json'
    argCount = 0
    
    def __init__(self, workingDir):
        self.workingDir = workingDir
        self.jsonPath = self.workingDir + '/%s' % App.jsonName
        self.taskCount = 0

    def printTaskList(self):
        print('Total number of tasks: %d' % len(self.taskList))
        for task in self.taskList:
            task.display()

    def createTasksJSON(self):
        with open(App.jsonName, 'w') as f:
            tasks = jsonpickle.encode(self.taskList)
            f.write(str(tasks))
            f.close() 

    def addTODO(self, taskID, todo):
        if self.taskCount - 1 < taskID:
            print('ID is too big, cant add TODO')
            return
        self.taskList[taskID].addTODO(todo)

        print('Added a new TODO for task ID %d' % taskID)
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

        self.taskList[taskID].removeTODO(todoID)
        print('Removed TODO ID %d from task ID %d' % (int(todoID), int(taskID)))

    def addTask(self, taskName: str):
        task:TaskDescription = TaskDescription(taskName, os.getcwd(), time.time())
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
            taskID = self.addTask(taskname)
                
        elif action == 'remove':
            if len(self.taskList) < 1:
                print('No task to remove!')
                return
            self.removeTask(taskID)

        elif action == 'status':
            if taskID < 0:
                print('No task with that name!')
            else:
                self.taskList[taskID].display()

        elif action == 'add-todo':
            if taskID >= 0:
                description = args[3]
                todo = TODODescription(description)
                self.addTODO(taskID, todo)

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


