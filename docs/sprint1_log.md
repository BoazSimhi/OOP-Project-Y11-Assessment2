# OOP Project Sprint Log: Sprint 1

## Sprint goal
To implement the core object-oriented structure of the *Thanes of Combat*, including:
- Definition of the `Player` and `Enemy` classes
- Methods for ________, ______, and ________
- Manual testing via `main.py`
- Internal documentation and preparation for future extension

---

## Tasks completed
- Created `CLASS1.py` containing `CLASS` class with attributes: `title`, `description`, `due_date`, `is_complete`
- Implemented methods in `CLASS1`: `mark_complete()`, `mark_incomplete()`, `display_summary()`, `display_details()`
- Created `CLASS2.py` containing `CLASS2` class with an internal list of Task objects
- Implemented methods in `TaskManager`: `add_task()`, `list_tasks()`, `find_task()`, `remove_task()`, `get_completed_tasks()`, `get_incomplete_tasks()`, `display_all_tasks()`
- Wrote `main.py` to instantiate Task and TaskManager objects and demonstrate functionality through print-based interaction
- Added test examples with known input to verify core behaviour
- Prepared `README.md` and initial SDS to describe app architecture and constraints
- Added TODO comments to `main.py` to guide future iterations
- Drafted Markdown checklist for student verification of Sprint 1 feature completion

---

## Resources used
- Python documentation (class syntax, list operations, Boolean logic)
- GitBook Module 222 for system design and class modelling
- AI assistant (ChatGPT) used to review my work and for feedback
- Internal test cases designed using pre-defined inputs and expected outputs

---

## Testing log DO THIS WHEN I FINISH THE SPRINT

| Test case | Input | Expected outcome | Actual outcome | Notes |
|-----------|-------|------------------|----------------|-------|
| Add task to manager | 2 Task objects | Appears in list | Confirmed | Order preserved |
| Mark task complete | call `mark_complete()` | `is_complete = True` | Confirmed | Display updated |
| Toggle task status | call `mark_incomplete()` | `is_complete = False` | Confirmed | Reliable state change |
| Display summary | task.display_summary() | Title + ✓/✗ | Confirmed | Status shown correctly |
| Display details | task.display_details() | Title, desc, due, status | Confirmed | Good for debugging |
| Find task by title | valid and invalid titles | Returns object or None | Confirmed | Case-sensitive |
| Remove task | title exists | Task removed | Confirmed | Shrinks list |
| Remove missing task | title does not exist | No crash | Confirmed | Safe fallback |
| List completed tasks | 1 complete, 1 incomplete | Returns correct subset | Confirmed | Used comprehension |
| List incomplete tasks | See above | Returns correct subset | Confirmed | Symmetrical logic |

---

## Version control
- Initialised Git repository in GitHub
- Created `Player.py`, `Enemy.py`, `main.py`, and committed first draft
- Commits made incrementally by component: `Player`, `Enemy`, main logic
- `.gitignore` added to exclude PyCharm and OS metadata
- Pushed to public GitHub repo using SSH

---

## Reflections DO THIS WHEN DONE THE SPRINT
- Defining two tightly-focused classes helped clarify object-oriented structure early
- Avoiding user input at this stage allowed complete testing through method calls
- Separating summary from detail output improved readability and potential for reuse
- All tasks in Sprint 1 were completed without needing to restructure code
- The system design anticipates extension with filters, file storage, and user interface without requiring major changes to the current classes

---

## Notes for next sprint DO THIS WHEN DONE THE SPRINT
- Prepare file format for saving/loading task data
- Decide on internal vs external ID strategy for uniquely identifying tasks
- Design a flexible command-line menu system or CLI interface layer
- Begin drafting basic error handling for bad input or invalid operations