from task_manager import TaskManager

def test_add_task():
    manager = TaskManager()
    manager.add_task("Test Task", "This is a test task.")
    
    tasks = manager.view_tasks()
    
    assert len(tasks) == 1
    assert tasks[0]['title'] == "Test Task"
    assert tasks[0]['description'] == "This is a test task."
    
def test_multiple_tasks():
    manager = TaskManager()
    manager.add_task("Task 1", "Description 1")
    manager.add_task("Task 2", "Description 2") 
    
    assert len(manager.view_tasks()) == 2
    
def test_view_tasks_empty():
    manager = TaskManager()
    assert manager.view_tasks() == []
    
