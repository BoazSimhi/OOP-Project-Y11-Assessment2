# Software Design Specification (SDS)

## Project name
NAME OF PROJECT

## Version
v1.0 – Initial system design (covers all planned features across sprints)

## Overview
PROJECTF OVERVIEW

The system design outlined here covers the full project scope, even though features will be implemented gradually over time.

## System architecture
The system consists of two main classes:

- `NAME`: Represents ______________________.
- `OTHER NAME`: ____________________.

The program is designed for terminal-based use and avoids GUI dependencies. Each sprint builds on the existing functionality.

## Class descriptions

### CLASS 1

| Attribute       | Type     | Description                                 |
|----------------|----------|---------------------------------------------|
| `title`        | `str`    | Short label describing the task             |
| `description`  | `str`    | Detailed explanation of the task            |
| `due_date`     | `str`    | Task deadline (in YYYY-MM-DD format)        |
| `is_complete`  | `bool`   | True if task is completed, otherwise False  |

| Method              | Description                                |
|---------------------|--------------------------------------------|
| `mark_complete()`   | Sets `is_complete` to `True`               |
| `mark_incomplete()` | Sets `is_complete` to `False`              |
| `display_summary()` | Prints a short overview of the task        |
| `display_details()` | Prints all information about the task      |

### CLASS 2

| Attribute | Type        | Description                                |
|-----------|-------------|--------------------------------------------|
| `tasks`   | `list[Task]`| Stores all created Task objects            |

| Method                    | Description                                         |
|---------------------------|-----------------------------------------------------|
| `add_task(task)`          | Adds a Task object to the list                      |
| `list_tasks()`            | Prints a summary of all tasks                       |
| `find_task(title)`        | Searches for a Task by title and returns it         |
| `remove_task(title)`      | Removes a task from the list by its title           |
| `get_completed_tasks()`   | Returns a list of completed tasks                   |
| `get_incomplete_tasks()`  | Returns a list of incomplete tasks                  |
| `display_all_tasks()`     | Prints full details of all tasks                    |
| `save_to_file(filename)`  | (Planned) Saves tasks to a file in structured format|
| `load_from_file(filename)`| (Planned) Loads tasks from file into memory         |
| `filter_by_status()`      | (Planned) Returns tasks based on completion         |
| `sort_by_due_date()`      | (Planned) Sorts tasks chronologically               |

## Assumptions and constraints
- The application runs in a command-line interface (CLI) only.
- All data is stored in memory initially; persistence will be added in later sprints.
- OTHER ASSUMPTION/CONSTRAINT
- Python 3 standard library MAYBE EXTERNAL DEPENDENCIES?

## Planned features by sprint

**Sprint 1**
- Things
- I'll
- Do
- in Sprint 1

**Sprint 2**
- Things
- I'll
- Do
- in Sprint 2

**Sprint 3**
- Optional: SOmething
- Something
- Add automated tests for core functionality
- Final documentation and polish

## Extensibility
The design supports easy addition of new features. Attributes such as `priority`, `category`, or `created_at` can be added to the `Task` class. More advanced user interface options or external file formats (e.g. CSV, JSON) can be implemented with minimal disruption to the system architecture. SOME STUFF ABOUT EXTENSIBILITY

## Author
Boaz Simhi - Stage 6 Software Engineering Student  
2025