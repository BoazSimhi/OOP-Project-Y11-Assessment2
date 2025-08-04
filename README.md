# OOP-Project-Y11-Assessment2
My Year 11 Software Engineering Assessment 2 (for Term 3). An OOP project called *Thane of Combat*.

*Thanes of Combat* is a riveting command line fantasy adventure-combat game written in Python. The project will use object-oriented principles and follow an Agile development paradigm using sprints, system design, and version control with Git and GitHub.

## Features

- Player has health, damage, and other attributes
- Fights enemies and receives xp for defeating them
- Player is able to level up and get stronger
- Fully object-oriented design using Python classes
- Manual testing and logging included in /docs


## Folder structure

```
OOP-Project-Y11-Assessment2/
│
├── Player.py   # Player class definition
├── Enemy.py    # Enemy class for creating different types of enemies
├── main.py     # Entry point and manual test runner
│
├── docs/
│   ├── SDS.md            # Software Design Specification (v1.0+)
│   ├── sprint1_log.md    # Completed log of sprint 1 with testing summary
│   └── sprint2_log.md    # Completed log of sprint 2 with testing summary
│
├── .gitignore            # Files excluded from version control
├── README.md             # Project overview and setup
```

## Requirements

- Python 3.x (standard library only)
- Standard Python libraries such as `os` and `random` for screen clearing and enemy selection

## Getting started

To run the app:

```bash
python3 main.py
```

To test functionality, read the sprint logs in `/docs` or use the checklists provided in GitBook.

## Development process

This project follows an Agile process, with incremental development across multiple sprints. Each sprint is documented in `/docs` with:

- Sprint goals and tasks completed
- Testing log and results
- Git commit history and version updates
- Reflections on improvements and next steps

## Version control

The project uses Git for version control. To contribute:

```bash
git clone git@github.com:BoazSimhi/OOP-Project-Y11-Assessment2.git
cd OOP-Project-Y11-Assessment2
```

Make your changes and push:

```bash
git add .
git commit -m "Describe your change"
git push
```

## License

This project is released under the MIT License for educational use.