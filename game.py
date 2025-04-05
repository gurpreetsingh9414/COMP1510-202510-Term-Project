"""
Gurpreet Singh
A01405950
"""

import random


def make_board(rows, columns):
    """
        Generate a game board as a dictionary mapping coordinates to room descriptions.

        :param rows: number of rows in the board (int)
        :param columns: number of columns in the board (int)
        :precondition: rows and columns must be positive integers greater than 0
        :postcondition: dictionary where each (row, column) key is associated with a random location description
        :return: dict representing the game board

        >>> isinstance(make_board(3, 3), dict)
        True
        >>> len(make_board(2, 2)) == 4
        True
        """
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
    """
        Create and return a new player character with default stats and starting position.

        :postcondition: dictionary representing the character's starting state
        :return: dict with keys 'X', 'Y', 'HP', 'Max HP', 'Level', 'XP', and 'XP to next'

        >>> character = make_character()
        >>> isinstance(character, dict)
        True
        >>> character["Level"]
        1
        >>> character["HP"] == character["Max HP"]
        True
        >>> character["X"], character["Y"]
        (0, 0)
        """
    return {
        "X": 0,
        "Y": 0,
        "HP": 5,
        "Max HP": 5,
        "Level": 1,
        "XP": 0,
        "XP to next": 3,
    }


def describe_current_location(board, character):
    """
     Print the character's current position and the room description from the board.

     :param board: a dictionary representing the game board, with (x, y) tuples as keys and strings as descriptions
     :param character: a dictionary containing at least 'X' and 'Y' keys representing the character's position
     :precondition: board must contain the (X, Y) coordinate; character must have valid 'X' and 'Y' integer values
     :postcondition: prints the current coordinates and the associated room description to the console

     """

    loca_x, loca_y = character["X"], character["Y"]
    print(f"\nYou are at ({loca_x}, {loca_y}).")
    print("Location:", board[(loca_x, loca_y)])


def draw_map(character, rows=5, columns=5):
    """
     Display a color-coded grid map showing the player's current position and the final goal location.

    :param character: a dictionary containing at least 'X' and 'Y' keys representing the player's position
    :param rows: number of rows in the map (default is 5)
    :param columns: number of columns in the map (default is 5)
    :precondition: character must contain valid 'X' and 'Y' within bounds of rows and columns
    :postcondition: prints a color-coded map with the player position marked as [P] and the finish location as [F]

    """
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
    """
     Display the current status of the player, including position, health, level, and experience.

    :param character: a dictionary containing player attributes such as 'X', 'Y', 'HP', 'Level', etc.
    :precondition: character must be a dictionary with relevant keys and values
    :postcondition: prints the player's current stats in a formatted, color-coded manner
    """
    blue = "\033[94m"
    reset = "\033[0m"

    print(blue + "\n=== Player Status ===" + reset)
    for key, value in character.items():
        print(f"{key}: {value}")
    print(blue + "\n=====================" + reset)


def get_direction():
    """
     Prompt the user to input a direction and return the corresponding direction name.

     :precondition: user must enter one of the valid direction keys: 'w', 's', 'd', or 'a'
     :postcondition: a valid direction string ('north', 'south', 'east', or 'west')
     :return: str representing the chosen direction

     """
    directions = {"w": "north", "s": "south", "d": "east", "a": "west"}
    while True:
        print("\nMove:")
        print("w. North\ns. South\nd. East\n. West")
        choice = input("Enter: ")
        if choice in directions:
            return directions[choice]
        print("Invalid. Try again.")


def validate_move(character, direction, board):
    """
        Check if a movement in the specified direction is valid based on the board boundaries.

        :param character: a dictionary containing the current 'X' and 'Y' position of the player
        :param direction: a string direction ('north', 'south', 'east', or 'west')
        :param board: a dictionary representing the game board with coordinate tuples as keys
        :precondition: character must contain valid 'X' and 'Y' keys; direction must be a valid string; board must include all accessible tiles
        :postcondition:  True if the move is within the bounds of the board; otherwise False
        :return: bool

        >>> boards = {(0, 0): "Start", (0, 1): "Right"}
        >>> characters = {"X": 0, "Y": 0}
        >>> validate_move(characters, "east", boards)
        True
        >>> validate_move(characters, "north", boards)
        False
        """
    x, y = character["X"], character["Y"]
    if direction == "north": return (x - 1, y) in board
    if direction == "south": return (x + 1, y) in board
    if direction == "east": return (x, y + 1) in board
    if direction == "west": return (x, y - 1) in board
    return False


def move_character(character, direction):
    """
        Update the character's position by modifying their coordinates based on the given direction.

        :param character: a dictionary containing 'X' and 'Y' keys representing the player's current position
        :param direction: a string direction ('north', 'south', 'east', or 'west')
        :precondition: character must have valid 'X' and 'Y' integer values; direction must be a valid string
        :postcondition: the character's position is updated in-place to reflect the chosen direction

        >>> char = {"X": 1, "Y": 1}
        >>> move_character(char, "north")
        >>> char["X"], char["Y"]
        (0, 1)
        >>> move_character(char, "east")
        >>> char["X"], char["Y"]
        (0, 2)
        """
    if direction == "north":
        character["X"] -= 1
    elif direction == "south":
        character["X"] += 1
    elif direction == "east":
        character["Y"] += 1
    elif direction == "west":
        character["Y"] -= 1


def is_alive(character):
    """
        Check if the character is still alive based on their HP.

        :param character: a dictionary containing the 'HP' (hit points) key
        :precondition: character must include an 'HP' key with an integer value
        :postcondition: evaluates the character's HP to determine if they are alive
        :return: True if HP is greater than 0, otherwise False

        >>> is_alive({"HP": 3})
        True
        >>> is_alive({"HP": 0})
        False
        >>> is_alive({"HP": -2})
        False
        """
    return character["HP"] > 0


def level_up(character):
    """
        Increase the character's level and update stats if the character is below the max level cap (3).

        :param character: a dictionary representing the player with keys 'Level', 'XP', 'XP to next', 'HP', 'Max HP', 'X', 'Y'
        :precondition: character must have all necessary keys with valid values (e.g., Level is an int)
        :postcondition: character's Level, HP, Max HP, XP to next, and position are updated if not already at max level

        >>> char = {'Level': 1, 'XP': 5, 'XP to next': 3, 'Max HP': 5, 'HP': 3, 'X': 2, 'Y': 2}
        >>> level_up(char)
        <BLANKLINE>
        🎉 Leveled up to Level 2!
        Max HP is now 7.
        You are sent back to the start.
        >>> char['Level']
        2
        >>> char['HP'] == char['Max HP'] == 7 and char['X'] == 0 and char['Y'] == 0
        True
        """
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
    """
        Increase the character's XP and level them up if they have enough XP and are below max level.

        :param character: a dictionary representing the player, with keys including 'XP', 'Level', and 'XP to next'
        :param amount: an integer value of XP to add
        :precondition: character must include keys 'XP', 'Level', 'XP to next'; amount must be a non-negative integer
        :postcondition: character's XP increases by the amount; if XP exceeds threshold, character levels up (unless already level 3)

        >>> char = {"XP": 2, "Level": 1, "XP to next": 3, "HP": 5, "Max HP": 5, "X": 0, "Y": 0}
        >>> gain_xp(char, 2)
        You gained 2 XP!
        <BLANKLINE>
        🎉 Leveled up to Level 2!
        Max HP is now 7.
        You are sent back to the start.
        >>> char["Level"]
        2
        >>> char["XP"]
        0
        """
    character["XP"] += amount
    print(f"You gained {amount} XP!")
    if character["Level"] < 3:
        while character["XP"] >= character["XP to next"]:
            level_up(character)


def check_for_foe(character):
    """
    Determine whether the player encounters a foe based on their level.

    :param character: a dictionary containing the player's 'Level'
    :precondition: character must include a 'Level' key with an integer value (1–3)
    :postcondition: randomly returns True with a chance based on level (25% if < 3, 33% if 3)
    :return: true if a foe appears; False otherwise
    """
    chance = 0.30 if character["Level"] < 3 else 0.35
    return random.random() < chance


def number_guessing_game(character):
    """
        Launch a number guessing mini-game where the player guesses a number between 1 and 5.

        :param character: a dictionary representing the player with at least 'HP' and 'XP' keys
        :precondition: character must include 'HP', 'XP', 'Level', and 'XP to next'
        :postcondition: if the player guesses correctly, they gain 2 XP; otherwise, they lose 1 HP
                        invalid inputs are also penalized with -1 HP

        """
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
    """
    Launch a rock-paper-scissors game between the player and an enemy.

    :param character: a dictionary representing the player with keys 'HP', 'XP', etc.
    :precondition: character must include 'HP' and 'XP' keys; user must input 'rock', 'paper', or 'scissors'
    :postcondition: If input is invalid: player loses 1 HP
    :postcondition: If it's a tie: player escapes without gain or loss
    :postcondition: If player wins: gain 2 XP
    :postcondition: If player loses: lose 1 HP
    """
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
    """
    Launch a riddle mini-game where the player must answer a random riddle.

    :parameters: a dictionary containing at least 'HP' and 'XP' keys
    :precondition: character must include valid 'HP', 'XP', and 'Level' fields
    :postcondition: If the player's answer matches the correct answer, they gain 3 XP.
    :postcondition: If the player's answer is incorrect, they lose 1 HP.
    """
    riddles = [
        ("What has keys but can't open locks?", "keyboard"),
        ("What gets wetter as it dries?", "towel"),
        ("What has hands but can't clap?", "clock"),
        ("What runs but never walks?", "water"),
        ("I speak without a mouth and hear without ears. What am I?", "echo"),
        ("What has a head and tail, but no body?", "coin"),
        ("What breaks when you say it?", "silence"),
        ("What goes up but never comes down", "age")
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
    """
    The main game loop that drives gameplay until the player either wins or runs out of HP.

    :param: a dictionary representing the game board with coordinate tuples as keys and room descriptions as values
    :param character: a dictionary representing the player's state, including position, HP, XP, and level
    :precondition: board must be properly initialized; character must have required keys and valid values
    :postcondition: Continuously handles movement, encounters, XP gain, and level-ups
    :postcondition: Ends when the character dies (HP <= 0) or wins the game (XP >= 21 or reaches (4, 4) at level 3)
    """
    while is_alive(character):
        if character["Level"] == 3:
            if character["XP"] >= 21:
                print("\n👑 YOU WIN! Your wisdom and strength have surpassed all expectations!")
                print_game_over_banner()
                return
            elif (character["X"], character["Y"]) == (4, 4):
                print("\n👑 YOU WIN! You have conquered the final chamber of Patiala House!")
                print_game_over_banner()
                return
        describe_current_location(board, character)
        draw_map(character)
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
            if (character["X"], character["Y"]) == (4, 4):
                if character["Level"] < 3:
                    print("You feel stronger after reaching the end of the maze.")
                    gain_xp(character, 3)
        else:
            print("You can't go that way!")

    print("\n💀 Game Over. You ran out of HP.")


def print_game_over_banner():
    """
    Print a stylized 'Game Over' banner in green text.

    :postcondition: Outputs ASCII art to the terminal indicating that the game has ended
    """
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
    """
    Print a colorful ASCII welcome banner introducing the game.

    :postcondition: Outputs a welcome message with stylized ASCII art and colors

    """
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
    """
        Drive the game by initializing the board, character, and launching the main game loop.
    """

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