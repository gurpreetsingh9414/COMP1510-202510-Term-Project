# 🏰 Patiala House – A Single User Dungeon (SUD)

**Author:** Gurpreet Singh  
**Student ID:** A01405950

---

## 🎮 About the Game

"Patiala House" is a text-based Single User Dungeon (SUD) that invites players into a mythological rich grid world
based on ancient Indian legends.
Explore hidden rooms, battle or outwit foes, solve riddles, and level up to conquer the
final chamber.
The game is built using Python and runs in a terminal.

---

## ▶️ How to Run

```bash
python game.py
```

Use `w`, `a`, `s`, `d` to move (north, west, south, east). Type `status` anytime to check your character’s stats.

---

## 🧪 File Structure and Function Map

| **Feature**                                  | **Function / Line #**                         |
|----------------------------------------------|-----------------------------------------------|
| Entry point / main function                  | `main()` – Line 649                           |
| Character creation                           | `make_character()` – Line 58                  |
| Game board creation                          | `make_board()` – Line 19                      |
| Dictionary comprehension                     | Used in `make_board()` – Line 42              |
| Movement logic                               | `move_character()` – Line 250                 |
| Movement validation                          | `validate_move()` – Line 224                  |
| Display current location                     | `describe_current_location()` – Line 84       |
| Draw player map                              | `draw_map()` – Line 130                       |
| Game loop logic                              | `game_loop()` – Line 387                      |
| Experience system                            | `gain_xp()` – Line 308                        |
| Leveling system                              | `level_up()` – Line 283                       |
| Final win condition                          | `game_loop()` – Line 393 & 395                |
| Game over banner                             | `print_game_over_banner()` – Line 603         |
| Welcome banner                               | `print_welcome_banner()` – Line 617           |
| Minigame: Number Guessing                    | `number_guessing_game()` – Line 432           |
| Minigame: Rock-Paper-Scissors                | `rock_paper_scissors()` – Line 452            |
| Minigame: Riddle                             | `riddle_game()` – Line 475                    |
| XP and foe difficulty scaling                | `check_for_foe()` – Line 424                  |

---

## ✅ Python Feature Checklist

| **Requirement**                                        | **Location in Code (`game.py`)**                                                                                |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| (a) Immutable data structures (tuples)                 | Used as dictionary keys in `make_board()` — Line **42**, also in `validate_move()` — Line **176 to 179**        |
| (b) Mutable structures used thoughtfully (lists/dicts) | `character` dictionary — Line **65**, `descriptions` list — Line **31**                                         |
| (c) Exception handling                                 | `try/except` in `number_guessing_game()` — Line **315**                                                         |
| (d) Minimized scope/lifetime of variables              | All variables declared locally inside functions — throughout                                                    |
| (e) Small, reusable, independent functions             | Modular functions like `move_character()`, `gain_xp()`, `draw_map()` etc.                                       |
| (f) Simple and flat code                               | No deeply nested blocks; flat and readable logic in `game_loop()`                                               |
| (g) Comprehensions used correctly                      | Dictionary comprehension in `make_board()` — Line **42**                                                        |
| (h) Selection using `if` statements                    | Used in `move_character()` — Line **200**, `gain_xp()`, `is_alive()`                                            |
| (i) Repetition using `for` and `while` loops           | `draw_map()` — Line **109**, `game_loop()` — Line **401**                                                       |
| (j) Membership operator (`in`)                         | `if direction in directions:` — Line **152**, `if coord in board:` — Line **176**                               |
| (k) `range()` function usage                           | Used with `product(range(...))` in `make_board()` — Line **42**, and in `draw_map()` — Line **109 & 119**       |
| (l) Use of `itertools.product()`                       | Used to generate coordinate grid in `make_board()` — Line **42**                                                |
| (m) Use of `random` module                             | `random.choice`, `random.randint`, `random.random` in `make_board()`, `number_guessing_game()`, `riddle_game()` |
| (n) Docstrings with parameters and return descriptions | Every function includes detailed docstrings — throughout                                                        |
| (o) Doctests or unit tests for all testable functions  | Found in `make_board()` — Line **10**, `gain_xp()` — Line **308**, etc.                                         |
| (p) Output formatted using f-strings                   | Found in `describe_current_location()` — Line **88**, `gain_xp()` — Line **283**, etc.                          |

---

## 🏁 Game Objectives

- 🎯 Reach **Level 3** and accumulate **21 XP**
- OR, arrive at the final coordinate `(4, 4)` at Level 3

### 💀 Game Over Condition

- HP reaches **0** — character dies

---

