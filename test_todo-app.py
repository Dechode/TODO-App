import os
import unittest
import app as TODOApp

class TestApp(unittest.TestCase):

    def setUp(self):
        print('setUp')

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
        self.app.addTask('TestingTask')
        taskCount2= len(self.app.taskList)
        self.assertLess(taskCount1, taskCount2)

if __name__ == '__main__':
    unittest.main()

