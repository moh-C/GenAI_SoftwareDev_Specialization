import unittest

tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return tasks

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        # Clear tasks before each test
        tasks.clear()
    
    def test_add_task_basic(self):
        result = add_task("Test task")
        self.assertEqual(result, "Task 'Test task' added.")
        self.assertEqual(len(tasks), 1)
        self.assertIn("Test task", tasks)

    def test_add_empty_task(self):
        result = add_task("")
        self.assertEqual(result, "Task '' added.")
        self.assertIn("", tasks)

    def test_add_none_task(self):
        with self.assertRaises(TypeError):
            add_task(None)

    def test_add_duplicate_task(self):
        add_task("Duplicate")
        add_task("Duplicate")
        self.assertEqual(tasks.count("Duplicate"), 2)

    def test_remove_existing_task(self):
        add_task("Test task")
        result = remove_task("Test task")
        self.assertEqual(result, "Task 'Test task' removed.")
        self.assertEqual(len(tasks), 0)

    def test_remove_nonexistent_task(self):
        result = remove_task("Nonexistent")
        self.assertEqual(result, "Task not found.")

    def test_remove_duplicate_task(self):
        add_task("Duplicate")
        add_task("Duplicate")
        remove_task("Duplicate")
        self.assertEqual(tasks.count("Duplicate"), 1)

    def test_list_tasks_empty(self):
        self.assertEqual(list_tasks(), [])

    def test_list_tasks_multiple(self):
        add_task("Task 1")
        add_task("Task 2")
        self.assertEqual(list_tasks(), ["Task 1", "Task 2"])

if __name__ == '__main__':
    unittest.main()
