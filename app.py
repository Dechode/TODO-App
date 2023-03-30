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

if __name__ == '__main__':
    todo()


