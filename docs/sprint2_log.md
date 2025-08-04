# OOP Project Sprint Log: Sprint 2

## Sprint goal
To complete the MVP (Minimum Viable Product) of *Thane of Combat*, including:
- Filtering possible enemies to fight by their `difficulty` attribute
- Implement Player levelling-up capability with stat increase
- Enhancing user feedback and validation
- Allowing the user to input their own name for the player
- Manual testing via `main.py`
- Internal documentation and preparation for possible future extension

---

## Tasks completed
- Implemented `level_up()` class in `Player` class to increase the player's `max_health` by 2, fuly heal the player, and give them a choice of `strength`, `wisdom`, or `max_health` to increase/further increase
- Implemented algorithm in `main.py` to select an appropriate `Enemy` object to fight based on their `difficulty`
- Allowed the user to input a string as the `Player`'s `name` attribute
- Improved command-line outputs in `main.py` to make the users' necessary inputs clearer, thus demonstrating functionality through print-based interaction
- Added test examples with known input to verify final behaviour
- Updates `README.md` and `SDS.md` to fully describe app architecture and constraints

---

## Resources used
- Python documentation (class syntax, list operations, Boolean logic)
- GitBook Module 222 for system design and class modelling
- AI assistance only for testing cases in sprint log and refining SDS
- Further internal test cases designed using pre-defined inputs and expected outputs

---

## Testing log

| Test Case  | Input  | Expected Outcome   | Actual Outcome | Notes |
|------------|--------|--------------------|----------------|-------|
| Player chooses their name at creation  | Any string input                     | Name is stored and used in game                               | Confirmed  | Output confirms name and stats             |
| Level up when XP threshold reached     | XP >= threshold                      | Level increases by 1, `level_up()` called                      | Confirmed  | Player prompted to choose stat to increase |
| Stat increase on level up              | Choose stat during `level_up()`      | Selected stat value increases                             | Confirmed  | Works for strength, wisdom, and max_health |
| Enemy selection based on player level  | Player level 1-3                     | Only enemies with matching difficulty appear                   | Confirmed  | No overpowered enemies encountered         |
| XP awarded correctly                   | Defeat enemy                         | XP increases based on enemy defeated                           | Confirmed | Output displays XP gained                  |
| Input validation                       | Enter invalid option (e.g. typo)     | Outputs "Invalid choice." and reprompts                        | Confirmed  | Game doesn’t crash                         |
| Feedback on actions                    | Attack, heal, level up, etc.         | Descriptive output shown (damage dealt, XP gained, etc.)       | Confirmed                                  | All actions provide clear console feedback |
| Prevent stat overflow                  | Attempt to increase stat repeatedly  | Stat increases only by allowed amount                          | Confirmed                                  | No errors encountered                      |


---

## Version control
- Consistently commited to Git repository on local machine
- Commits made incrementally by component: updates to main logic, `Player.level_up()`, edits to documents and other changes
- Pushed to public GitHub repo using SSH

---

## Reflections DO THIS SECTION
- Defining two tightly-focused classes helped clarify object-oriented structure early
- User input works fine and has clearly outlined possible options
- Separating summary from detail output improved readability and potential for reuse
- All tasks in Sprint 1 were completed without needing to restructure code
- The system design anticipates extension with filters, file storage, and user interface without requiring major changes to the current classes
- Core gameplay loop is able to be expanded for future sprints with relative ease

---

## Notes for (optional) next sprint
- Implement the `critical_chance` attribute for `Player` and/or `Enemy` objects
- Improve enemy selection algoriithm
- Decide whether to store player data to an external file to add permanence
- Improve command-line menu system
- Ensure SDS remains aligned to changes made to the overall class structure
- Possibly allow the user to randomly 'roll' for their stats
