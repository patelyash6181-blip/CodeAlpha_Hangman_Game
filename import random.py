import random
import os
import sys

# --- UI COLORS ---
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def clear_screen():
    """Clears terminal based on Operating System."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_game_data():
    """Returns a dictionary of technical terms and their hints."""
    return {
        'database': 'An organized collection of structured information.',
        'interface': 'A point where two systems, subjects, or organizations meet.',
        'framework': 'A basic structure underlying a system or concept.',
        'argument': 'A value passed to a function.',
        'frontend': 'The part of a website that the user interacts with.',
        'variable': 'A storage location paired with an associated symbolic name.',
        'boolean': 'A data type that has one of two possible values: true or false.',
        'callback': 'A function passed into another function as an argument.',
        'algorithm': 'A process or set of rules to be followed in calculations.',
        'recursion': 'The process of a function calling itself.'
    }

def draw_header():
    """Standard header for the game UI."""
    print(f"{Color.BOLD}{Color.CYAN}{'='*45}")
    print(f"{' '*7}HANGMAN: INTERNSHIP EDITION 2.0")
    print(f"{'='*45}{Color.END}\n")

def confirm_exit():
    """Asks the user for confirmation before closing the app."""
    print(f"\n{Color.BOLD}{Color.RED}EXIT REQUESTED{Color.END}")
    choice = input(f"{Color.YELLOW}Do you want to exit? (yes/no): {Color.END}").lower().strip()
    if choice in ['yes', 'y']:
        print(f"\n{Color.CYAN}Shutting down systems... Goodbye.{Color.END}")
        sys.exit()
    else:
        print(f"{Color.GREEN}Returning to menu...{Color.END}")
        import time
        time.sleep(1)
        return

def show_help():
    """Rules and Shortcuts screen."""
    clear_screen()
    draw_header()
    print(f"{Color.BOLD}GAME RULES:{Color.END}")
    print(f" * Guess the technical word one letter at a time.")
    print(f" * Each wrong guess removes 1 heart {Color.RED}♥{Color.END}.")
    print(f" * You lose when your hearts reach 0.")
    
    print(f"\n{Color.BOLD}PC KEYBOARD SHORTCUTS:{Color.END}")
    print(f" [{Color.GREEN}S{Color.END}] - Start New Session")
    print(f" [{Color.YELLOW}H{Color.END}] - Help & Rules")
    print(f" [{Color.RED}Q{Color.END}] - Quit / Exit System")
    print(f" [{Color.CYAN}R{Color.END}] - Restart (on Game Over screen)")
    
    input(f"\n{Color.CYAN}Press Enter to return to menu...{Color.END}")

def play_game():
    """The core gameplay loop."""
    data = get_game_data()
    secret_word = random.choice(list(data.keys())).lower()
    hint = data[secret_word]
    
    guessed_word = ["_"] * len(secret_word)
    used_letters = set()
    lives = 6
    heart_symbol = "♥"

    # Initial Reveal (Starting Letters)
    starting_pool = list(set(secret_word))
    num_to_reveal = min(2, len(starting_pool))
    starting_letters = random.sample(starting_pool, num_to_reveal)
    
    for char in starting_letters:
        used_letters.add(char)
        for i, letter in enumerate(secret_word):
            if letter == char:
                guessed_word[i] = char

    message = f"{Color.CYAN}Session started. Type a letter and press Enter.{Color.END}"

    while lives > 0 and "_" in guessed_word:
        clear_screen()
        draw_header()
        
        print(f"{Color.YELLOW}HINT:{Color.END} {hint}")
        
        # Heart Display
        current_hearts = f"{Color.RED}{heart_symbol * lives}{Color.END}"
        lost_hearts = f"{Color.END}{'.' * (6 - lives)}"
        print(f"{Color.CYAN}LIVES:{Color.END} {current_hearts}{lost_hearts} ({lives}/6)")
        print(f"{Color.CYAN}USED: {Color.END} {', '.join(sorted(list(used_letters)))}")
        
        print(f"\n{Color.BOLD}WORD:  {' '.join(guessed_word).upper()}{Color.END}\n")
        print(f">> {message}")

        user_input = input(f"\n{Color.BOLD}Guess [A-Z]:{Color.END} ").lower().strip()

        if len(user_input) != 1 or not user_input.isalpha():
            message = f"{Color.RED}ERROR: Invalid input. Enter one letter.{Color.END}"
            continue

        if user_input in used_letters:
            message = f"{Color.YELLOW}WARNING: '{user_input.upper()}' already tried.{Color.END}"
            continue

        used_letters.add(user_input)

        if user_input in secret_word:
            message = f"{Color.GREEN}SUCCESS: '{user_input.upper()}' is in the word.{Color.END}"
            for i, letter in enumerate(secret_word):
                if letter == user_input:
                    guessed_word[i] = user_input
        else:
            lives -= 1
            message = f"{Color.RED}FAILURE: '{user_input.upper()}' not found.{Color.END}"

    # Final Result Screen
    clear_screen()
    draw_header()
    if "_" not in guessed_word:
        print(f"{Color.GREEN}{Color.BOLD}   VICTORY: INTERNSHIP COMPLETED!{Color.END}")
        print(f"   The term was: {Color.BOLD}{secret_word.upper()}{Color.END}")
    else:
        print(f"{Color.RED}{Color.BOLD}   TERMINATED: SYSTEM FAILURE{Color.END}")
        print(f"   The correct term was: {Color.BOLD}{secret_word.upper()}{Color.END}")
    
    print(f"\n{'='*45}")
    
    choice = input(f"\n[{Color.GREEN}R{Color.END}]estart or [{Color.RED}M{Color.END}]enu?: ").lower().strip()
    if choice == 'r':
        play_game()
    else:
        return

def main_menu():
    """Initial landing screen with Shortcuts."""
    while True:
        clear_screen()
        draw_header()
        print(f"{Color.BOLD}MAIN MENU (PC SHORTCUTS){Color.END}")
        print(f"[{Color.GREEN}S{Color.END}] Start New Session")
        print(f"[{Color.YELLOW}H{Color.END}] View Help / Rules")
        print(f"[{Color.RED}Q{Color.END}] Quit System")
        
        # User input maps to shortcuts
        choice = input(f"\n{Color.BOLD}Input Shortcut >> {Color.END}").lower().strip()
        
        if choice == 's':
            play_game()
        elif choice == 'h':
            show_help()
        elif choice == 'q':
            confirm_exit()
        else:
            print(f"{Color.RED}Unknown command. Use S, H, or Q.{Color.END}")
            import time
            time.sleep(1)

# --- BOOT UP ---
if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Color.RED}System force-closed.{Color.END}")
        sys.exit()
