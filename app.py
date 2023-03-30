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
    taskList = []
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

    def addTask(self, task=None):
        if not task:
            task = TaskDescription(sys.argv[2], os.getcwd(), time.time())
        self.taskList.append(task)
        self.taskCount += 1
        print('Created Task ID = %d' % int(self.taskCount-1))
        return self.taskCount - 1

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
            tasks = jsonpickle.decode(f.read())
            #if len(tasks) <= 0:
            #    print('Loaded Json is empty!')

        self.taskList = tasks
        self.taskCount = self.getTaskCount()

    def saveTasks(self):
        if len(self.taskList) <= 0:
            print('Nothing to save, task list is empty')
            #os.remove(self.jsonPath)
            return

        with open(App.jsonName, 'w') as f:
            tasks = jsonpickle.encode(self.taskList)
            f.write(str(tasks))
            f.close()
if __name__ == '__main__':
    todo()


