"""
Gurpreet Singh
A01405950
"""

import random


def make_board(rows, columns):
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    reset = "\033[0m"

    descriptions = [
        blue + "THE ASHOKA CHAMBER - Ancient inscriptions glow faintly on the sandstone walls. The air is heavy with the wisdom of Emperor Ashoka’s edicts.\nYou feel a strange pull — as if the Mauryan spirit still lingers here." + reset,
        green + "THE TRIDENT SHRINE - Three blazing torches illuminate a stone statue of Lord Shiva, his trident piercing the air above.\nEchoes of the Tandava dance resonate through the cold granite floor." + reset,
        yellow + "THE MUGHAL VAULT - Intricate Mughal arches crown the room, and faded Persian calligraphy adorns the dome.\nA dusty scent of oud lingers, and in the center lies a broken royal seal — perhaps once belonging to Shah Jahan himself." + reset,
        blue + "THE VIMANA HALL - Carvings of flying machines and celestial beings cover every inch of this temple-like space.\nLegends say the sages of ancient India once built vehicles to travel across dimensions — could one be hidden here?" + reset,
        cyan + "THE SUNKEN DWARKA RUINS - You tread through damp stone as ancient pillars rise from a waterlogged floor.\nA golden conch lies half-buried — perhaps once blown by Krishna himself before battle. The sea whispers stories of the lost city." + reset,
        magenta + "THE KURUSHETRA BATTLEFIELD ECHO - Dust and silence fill the room — but the ground trembles with ancient cries.\nWeapons are embedded in the floor, and a spectral chariot flickers in and out of view. This is where destinies were once rewritten." + reset,
        yellow + "THE AGNI PASSAGE - The walls pulse with heat, carved with flames and Vedic mantras.\nThis sacred tunnel is said to be blessed by Agni, the fire god. Only those with pure intent may pass unharmed." + reset,
        green + "THE MAURYA TREASURY - Gold coins stamped with the seal of Chandragupta Maurya are scattered across the floor.\nBut beware — the wealth is guarded by mechanical traps rumored to have been designed by Chanakya himself." + reset
    ]

    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(descriptions)
    return board


def make_character():
    return {
        "X": 0,
        "Y": 0,
        "HP": 5,
        "Max HP": 5,
        "Level": 1,
        "XP": 0,
        "XP to next": 5
    }


def describe_current_location(board, character):
    x, y = character["X"], character["Y"]
    print(f"\nYou are at ({x}, {y}).")
    print("Location:", board[(x, y)])


def draw_map(character, rows=5, columns=5):
    reset = "\033[0m"
    player_color = "\033[1;32m"
    finish_color = "\033[1;31m"
    tile_color = "\033[1;34m"
    red = "\033[1;31m"
    print("\n" + red + "Map:" + reset)
    for row_s in range(rows):
        row = ""
        for col_s in range(columns):
            if (row_s, col_s) == (character["X"], character["Y"]):
                row += player_color + "[P]" + reset
            elif (row_s, col_s) == (4, 4):
                row += finish_color + "[F]" + reset
            else:
                row += tile_color + "[ ]" + reset
        print(row)


def show_status(character):
    blue = "\033[94m"
    reset = "\033[0m"

    print(blue + "\n=== Player Status ===" + reset)
    for key, value in character.items():
        print(f"{key}: {value}")
    print(blue + "\n=====================" + reset)


def get_direction():
    directions = {"w": "north", "s": "south", "d": "east", "a": "west"}
    while True:
        print("\nMove:")
        print("w. North\ns. South\nd. East\n. West")
        choice = input("Enter: ")
        if choice in directions:
            return directions[choice]
        print("Invalid. Try again.")


def validate_move(character, direction, board):
    x, y = character["X"], character["Y"]
    if direction == "north": return (x - 1, y) in board
    if direction == "south": return (x + 1, y) in board
    if direction == "east": return (x, y + 1) in board
    if direction == "west": return (x, y - 1) in board
    return False


def move_character(character, direction):
    if direction == "north":
        character["X"] -= 1
    elif direction == "south":
        character["X"] += 1
    elif direction == "east":
        character["Y"] += 1
    elif direction == "west":
        character["Y"] -= 1


def is_alive(character):
    return character["HP"] > 0


def level_up(character):
    if character["Level"] >= 3:
        return
    character["Level"] += 1
    character["XP"] = 0
    character["XP to next"] += 2
    character["Max HP"] += 2
    character["HP"] = character["Max HP"]
    print(f"\n🎉 Leveled up to Level {character['Level']}!")
    print(f"Max HP is now {character['Max HP']}.")
    character["X"], character["Y"] = 0, 0
    print("You are sent back to the start.")


def gain_xp(character, amount):
    character["XP"] += amount
    print(f"You gained {amount} XP!")
    while character["XP"] >= character["XP to next"]:
        level_up(character)


def check_for_foe(character):
    chance = 0.25 if character["Level"] < 3 else 0.33
    return random.random() < chance


def number_guessing_game(character):
    print("Number guessing challenge!")
    answer = random.randint(1, 5)
    try:
        guess = int(input("Guess (1-5): "))
        if guess == answer:
            print("Correct!")
            gain_xp(character, 2)
        else:
            print("Wrong! -1 HP")
            character["HP"] -= 1
    except ValueError:
        print("Invalid! -1 HP")
        character["HP"] -= 1


def rock_paper_scissors(character):
    print("Rock-Paper-Scissors!")
    enemy = random.choice(['rock', 'paper', 'scissors'])
    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid! -1 HP")
        character["HP"] -= 1
        return
    print(f"Enemy chose {enemy}.")
    if player == enemy:
        print("Tie. Escape!")
    elif (player == 'rock' and enemy == 'scissors') or \
            (player == 'paper' and enemy == 'rock') or \
            (player == 'scissors' and enemy == 'paper'):
        print("You win!")
        gain_xp(character, 2)
    else:
        print("You lose! -1 HP")
        character["HP"] -= 1


def riddle_game(character):
    riddles = [
        ("What has keys but can't open locks?", "keyboard"),
        ("What gets wetter as it dries?", "towel"),
        ("What has hands but can't clap?", "clock"),
        ("What runs but never walks?", "water"),
        ("I speak without a mouth and hear without ears. What am I?", "echo")
    ]
    question, answer = random.choice(riddles)
    print("Riddle Challenge:")
    print(question)
    guess = input("Answer: ").lower().strip()
    if guess == answer:
        print("Correct!")
        gain_xp(character, 3)
    else:
        print(f"Wrong! The answer was '{answer}'. -1 HP")
        character["HP"] -= 1


def game_loop(board, character):
    while is_alive(character):
        describe_current_location(board, character)
        draw_map(character)

        if character["Level"] == 3 and (character["X"], character["Y"]) == (4, 4):
            print("\n👑 YOU WIN! You conquered all 3 levels!")
            print_game_over_banner()
            return

        if character["Level"] == 3 and random.random() < 0.33:
            print("A strange whisper asks you a question...")
            riddle_game(character)
            if not is_alive(character):
                break

        purple = "\033[95m"
        green = "\033[92m"
        reset = "\033[0m"

        cmd = input(
            purple + "\nEnter direction (w,s,d,a) or " + green + "'status'" + purple + ": " + reset
        ).lower().strip()

        if cmd == "status":
            show_status(character)
            continue

        direction_map = {"w": "north", "s": "south", "d": "east", "a": "west"}
        if cmd not in direction_map:
            print("Invalid.")
            continue

        direction = direction_map[cmd]
        if validate_move(character, direction, board):
            move_character(character, direction)
            if check_for_foe(character):
                print("\n⚔️ A foe appears!")
                if character["Level"] == 1:
                    number_guessing_game(character)
                elif character["Level"] == 2:
                    rock_paper_scissors(character)
                else:
                    riddle_game(character)

            # Gain XP or Level up if standing on goal square and not already at max level
            if (character["X"], character["Y"]) == (4, 4):
                if character["Level"] < 3:
                    print("You feel stronger after reaching the end of the maze.")
                    gain_xp(character, 3)  # Instant level up
        else:
            print("You can't go that way!")

    print("\n💀 Game Over. You ran out of HP.")


def print_game_over_banner():
    green = "\033[1;32m"
    reset = "\033[0m"
    print(green + r"""
   ____                         ___                 
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   

               G A M E   O V E R
""" + reset)


def print_welcome_banner():
    magenta = "\033[1;35m"
    yellow = "\033[1;33m"
    reset = "\033[0m"

    print(magenta + r"""
    __        __   _                           
    \ \      / /__| | ___ ___  _ __ ___   ___  
     \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
      \ V  V /  __/ | (_| (_) | | | | | |  __/   
       \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   
 """ + yellow + "W E L C O M E   T O   T H E   P A T I A L A   H O U S E" + reset)


def main():
    board = make_board(5, 5)
    character = make_character()
    print_welcome_banner()
    green = "\033[92m"
    purple = "\033[95m"
    reset = "\033[0m"

    print(
        green + "=====HELP=====" + "\n" +
        purple + "==============\n|| w:North  ||\n|| s:South  ||\n|| d:East   ||\n|| a:West   ||\n=============="
        + reset
    )

    game_loop(board, character)


if __name__ == '__main__':
    main()