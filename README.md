# Mystery Island — The Lost Lighthouse

## Project Description

Mystery Island is a text-based adventure game developed using Python.

The player wakes up on a mysterious island and must explore different locations, collect useful items, and restore the light of an abandoned lighthouse.

The player starts with 5 energy points and must complete the mission before running out of energy.

## Game Features

- Player name input.
- Five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Energy management system.
- Rope collection at the Beach.
- Lantern collection inside the Cave.
- Rope required to cross the Old Bridge.
- Lantern required to activate the Lighthouse.
- Valid movements consume one energy point.
- Invalid movements do not consume energy.
- Win and Game Over conditions.
- Quit Game option.
- Replay system.
- Automated Unit Testing using Python unittest.

## Project Structure

```text
mystery-island/
├── main.py
├── test_game.py
└── README.md
```

## Requirements

- Python 3
- No external libraries required.

## How to Run the Game

Open a terminal inside the project folder.

Run:

```bash
python3 main.py
```

Enter your name and follow the instructions displayed in the terminal.

## How to Play

The player starts at the Beach with 5 energy points.

1. Search for the Rope at the Beach.
2. Travel to the Jungle.
3. Enter the Cave.
4. Search for the Lantern.
5. Use the Rope to cross the Old Bridge.
6. Travel to the Lighthouse.
7. Activate the Lighthouse using the Lantern.

The player wins by activating the lighthouse before running out of energy.

## Game Controls

| Number | Action |
|---|---|
| 1 | Explore the Beach |
| 2 | Go to the Jungle |
| 3 | Go to the Cave |
| 4 | Quit Game |
| 5 | Search for Rope |
| 6 | Go to the Old Bridge |
| 7 | Search for Lantern |
| 8 | Go to the Lighthouse |
| 9 | Activate the Lighthouse |

## Energy System

The player starts with 5 energy points.

Each successful movement to another location costs one energy point.

Searching for items does not consume energy.

Invalid movements do not consume energy.

If the player's energy reaches zero, the game ends.

## Winning Condition

The player must reach the Lighthouse with the Lantern and activate its light.

When successful, the game displays:

```text
Congratulations! You activated the Lighthouse!
YOU WIN!
```

## Replay System

After winning, losing, or quitting, the player can choose to restart the game.

Entering `yes` starts a new game with 5 energy points, the Beach as the starting location, and an empty inventory.

Entering `no` exits the game.

## Unit Testing

The project includes 12 automated unit tests using Python's built-in `unittest` framework.

To run the tests:

```bash
python3 -m unittest test_game.py -v
```

The tests cover starting conditions, item collection, movement restrictions, energy management, bridge requirements, lighthouse activation, winning, game over, and player state reset.

### Test Results

```text
Ran 12 tests in 0.003s

OK
```

All 12 unit tests passed successfully.

## Technologies Used

- Python 3
- Python unittest
- Visual Studio Code
- Git and GitHub

## Project Status

Completed and tested locally.

## Conclusion

Mystery Island demonstrates fundamental Python programming concepts, including variables, dictionaries, functions, conditional statements, loops, user input, and automated testing.