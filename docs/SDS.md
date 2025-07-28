# Software Design Specification (SDS)

## Project name
Thane of Combat

## Version
v1.0 – Initial system design (covers all planned features across sprints)

## Overview
*Thane of Combat* is a command-line game built in Python in which the Player fights enemies, gaining xp and levelling up with their victories. It is developed using object-oriented design and an agile workflow. The app is built incrementally over several sprints, each delivering a functional stage of development. Features include creating a player with stats, managing them in memory, selecting level-appropriate enemies to fight, the player gaining xp for defeating enemies, and levelling up where they can increase their stats.

The system design outlined here covers the full project scope, even though features will be implemented gradually over time.

## System architecture
The system consists of two main classes:

- `Player`: Represents the Player character with attributes such as health, damage, level, and xp.
- `Enemy`: For creating different types of enemies and assigning them similar attributes to the Player so that the Player can engage in text-based combat.

The program is designed for terminal-based use and avoids GUI dependencies. Each sprint builds on the existing functionality.

## User Stories

### Sprint 1
- As a player, I want to create a character with a name and starting stats so that I can begin my journey in the game.
- As a player, I want my character to have stats like strength, wisdom, health, and level so that my performance in battle reflects my build.
- As a player, I want to view my stats between rounds of combat so that I can plan my next move.
- As a player, I want to fight a variety of fantasy-themed enemies with unique stats so that the combat feels dynamic.
- As a player, I want enemies to deal damage to me during combat so that the battles feel risky and challenging, but still fair.
- As a player, I want to gain XP after defeating enemies so that I can progress and eventually level up.
- As a player, I want to see enemies selected randomly so that each playthrough feels different.
- As a developer, I want core Player and Enemy classes with key methods implemented so that the game loop can be built around them.
- As a player, I want the game to have a basic loop of fighting enemies and resting so that I can keep playing without restarting.

### Sprint 2
- As a player, I want to level up after reaching a reasonable amount of XP so that I feel rewarded for my success.
- As a player, I want to increase my stats when I level up so that I can tailor my character to my playstyle.
- As a player, I want only appropriate enemies to be selected based on my level so that I am not overwhelmed early or bored later.
- As a player, I want the game to give me clear feedback (like damage dealt and XP gained) so that I understand the consequences of my actions.
- As a player, I want to be prevented from resting if my health is full so that healing actions aren’t wasted.
- As a developer, I want to validate player inputs so that errors and crashes are minimized.

### Possible Extensibility
- As a player, I want to use new items (like potions) during battle so that I can better manage my survival.
- As a player, I want enemies to drop loot occasionally so that I feel rewarded beyond XP.
- As a developer, I want to store Player progress in files so that the game can be saved and resumed later.
- As a developer, I want to allow importing/exporting of player/enemy data using CSV or JSON so that data can be updated externally.


## Class descriptions

### Player

| Attribute       | Type     | Description                                 |
|----------------|----------|---------------------------------------------|
| `name`        | `str`    | The Player's name             |
| `strength`     | `int`    | The Player's damage they are able to deal when they `attack()`     |
| `wisdom`  | `int`   | How much the Player is able to heal when they `rest()`  |
| `current_health`  | `int`    | The Player's remaining health            |
| `max_health`  | `int`    | The Player's maximum health capacity      |
| `level`  | `int`   | The Player's level, indicating their progress in the game  |
| `xp`  | `int`   | How close the player is to levelling up  |


| Method              | Description                                |
|---------------------|--------------------------------------------|
| `attack(target)`   | Reduces `Enemy.health` by `strength`               |
| `rest()` | Increases `Player.health` by `wisdom`              |
| `display_stats()` | Prints the `Player` object's statistics   |
| `level_up()` | Allows the Player to increase one of their attributes     |
| `death()` | When the Player's `health` reaches 0 they die    |

### Enemy

| Attribute | Type        | Description                                |
|-----------|-------------|--------------------------------------------|
| `name`        | `str`    | The Enemy's name             |
| `strength`     | `int`    | The Enemy''s damage they are able to deal when they `attack()`     |
| `current_health`  | `int`    | The Enemy's remaining health            |
| `max_health`  | `int`    | The Enemy's maximum health capacity      |
| `difficulty`  | `int`   | To determine at what `Player level` this enemy should be fought  |

| Method                    | Description                                         |
|---------------------------|-----------------------------------------------------|
| `attack(target)`      | Reduces `Player.health` by `strength`                      |


## Assumptions and constraints
- The application runs in a command-line interface (CLI) only.
- All data is stored in memory initially; persistence will be added in later sprints.
- Python 3 standard library and minimal external dependencies (`os`, `random`).

## Planned features by sprint

**Sprint 1**
- Files for Player and Enemy classes created, as well as an MVP for both classes coded
- Instantiate different enemies with relevant attributes
- Display Player stats and full details
- Pseudo-randomly select an enemy to fight
- Add xp gain for when the Player defeats an enemy
- Create a MVP with the most of the core game loop in place

**Sprint 2**
- Filter possible enemies to fight by their difficulty
- Implement Player levelling-up capability with stat increase
- Enhance user feedback and validation
- Allow the user to input their own name for the player

**Sprint 3**
- Optional: Add `critical_chance` for enemy attacks
- Extend user interface with command menus
- Add automated tests for core functionality
- Final documentation and polish

## Extensibility
The design supports easy addition of new features. Possibly a new class for `Items` such as potions that could be stored in an `inventory` for the `Player` class. Attributes such as `critical_chance`, `dodge_chance`, or `droppable_loot` can be added to the `Enemy` class. More advanced user interface options or external file formats (e.g. CSV, JSON) can be implemented with minimal disruption to the system architecture - especially to add data persistence in storing the `Player` statistics.

## Author
Boaz Simhi - Stage 6 Software Engineering Student  
2025