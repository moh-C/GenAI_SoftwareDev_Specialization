import unittest
from tasks2 import add_task, remove_task, list_tasks, tasks

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Clear tasks before each test
        tasks.clear()

    def test_add_task(self):
        # Test adding a single task
        result = add_task("Buy groceries")
        self.assertEqual(result, "Task 'Buy groceries' added.")
        self.assertEqual(len(tasks), 1)
        self.assertIn("Buy groceries", tasks)

    def test_add_multiple_tasks(self):
        # Test adding multiple tasks
        add_task("Buy groceries")
        add_task("Read a book")
        self.assertEqual(len(tasks), 2)
        self.assertIn("Buy groceries", tasks)
        self.assertIn("Read a book", tasks)

    def test_remove_existing_task(self):
        # Test removing an existing task
        add_task("Buy groceries")
        result = remove_task("Buy groceries")
        self.assertEqual(result, "Task 'Buy groceries' removed.")
        self.assertEqual(len(tasks), 0)

    def test_remove_nonexistent_task(self):
        # Test removing a task that doesn't exist
        result = remove_task("Nonexistent task")
        self.assertEqual(result, "Task not found.")

    def test_list_tasks(self):
        # Test listing tasks
        add_task("Task 1")
        add_task("Task 2")
        task_list = list_tasks()
        self.assertEqual(len(task_list), 2)
        self.assertEqual(task_list, ["Task 1", "Task 2"])

    def test_list_empty_tasks(self):
        # Test listing when no tasks exist
        self.assertEqual(list_tasks(), [])

    def test_add_empty_task(self):
        # Test adding an empty task
        result = add_task("")
        self.assertEqual(result, "Tasks must be non-empty.")
        result = add_task(None)
        self.assertEqual(result, "Tasks must be non-empty.")

if __name__ == '__main__':
    unittest.main(verbosity=1)
