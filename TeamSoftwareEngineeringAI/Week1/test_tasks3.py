import pytest
from tasks3 import add_task, remove_task, list_tasks, clear_tasks, tasks

@pytest.fixture(autouse=True)
def clear_tasks_before_test():
    clear_tasks()

def test_add_task():
    assert add_task("Test task") == ["Test task"]
    assert add_task("Another task") == ["Test task", "Another task"]

def test_add_empty_task():
    with pytest.raises(ValueError, match="Task cannot be empty."):
        add_task("")

def test_remove_existing_task():
    add_task("Test task")
    assert remove_task("Test task") == []

def test_remove_nonexistent_task():
    assert remove_task("Nonexistent task") == "Task not found."

def test_list_empty_tasks():
    assert list_tasks() == []

def test_list_multiple_tasks():
    add_task("Task 1")
    add_task("Task 2")
    assert list_tasks() == ["Task 1", "Task 2"]

def test_clear_tasks():
    add_task("Task 1")
    add_task("Task 2")
    assert clear_tasks() == "Tasks cleared."
    assert list_tasks() == []

def test_task_persistence():
    add_task("Task 1")
    assert tasks == ["Task 1"]
