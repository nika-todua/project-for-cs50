import json
from datetime import datetime


def main():
    print("Welcome to Task Manager!")
    tasks = []
    while True:
        print("\nOptions: add, list, complete, save, load, quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "add":
            title = input("Task title: ").strip()
            due_date = input("Due date (YYYY-MM-DD, optional): ").strip()
            priority = input("Priority (low/medium/high): ").strip().lower()
            tasks = add_task(tasks, title, due_date, priority)

        elif choice == "list":
            sort_by = input("Sort by (priority/date/none): ").strip().lower()
            for t in list_tasks(tasks, sort_by):
                print(t)

        elif choice == "complete":
            task_id = int(input("Task ID to complete: ").strip())
            tasks = complete_task(tasks, task_id)

        elif choice == "save":
            filename = input("Filename: ").strip()
            save_tasks(tasks, filename)
            print(f"Tasks saved to {filename}")

        elif choice == "load":
            filename = input("Filename: ").strip()
            tasks = load_tasks(filename)
            print(f"Tasks loaded from {filename}")

        elif choice == "quit":
            break

        else:
            print("Invalid choice. Try again.")


def add_task(tasks, title, due_date=None, priority="medium"):
    """Add a new task to the task list."""
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "due_date": due_date if due_date else None,
        "completed": False,
    }
    tasks.append(task)
    return tasks


def list_tasks(tasks, sort_by="none"):
    """Return tasks, optionally sorted by priority or due date."""
    if sort_by == "priority":
        priority_order = {"high": 1, "medium": 2, "low": 3}
        return sorted(tasks, key=lambda x: priority_order.get(x["priority"], 4))
    elif sort_by == "date":
        return sorted(
            tasks,
            key=lambda x: datetime.strptime(x["due_date"], "%Y-%m-%d")
            if x["due_date"]
            else datetime.max,
        )
    return tasks


def complete_task(tasks, task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    return tasks


def save_tasks(tasks, filename):
    """Save tasks to a JSON file."""
    with open(filename, "w") as f:
        json.dump(tasks, f)


def load_tasks(filename):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    main()
