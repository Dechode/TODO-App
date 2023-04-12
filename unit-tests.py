#!/usr/bin/python3

import os
import unittest
import jsonpickle
import app as TODOApp
import time

class TestTODOApp(unittest.TestCase):

    def setUp(self):
        print('\nsetUp')

        self.app = TODOApp.App(os.getcwd())
        self.appFileName = './app.py'
        self.app.loadTasks()

        print('Loaded %d tasks' % len(self.app.taskList))

    def tearDown(self):
        print('tearDown')
        self.app.taskList.clear()


    def test_taskCount(self):
        self.assertEqual(self.app.taskCount, len(self.app.taskList))

    def test_addTask(self):
        taskCount1 = len(self.app.taskList)
        task = TODOApp.TaskDescription('TestingTask', os.getcwd(), time.time())
        self.app.addTask(task)
        taskCount2= len(self.app.taskList)
        self.assertLess(taskCount1, taskCount2)

    def test_addNRemoveTask(self):
        taskCount1 = len(self.app.taskList)
        task = TODOApp.TaskDescription('TestingTask', os.getcwd(), time.time())
        self.app.addTask(task)
        taskCount2= len(self.app.taskList)
        self.assertLess(taskCount1, taskCount2)

        self.app.removeTask(0)
        taskCount3 = len(self.app.taskList)
        self.assertGreater(taskCount2, taskCount3)

    def test_addTODO(self):
        if self.app.taskCount < 1:
            task = TODOApp.TaskDescription('TestingTask', os.getcwd(), time.time())
            self.app.addTask(task)

        todoCount1 = 0
        for task in self.app.taskList:
            todoCount1 += len(task.todos)

        self.app.addTODO(0, 'TestingTodo')

        todoCount2 = 0
        for task in self.app.taskList:
            todoCount2 += len(task.todos)
        
        self.assertLess(todoCount1, todoCount2)

    def test_addNRemoveTODO(self):
        if self.app.taskCount < 1:
            task = TODOApp.TaskDescription('TestingTask', os.getcwd(), time.time())
            self.app.addTask(task)

        todoCount1 = 0
        for task in self.app.taskList:
            todoCount1 += len(task.todos)

        self.app.addTODO(0, 'TestingTodo')

        todoCount2 = 0
        for task in self.app.taskList:
            todoCount2 += len(task.todos)
        
        self.assertLess(todoCount1, todoCount2)

        self.app.removeTODO(0,0)

        todoCount3 = 0
        for task in self.app.taskList:
            todoCount3 += len(task.todos)

        self.assertGreater(todoCount2, todoCount3)

if __name__ == '__main__':
    unittest.main()

