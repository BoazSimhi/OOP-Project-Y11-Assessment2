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
- As a player, I want to be prevented from resting if my health is full so that healing actions aren’t wasted.

### Sprint 2
- As a player, I want to level up after reaching a reasonable amount of XP so that I feel rewarded for my success.
- As a player, I want to increase my stats when I level up so that I can tailor my character to my playstyle.
- As a player, I want only appropriate enemies to be selected based on my level so that I am not overwhelmed early or bored later.
- As a player, I want the game to give me clear feedback (like damage dealt and XP gained) so that I understand the consequences of my actions.
- As a developer, I want to validate player inputs so that errors and crashes are minimized.

### Possible Extensibility
- As a player, I want to use new items (like potions) during battle so that I can better manage my survival.
- As a player, I want enemies to drop loot occasionally so that I feel rewarded beyond XP.
- As a developer, I want to store Player progress in files so that the game can be saved and resumed later.
- As a developer, I want to allow importing/exporting of player/enemy data using CSV or JSON so that data can be updated externally.

## Use Cases

### Use Case 1: Create Player Character
- **Actors**: Player  
- **Description**: The player creates a character with a custom name and starting stats.  
- **Preconditions**: Game has started.  
- **Main Flow**:
  1. Prompt player to enter a name.
  2. Generate default or rolled stats.
  3. Instantiate `Player` object.
- **Postconditions**: Player character is created and stored in memory.

### Use Case 2: View Player Stats
- **Actors**: Player  
- **Description**: Player can view their current stats.  
- **Preconditions**: A `Player` object must exist.  
- **Main Flow**:
  1. Player selects the "view stats" option.
  2. `Player.display_stats()` is called.
  3. Stats are printed to the screen.
- **Postconditions**: Player sees their current state.

### Use Case 3: Enter Combat
- **Actors**: Player, Enemy  
- **Description**: Player engages in battle with an enemy.  
- **Preconditions**: Player is alive.  
- **Main Flow**:
  1. Game selects a level-appropriate enemy.
  2. Instantiate an `Enemy` object.
  3. Begin turn-based combat.
- **Postconditions**: Combat ends with player or enemy defeated.

### Use Case 4: Attack Enemy
- **Actors**: Player  
- **Description**: Player attacks an enemy, dealing damage.  
- **Preconditions**: Combat is active.  
- **Main Flow**:
  1. Player chooses "attack".
  2. `Player.attack(Enemy)` is called.
  3. Enemy health is reduced.
- **Postconditions**: Enemy takes damage or is defeated.

### Use Case 5: Enemy Attacks Player
- **Actors**: Enemy  
- **Description**: Enemy attacks the player.  
- **Preconditions**: Combat is active.  
- **Main Flow**:
  1. Enemy's turn begins.
  2. `Enemy.attack(Player)` is called.
  3. Player health is reduced.
- **Postconditions**: Player takes damage or dies.

### Use Case 6: Gain XP and Level Up
- **Actors**: Player  
- **Description**: Player earns XP after winning combat and may level up.  
- **Preconditions**: Enemy is defeated.  
- **Main Flow**:
  1. Player gains XP based on enemy difficulty.
  2. XP total is updated.
  3. If threshold met, `Player.level_up()` is called.
- **Postconditions**: Player levels up and selects a stat to increase.

### Use Case 7: Rest to Heal
- **Actors**: Player  
- **Description**: Player heals by resting.  
- **Preconditions**: Player is not at full health.  
- **Main Flow**:
  1. Player chooses "rest".
  2. `Player.rest()` is called.
  3. Health increases by wisdom amount.
- **Postconditions**: Health is restored (not beyond max).

### Use Case 8: Prevent Rest at Full Health
- **Actors**: Player  
- **Description**: Player is prevented from resting when at full health.  
- **Preconditions**: Health is already at max.  
- **Main Flow**:
  1. Player chooses "rest".
  2. System checks current health.
  3. Message displayed: "Health is already full."
- **Postconditions**: No changes to health or state.

### Use Case 9: Random Enemy Selection
- **Actors**: System  
- **Description**: Game selects a random enemy appropriate to player's level.  
- **Preconditions**: Combat initiated.  
- **Main Flow**:
  1. Filter enemy list by `Enemy.difficulty`.
  2. Use random module to pick one.
  3. Instantiate that enemy.
- **Postconditions**: Enemy appears in combat.

### Use Case 10: Input Validation
- **Actors**: System  
- **Description**: Game validates user inputs to prevent crashes.  
- **Preconditions**: User is prompted for input.  
- **Main Flow**:
  1. Input received from user.
  2. Checked against valid options.
  3. Invalid input causes error message and re-prompt.
- **Postconditions**: Safe, continuous game loop.

### (Optional) Use Case 11: Use Item
- **Actors**: Player  
- **Description**: Player uses an item such as a potion.  
- **Preconditions**: Player has item in inventory.  
- **Main Flow**:
  1. Player selects item.
  2. Item effect is applied.
  3. Item removed from inventory.
- **Postconditions**: Health/stats change; item consumed.

### (Optional) Use Case 12: Save and Load Game
- **Actors**: Player, System  
- **Description**: Game state is saved to or loaded from a file.  
- **Preconditions**: Player chooses "save" or "load".  
- **Main Flow**:
  1. For save: serialize `Player` to file (e.g. CSV, JSON).
  2. For load: read file and reconstruct `Player`.
- **Postconditions**: Game resumes from saved state.


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

**Sprint 2 - Required for the MVP**
- Filter possible enemies to fight by their difficulty
- Implement Player levelling-up capability with stat increase
- Enhance user feedback and validation
- Allow the user to input their own name for the player

**Sprint 3 - Optional Further Development** 
- Add `critical_chance` for player and/or enemy attacks
- Allow the user to 'roll' for their initial stats
- Extend user interface with command menus
- Add automated tests for core functionality
- Final documentation and polish

## Extensibility
The design supports easy addition of new features. Possibly a new class for `Items` such as potions that could be stored in an `inventory` for the `Player` class. Attributes such as `critical_chance`, `dodge_chance`, or `droppable_loot` can be added to the `Enemy` class. More advanced user interface options or external file formats (e.g. CSV, JSON) can be implemented with minimal disruption to the system architecture - especially to add data persistence in storing the `Player` statistics.

## Author
Boaz Simhi - Stage 6 Software Engineering Student  
2025