import random as rnd
import time 
import sys

# ANSI Codes to allow for coloured text
class OutColours: 
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

class Strings:
    TITLE = """
==============================
          Not Wordle
==============================
"""
    INTRO = """
Welcome! 

You have 6 guesses to guess what the word is.
Each guess will provide feedback:
    * = Letter is correct and in the correct position (green).
    + = Letter is correct but in the wrong position (yellow).
    _ = Letter is not present in the word (red).

What should we call you?
"""

# Function to save the results compared to the players name
def save_result(name: str, time: float):
    
    # {name},{time}
    save_txt: str = f"{name.capitalize()},{time}"

    file = open("game_saves.txt", "a")
    
    file.write(save_txt + "\n")
    file.close()
    

# Function to display the fastest solve times 
def display_best(name: str):
    highest_score: str = ""
    players_best: str = ""
    
    file = open("game_saves.txt", "r")
    
    _highest_score: int = 0
    _highest_name: str = ""
    _player_high: int = 0
    
    if len(file) != 0:
        # Find highest scores
        for line in file:
            line_contents: list = line.split(',')
            
            try:
                line_name = line_contents[0].strip()
                line_val = float(line_contents[1].strip())
            
                if line_name.upper() == name.upper() and line_val > _player_high:
                    _player_high = line_val
                
                if line_val > _highest_score:
                    _highest_score =  line_val
                    _highest_name = line_name
                    
            except Exception as e:
                print(f"Error caclulating highest values: {e}")
        
        highest_score = f"""
The fastest time overall was made by {_highest_name} at {"{:.2f}".format(_highest_score)}s!
    """
    
        players_best = f"""
{name} the fastest time you achieved was {"{:.2f}".format(_player_high)}s.
    """
        print(highest_score, players_best)
       
    else:
        print("No hight scores set just yet!")
    
    print("\nPress enter to continue. . .")
    input()
        

# Function to load words from the dictionary.txt file into a list
def load_words(file_path: str = "dictionary.txt") -> list:
    """
    Returns a list of all the contents of a passed file, defaulting to dictionary.txt

    Args:
        file_name (str, optional): The chosen file to read from. Defaults to "dictionary.txt".

    Returns:
        list: The list of lines from the passed file.
    """
    words_list = []
    
    try:
        with open(file_path) as file:
            # Read each line in the file
            for line in file:
                words_list.append(line.strip().lower())
                
    # Catch if the file could not be found
    except FileNotFoundError:
        print(f"File with name {file_path} could not be found")
        sys.exit(1)
    
    # Returns the list of lines
    return words_list


# Function to select a random word of the specified length from the words_list
def select_random_word(word_length: int, words_list: list = load_words()):
    """
    Returns a word chosen from the passed list that is the passed word length.

    Args:
        words_list (list, optional): The list of words to chose from. Defaults to load_words().
        word_length (int, optional): The length of the desired word. Defaults to 5.

    Returns:
        str: The chosen word.
    """
    
    valid_words = [word for word in words_list if len(word) == word_length]
    if not valid_words:
        print(f"There are no words of word length {word_length} in words_list")
        sys.exit(1)
    
    return rnd.choice(valid_words)
     
           
# Function to get the user's guess and ensure it is valid
def get_guess(answer: str, dictionary: list = load_words()) -> str:
    
    while True:
        print("Enter your guess or [Q] to abandon the game:")
        guessed_word = input(" :: ").strip().lower()
        
        if len(guessed_word) != len(answer):
            print(f"Your guess must be {len(answer)} letters long.")
            continue
        
        if guessed_word not in dictionary:
            print("Invalid guess. Please enter a valid word from the dictionary.")
            continue
        
        return guessed_word


# Function to provide feedback on the guess (clue generation)
def provide_clue(answer: str, guess: str) -> str:
    
    colour_clue: list = []
    txt_clue: list = []
    answer_chars: list = list(answer)
    
    for i, char in enumerate(guess):
        # Correct letter in right position
        if char == answer_chars[i]:
            colour_clue.append(OutColours.GREEN + char.upper() + OutColours.ENDC)
            txt_clue.append("*")
            answer_chars[i] = None
            
        # Correct letter in wrong position
        elif char in answer_chars:
            colour_clue.append(OutColours.YELLOW + char.upper() + OutColours.ENDC)
            txt_clue.append("+")
            answer_chars[answer_chars.index(char)] = None 
            
        # Wrong letter
        else:
            colour_clue.append(OutColours.RED + char.upper() + OutColours.ENDC)
            txt_clue.append("_")
            
    return " | ".join(colour_clue) + "\n\t" + " | ".join(txt_clue)


# Function to handle the player's turn. It can return if the guess was correct, the clue and previous guesses
def handle_turn(answer: str, dictionary: list = load_words(), past_guesses: list = list(), guess: str = None):
    pass
    
    
# Function to display the game result (win/loss)
def display_result(is_winner, answer: str = None):
    pass  # replace pass with your code


# Function to handle the player's decision to give up
def give_up(answer: str = None):
    """
    Displays the correct answer and exits the game.

    Args:
        answer (str): The correct word.
    """
    print(f"You gave up! The correct answer was: {answer.capitalize()}")


# Function to display the game state
def display_game(clue: str, lives: str):
    
    game_str = f"""
{Strings.TITLE}
    * = Letter is correct and in the correct position (green).
    + = Letter is correct but in the wrong position (yellow).
    _ = Letter is not present in the word (red).
    
You have {lives} remaining\n
{clue}        
        """
    print(game_str)

# Main menu 
def main_menu():
        
    print("\033c", end="") # Clear the screen
    
    # Output the intro text
    print(Strings.TITLE, Strings.INTRO)
    
    name_input: str = input(" :: ")
    name: str = name_input.strip().capitalize()
    
    print("\033c", end="") # Clear the screen only works on some terminals

    menu_str: str = f"""
Welcome {name}! Please choose from one of the following:
 :: [1] New Game
 :: [2] Check High Score
 :: [Q] Quit

Please enter an option,
    """
    
    # Menu loop
    while True:
        
        print("\033c", end="") # Clear the screen only works on some terminals
        
        print(Strings.TITLE, menu_str)
        
        menu_input: str = input(" :: ").strip().upper()
        
        match menu_input:
            case "1":
                new_game(name)
            
            case "2":
                display_best(name)
            
            case "Q":
                print("Thank you for playing!")
                sys.exit(0)

    
# Function to handle the main game loop
def new_game(name: str):
    
    print("\033c", end="") # Clear the screen only works on some terminals

    world_len_str = f"""
{Strings.TITLE}
{name} you can choose to play with 
 :: [4] Four letters
 :: [5] Five letters
 :: [6] Six letters

Please enter your choice,"""

    word_len: int = 5 # Defualts to 5
    
    # Get the desired word length
    while True:
    # Loops until a valid input has been made
        print("\033c", end="") 
        print(world_len_str)
    
        len_in: str = input(" :: ")
    
        if len_in in ['4', '5', '6']:
            word_len: int = int(len_in)
            break
        
        else:
            print("Please entera valid option, 4, 5 or 6")
            
    answer: str = select_random_word(word_len)
    past_guesses: list = []
    lives: int = 6
    clue: str = ""
    
    # Start timer
    start_time: time = time.time()
    
    while lives > 0:
        
        print("\033c", end="") # Clear the screen only works on some terminals
        
        display_game(clue, lives)
        
        clue = ""
        guess = get_guess(answer)
        past_guesses.append(guess)      
        
        if guess.upper() == "Q":
            break
        
        if guess == answer:
            end_time = time.time()
            final_time = end_time - start_time
            
            win_str = f"""
Congratulations you guessed the word!
You completed the game in {"{:.2f}".format(final_time)}.
            """
            
            save_result(name, final_time)
            print(win_str)
            print("\nPress enter to continue. . .")
            input()
            return
        
        for word in past_guesses:
            clue += "\t" + provide_clue(answer, word) + "\n"
        
        
        lives -= 1
        
    print(f"Game over! The correct word was: {answer}")
    print("\nPress enter to continue. . .")
    input()
    
 
    
    
    
if __name__ == "__main__":
    main_menu()