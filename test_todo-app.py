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

    def test_addTODO(self):
        if self.app.taskCount < 1:
            task = TODOApp.TaskDescription('TestingTask', os.getcwd(), time.time())
            self.app.addTask(task)

        todoCount1 = 0
        for task in self.app.taskList:
            todoCount1 += len(task.todos)

        print('TODO count before adding = %d' % todoCount1)

        self.app.addTODO(0, 'TestingTodo')

        todoCount2 = 0
        for task in self.app.taskList:
            todoCount2 += len(task.todos)
        
        print('TODO count after adding = %d' % todoCount2)

        self.assertLess(todoCount1, todoCount2)



if __name__ == '__main__':
    unittest.main()

