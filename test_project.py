from project import add_task, list_tasks, complete_task


def test_add_task():
    tasks = []
    tasks = add_task(tasks, "Test Task", "2025-09-01", "high")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
    assert tasks[0]["priority"] == "high"


def test_list_tasks_priority():
    tasks = []
    tasks = add_task(tasks, "Low priority", priority="low")
    tasks = add_task(tasks, "High priority", priority="high")
    sorted_tasks = list_tasks(tasks, "priority")
    assert sorted_tasks[0]["priority"] == "high"


def test_complete_task():
    tasks = []
    tasks = add_task(tasks, "Incomplete Task")
    tasks = complete_task(tasks, 1)
    assert tasks[0]["completed"] is True
