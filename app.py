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
if __name__ == '__main__':
    todo()


