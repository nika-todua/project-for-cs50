# cs 50 harvard final project
    #### Video Demo:  https://github.com/nika-todua/project-for-cs50
    #### Description:

## Overview
The Task Manager CLI is a simple yet powerful command-line application written in Python that allows users to keep track of their to-do items directly from the terminal. The program supports creating, listing, sorting, completing, saving, and loading tasks. Each task can have a title, priority level, and an optional due date. Tasks are stored in memory during runtime and can also be persisted to disk in a JSON file so they can be retrieved later.

The project was designed to be lightweight and portable, requiring no third-party dependencies beyond Python’s standard library. This ensures that it can run on any system with Python installed without additional setup. Although intentionally minimalist in scope, the project demonstrates many core programming concepts, including data structures, file handling, user interaction, testing, and program design.

---

## Features
- **Add Tasks:** Users can create tasks with a title, optional due date, and a priority level (`low`, `medium`, `high`).
- **List Tasks:** Tasks can be displayed in the order they were added, or sorted by priority or due date.
- **Complete Tasks:** Users can mark tasks as completed. Completed tasks are still visible for record-keeping.
- **Persistence:** Tasks can be saved to a file in JSON format and loaded again later.
- **Error Handling:** The program gracefully handles missing files when loading and allows flexibility in input.

---

## File Structure
The project contains three main files:

### `project.py`
This is the core of the program. It contains the `main` function, which provides the interactive menu for the user, along with several helper functions:
- **`main()`**: Runs the command-line interface loop, prompting the user for commands.
- **`add_task()`**: Adds a new task with a unique ID, title, priority, and optional due date.
- **`list_tasks()`**: Returns tasks, sorted if requested by priority or due date.
- **`complete_task()`**: Marks a task as completed by its ID.
- **`save_tasks()`**: Saves the current list of tasks to a JSON file.
- **`load_tasks()`**: Loads tasks from a JSON file if it exists.

The program is written in a modular way so that each function performs one responsibility clearly and cleanly. This made it easier to test and maintain.

### `test_project.py`
This file contains unit tests written using `pytest`. The tests validate the correctness of the main helper functions:
- `test_add_task()` ensures that tasks are added with correct attributes.
- `test_list_tasks_priority()` checks that sorting by priority works as expected.
- `test_complete_task()` verifies that tasks can be marked as complete.

Testing was an important part of the project, as it provided confidence that the core functionality works as intended and would not break with future modifications.

### `requirements.txt`
This file lists all dependencies required for the project. In this case, the file is intentionally left empty because the program uses only Python’s standard library.

---

## Design Choices
A few key design decisions shaped this project:

1. **JSON for Storage**: I chose JSON as the persistence format because it is human-readable, lightweight, and well-supported in Python’s standard library. It also allows for straightforward saving and loading of structured task data.
2. **Command-Line Interface**: Rather than building a graphical application, I opted for a CLI to keep the focus on logic and functionality rather than interface design. This makes the project simpler but still effective.
3. **Dictionary-Based Task Representation**: Each task is represented as a dictionary with fields such as `id`, `title`, `priority`, `due_date`, and `completed`. This structure is flexible and easy to serialize.
4. **Testing Individual Functions**: By isolating functionality into small, testable functions, I was able to ensure correctness more easily. This modular approach also made the codebase cleaner.

---

## Reflections
In developing this project, I deepened my understanding of how to structure Python programs with multiple files and functions, as well as how to write automated tests. I also gained experience thinking critically about data representation, user experience in a CLI environment, and persistence of application state.  

While the Task Manager is fairly minimal, it could be extended in many directions: support for recurring tasks, more advanced filtering, integration with external services, or even a web interface. However, the current implementation satisfies all requirements of the assignment while providing a useful, working application.

---
