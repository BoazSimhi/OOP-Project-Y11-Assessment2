# OOP Project Sprint Log: Sprint 1

## Sprint goal
To implement the core object-oriented structure of *Thane of Combat*, including:
- Definition of the `Player` and `Enemy` classes
- Methods for `Enemy.attack(target)`, `Player.attack(target)`, `Player.rest()`, `Player.display_stats()`, and `Player.death()`
- Manual testing via `main.py`
- Internal documentation and preparation for future extension

---

## Tasks completed
- Created `Player.py` containing `Player` class with attributes: `name`, `strength`, `wisdom`, `max_health`, `level`, `xp`, and `current_health`
- Implemented methods in `Player`: `attack(target)`, `rest()`, `display_stats()`, `death()`
- Created `Enemy.py` containing `Enemy` class with attributes: `name`, `strength`, `max_health`, `current_health` and `difficulty`
- Implemented the `attack(target)` method in `Enemy`
- Wrote `main.py` to instantiate the user as a `Player` object and all the types of enemies as `Enemy` objects, demonstrating functionality through print-based interaction
- Added test examples with known input to verify core behaviour
- Prepared `README.md` and initial SDS to describe app architecture and constraints
- Created User stories in SDS

---

## Resources used
- Python documentation (class syntax, list operations, Boolean logic)
- GitBook Module 222 for system design and class modelling
- AI assistant (ChatGPT) used only: (No AI assistance for coding was used)
- - To review initial SDS
- - Provide ideas for enemy types
- - Help with formatting
- - Creating User stories for SDS
- Internal test cases designed using pre-defined inputs and expected outputs

---

## Testing log

| Test case | Input | Expected outcome | Actual outcome | Notes |
|-----------|-------|------------------|----------------|-------|
| Instantiate `Enemy` objects | Running `main.py` file | Objects of `Enemy` created | Confirmed | The class works as intended |
| Attack `Enemy` | call `Player.attack(enemy)` | `Enemy.current_health -= Player.strength` | Confirmed | Display updated |
| Player `rest`ing to heal | call `Player.rest()` | `current_health += wisdom` | Confirmed | Player is able to heal by the correct amount |
| Display the player's stats | `Player.display_stats()` | All stats are outputted | Confirmed | Formatted nicely too |
| Player dies | `Player.death()` | Some text output and code stopping | Confirmed | exit() is run at the end |
| Enemy attacks the Player | `Enemy.attack(Player)` | `Player.current_health -= Enemy.strength` | Confirmed | Is able to kill the player as intended |
| Running core game loop | Running `main.py` | Turn-based gameplay loops | Confirmed | Player does not yet level up |
| Non-existant player action | action does not exist | Output "Invalid choice." and able to choose again | Confirmed | Safe fallback |


---

## Version control
- Initialised Git repository in GitHub
- Created `Player.py`, `Enemy.py`, `main.py`, and committed first draft
- Commits made incrementally by component: `Player`, `Enemy`, main logic
- `.gitignore` added to exclude PyCharm and OS metadata
- Pushed to public GitHub repo using SSH

---

## Reflections
- Defining two tightly-focused classes helped clarify object-oriented structure early
- User input works fine and has clearly outlined possible options
- Separating summary from detail output improved readability and potential for reuse
- All tasks in Sprint 1 were completed without needing to restructure code
- The system design anticipates extension with filters, file storage, and user interface without requiring major changes to the current classes
- Core gameplay loop is able to be expanded for future sprints with relative ease

---

## Notes for next sprint
- Implement logic for `Player.level_up()` method
- Create algorithm to select an appropriately difficult enemy for the player to fight
- Improve command-line menu system
- Ensure SDS remains aligned to changes made to the overall class structure
- Allow the user to input their own name for the player
