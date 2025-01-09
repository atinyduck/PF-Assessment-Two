import random as rnd
import time, sys 


# ANSI Codes to allow for coloured text
class OutColours: 
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

# String constants for reuseablilty 
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


def clear_screen():
    """Function to clear the screen (only works on some terminals)"""
    print("\033c", end="") # Clear the screen
 

#region File Control


def create_file(file_name: str) -> bool:
    """Creates an empty file if it does not exist
    
    Args:
        file_name (str): The name of the file being accessed 

    Returns:
        bool: Returns if the file was successfully created
    """
    # Try to create the, if not output suitable error message.
    try:
        with open(file_name, "w") as file:
            pass
        return True
    
    except Exception as e:
        print(f"Failed to create file: {e}")
        return False
        
        
def ensure_file_exists(file_name: str) -> None:
    """Ensures the presence of a file before it is accessed

    Args:
        file_name (str): The name of the file being accessed 
    """
    # Try to open the file, if not create one.
    try:
        with open(file_name, "r"):
            pass
    
    except FileNotFoundError:
        if not create_file(file_name): # If the file cant be created exit process.
            print("Unable to create this file. Exiting.")
            sys.exit(1)


def append_to_file(save_txt: str, file_name: str):
    """Appends data into a file of choice.
    
    Args:
        save_txt (str): The data wanting to be added to the file.
        file_name (str): The name of the file.
    """
    # Make sure there is a file to access
    ensure_file_exists(file_name)
    
    # Try to open the file and write the contents to it, if not output suitable error.
    try:
        with open(file_name, "a") as file:
            file.write(save_txt + "\n")
            file.close()
    
    except Exception as e:
        print("Failed to save to file: {e}")


def read_from_file(file_name: str):
    """Read all data from a file.

    Args:
        file_name (str): The name of the file.

    Returns:
        _type_: The contents of the file.
    """
    # Make sure there is a file to access
    ensure_file_exists(file_name)
    
    # Try to open the file and read the contents, if failed return nothing.
    try:
        with open(file_name, "r") as file:
            return file.readlines()
        
    except Exception as e:
        print(f"Failed to read from file: {e}")
        return []
        

#endregion


#region Get Data Functions


def get_best_time(player_name: str) -> bool:
    """Finds the fastest times in the 'winners.txt' file and outputs them.

    Args:
        player_name (str): The player's name or alias.
    """
    
    file_txt = read_from_file("winners.txt")
    
    # Declare variables
    fastest_time: int = float('inf') # Use of infinity for "no limit" placeholder
    fastest_name: str = ""
    player_time: int = float('inf')
    
    if file_txt: # Checks if the files containts any data
        for line in file_txt:
            line_contents: list = line.strip().split(',')
            
            try:
                # Get the name and time values
                line_name = line_contents[0].strip()
                line_val = float(line_contents[1].strip())
                
                # Check if the lins matches the player's name and update their fastest time
                if line_name.lower() == player_name.lower() and line_val < player_time:
                    player_time = line_val
                
                # Update the fastest overall time
                if line_val < fastest_time:
                    fastest_time = line_val
                    fastest_name = line_name
                    
            except (IndexError, ValueError) as e:
                print(f"Error processing line '{line.strip()}': {e}")
        
        # Prepare outputs
        fastest_time_str = (
            f"\nThe fastest time overall was made by {fastest_name} at {fastest_time:.2f}s!"
            if fastest_time != float('inf')
            else "\nNo one has set a time just yet!"
        )
        
        players_time_str = (
            f"{player_name} the fastest time you achieved was {player_time:.2f}s."
            if player_time != float('inf')
            else "\nYou haven't set a time just yet!"
            
        )
        
        return f"{fastest_time_str}\n{players_time_str}"
    
    # If nothing output that there are no times 
    else:
        return("No times recorded yet!")
   
    
def get_dictionary(source: list = read_from_file("dictionary.txt")) -> list:
    """Function to create a dictionary from given words.

    Args:
        source (list, optional): The source list to read data from. Defaults to read_from_file("dictionary.txt").

    Returns:
        list: The dictionary of the words
    """
    # Get dictionary
    dictionary: list = list()
    
    # Go through each line in the list and 
    for word in source:
        dictionary.append(word.strip().lower())  
    
    return dictionary
    
    
def get_guess(answer: str, start_time: float, is_hardmode: bool, correct_letters: list) -> str:
    """Returns the user's guess if it is valid

    Args:
        answer (str): The hidden word to guess.

    Returns:
        str: The guess made by the user
    """
    dictionary = get_dictionary()
    
    while True: # Loop to get guess
        print("Enter your guess or [Q] to abandon the game:")
        guessed_word = input(" :: ").strip().lower()
        
        if guessed_word == "q" or guessed_word == "h": # If it is to quit.
            return guessed_word
        
        if len(guessed_word) != len(answer): # If the inputs length is incorrect.
            print(f"Your guess must be {len(answer)} letters long.")
            continue
        
        if is_hardmode and len(correct_letters) != 0: # If its hardmode and there have been correct guesses.
            
            # Counter to store the amount of correct letters used by the user.
            count: int = 0
            
            for char in guessed_word.upper():
                if char in correct_letters: # Increase the count if the player uses a correct letter.
                    count += 1
                    
            if count != len(correct_letters): # If the amount of correct letters is not equal to used ones.
                return "@"
            
        if guessed_word not in dictionary: # If the guessed word was not in the dictionary.
            return "!"
        
        if (time.time() - start_time) >= 30: # If the turn is longer than 30 seconds.
            return "#"
        
        return guessed_word


def get_clue(answer: str, guess: str) -> str:
    """Generates the clue for the user and returns the line

    Args:
        answer (str): The hidden word to guess.
        guess (str): The user's input.

    Returns:
        str: The clue for the user.
    """
    colour_clue: list = [""] * len(guess)
    txt_clue: list = [""] * len(guess)
    answer_chars: list = list(answer)
    
    # First pass: checks for items in correct positions
    for i, char in enumerate(guess):
        if char == answer[i]:
            colour_clue[i] = OutColours.GREEN + char.upper() + OutColours.ENDC
            txt_clue[i] = "*"
            answer_chars[i] = None # Mark as used
            
    # Second pass: Correct letters in wrong position
    for i, char in enumerate(guess):
        if txt_clue[i] == "": # If the character was not a match in the first pass
            if char in answer_chars:
                answer_index = answer_chars.index(char) 
                colour_clue[i] = OutColours.YELLOW + char.upper() + OutColours.ENDC
                txt_clue[i] = ("+")
                answer_chars[answer_index] = None # Mark as used
                    
            else: # If the charcter was found, mark as incorrect
                colour_clue[i] = OutColours.RED + char.upper() + OutColours.ENDC
                txt_clue[i] = "_"
            
    return " | ".join(colour_clue) + "\n\t" + " | ".join(txt_clue)
    

def get_hint(answer: str, found_letters: list) -> str:
    """Function to return a hint to the player when asked for.

    Args:
        answer (str): The current hidden word.
        found_letters (list): The current letters found by the player.

    Returns:
        str: The hint, a random letter in the answer.
    """
    # Split the answer into a list
    answer_list: list = list(answer)
    
    # Choose the random letter
    rnd_choice: str = rnd.choice(answer_list)
    
    # Return the hint unless it is already been found by the player
    return (
        rnd_choice 
        if rnd_choice not in found_letters 
        else get_hint(answer, found_letters)
    )
    


def get_used_letters(past_guesses: list) -> list:
    """This function returns all used letters in previous guesses

    Args:
        past_guesses (list): The previous guesses by the player

    Returns:
        list: The list of all used letters, without duplicates
    """
    used_letters: list = list()
    
    # Find all unique used letters
    for guess in past_guesses:
        for char in guess:
            if str(char).upper() not in used_letters:
                used_letters.append(str(char).upper())
    
    return used_letters


def get_word_length() -> int:
    """Function to get the player's prefered word length
    
    Returns:
        int: The player's choice.
    """
    clear_screen() 

    # Output the menu for the player.
    print(f"""
    {Strings.TITLE}
You can choose to play with 
 :: [4] Four letters
 :: [5] Five letters
 :: [6] Six letters

Please enter your choice,""")

    choice: str = input(" :: ").strip()
    if choice in ['4', '5', '6']: # If they enter a valid choice return it.
        return int(choice)
    
    else: # If not recall the function.
        return get_word_length()


def get_hardmode() -> bool:
    """Function to get if the player wants hard mode.
    
    Returns:
        bool: The player's choice.
    """
    clear_screen() 
    
    # Output if the description of hardmode and choice.
    print(f"""
    {Strings.TITLE}     
You can also play in hardmode, this means your guesses must include letters you've found.

Would you like to play in hardmode? 
 :: [Y/N]
          """)
    
    choice: str = input(" :: ").strip().upper()
    if choice in ['Y', 'N']: # If they enter a valid choice return if its Yes or No (True or False).
        return choice == "Y"
    
    else: # If not recall the function.
        return get_hardmode()


def get_random_word(word_length: int) -> str:
    """
    Returns a word chosen from the passed list that is the passed word length.

    Args:
        words_list (list, optional): The list of words to chose from. Defaults to load_words().
        word_length (int, optional): The length of the desired word. Defaults to 5.

    Returns:
        str: The chosen word.
    """
    dictionary = get_dictionary()
    
    # Make a list of words the correct length.
    valid_words = [word for word in dictionary if len(word) == word_length]
    
    if not valid_words: # If it failed to do so exit the process.
        print(f"There are no words of word length {word_length} in \"dictionary.txt\"")
        sys.exit(1)
    
    # Return the choice from valid words.
    return rnd.choice(valid_words)
     

def get_name() -> str:
    """Get the user's name or alias

    Returns:
        str: The players chosen name.
    """
    clear_screen()
    
    # Output the intro text
    print(Strings.TITLE, Strings.INTRO)
    
    # Get the name input
    name_input: str = input(" :: ")
    
    if name_input != "": # If there is a name present return the input
        return name_input.strip().capitalize()
    
    else: # If not recall the function
        return get_name()


def get_menu_input(name: str) -> str:
    """Get the user's name or alias
    
    Args:
        name (str): The player's name or alias.
    
    Returns:
        str: The player's menu input.
    """
        
    clear_screen()
    
    # Output the menu for the player
    print(Strings.TITLE, f"""
Welcome {name}! Please choose from one of the following:
 :: [1] New Game
 :: [2] Check High Score
 :: [Q] Quit

Please enter an option,
    """)
    
    # Return the users choice
    menu_input: str = input(" :: ").strip().upper()
    if menu_input in ['1', '2', 'Q']: # If they enter a valid input return it
        return menu_input
    
    else: # If not recall the function
        return get_menu_input(name)
    
    
#endregion


#region Game Functions


def display_game(clue: str, lives: int, used_letters: list, answer: str, is_hardmode: bool):
    """Displays the current game state.
    
    Args:
        clue (str): The clue generated.
        lives (int): The lives the user has left.
    """
    
    # Find the incorrect letters guessed.
    incorrect_letters: list = list()
    
    for char in used_letters:
        if char not in answer.upper():
            incorrect_letters.append(char)
    
    incorrect_letters_str: str = (
        ", ".join(incorrect_letters) if len(incorrect_letters) != 0 else ""
    ).upper()
    
    # String output for hardmode if it is current active.
    hardmode_str = (
        "\nHardmode! Remember you must guess with letters you've found.\n"
        if is_hardmode else ""
    )
    
    # Output the the information about the game.
    print(f"""
{Strings.TITLE}
You have 30 seconds to enter a guess!
{hardmode_str}
A guess not in the dictionary will remove a life.\n
    * = Letter is correct and in the correct position (green).
    + = Letter is correct but in the wrong position (yellow).
    _ = Letter is not present in the word (red).\n
You can spend a life to get a hint only once! [H]\n
You have {lives} remaining\n
{clue}
{incorrect_letters_str}
        """)


def main_menu():
    """Function to control the inputs for the main menu.
    """
    # Output the intro and get the player's name.
    player_name = get_name()
    
    # Menu loop
    while True:
        
        # Output the menu and get input.
        menu_input = get_menu_input(player_name)
        
        match menu_input:
            case "1": # Create a new game.
                game_loop(player_name)
            
            case "2": # Get and display the best times.
                best_time_str = get_best_time(player_name)
                
                print(best_time_str)
                
                # Wait for the user to continue.
                input("\nPress enter to continue. . .")
            
            case "Q": # Quit the program.
                print("Thank you for playing!")
                sys.exit(0)

            case _: # Handle invalid input.
                print("Invalid input, please enter one of the options.")
                input("\nPress enter to continue. . .")


# Function to handle the main game loop.
def game_loop(player_name: str):
    """Function to control the basic game loop.

    Args:
        player_name (str): The player's name or alias.
    """
    clear_screen()
    
    # Get the players prefered world length.
    word_length: int = get_word_length()
    
    # Get if the player wants hardmode.
    hardmode: bool = get_hardmode()
        
    # Initiate variables.
    answer: str = get_random_word(word_length)
    past_guesses: list = []
    correct_letters: list = list()
    lives: int = 6
    clue: str = ""
    
    # Start timer.
    start_time: time = time.time()
    
    # Main game loop.
    while lives > 0:
        
        clear_screen() 
        
        used_letters: list = get_used_letters(past_guesses)
        
        # Find correct letters.
        for char in answer.upper():
            if char in used_letters and char not in correct_letters:
                correct_letters.append(char.upper())
        
        display_game(clue, lives, used_letters, answer, hardmode)
        
        # Get the guess from the user.
        turn_start = time.time()
        guess = get_guess(answer, turn_start, hardmode, correct_letters)  
        
        if guess.upper() == "Q": # If the user wants to quit.
            print("You quit the game!")
            break
                
        if guess.upper() == "H": # If the user wants a hint.
            hint: str = get_hint(answer, correct_letters)
            print(f"\nYour hint is {hint.upper()}!")
            lives -= 1
            input("\nPress enter to continue. . .")
            continue        
        
        if guess == "@": # Error code for hardmode rules failed to be followed.
            print("\nInvalid guess. Please guess using all letters you've found!")
            lives -= 1
            input("\nPress enter to continue. . .")
            continue
                
        if guess == "!": # Error code for invalid world.
            print("\nInvalid guess. Please enter a valid word from the dictionary.")
            lives -= 1
            input("\nPress enter to continue. . .")
            continue
            
        if guess == "#": # Error code for taking too long to guess.
            print("\nToo slow! remember guess within 30 seconds.")
            lives -= 1
            input("\nPress enter to continue. . .")
            continue
                        
        if guess == answer: # If its the correct guess.
            end_game(player_name, start_time)
            return
                    
        # Add a record of the guess.
        past_guesses.append(guess)    
        
        clue = ""
        
        # Generate clue output from previous guesses.
        for word in past_guesses:
            clue += "\t" + get_clue(answer, word) + "\n"
        
        # Reduces the guesses by 1.
        lives -= 1
    
    # Player has failed to guess.
    print(f"Game over! The correct word was: {answer}")
    input("\nPress enter to continue. . .")



# Function for ending the game and saving the time.
def end_game(player_name: str, start_time: float):
    """Function to end the game.
    
    Args:
        player_name (str): The player's name or alias.
    
    """
    # Find the time it took to guess the word.
    end_time = time.time()
    final_time = end_time - start_time
    
    # Output the completion message.
    print(f"""
Congratulations {player_name.capitalize()} you guessed the word!
You completed the game in {final_time:.2f} seconds.
    """)
    
    # Saved as {name},{time}.
    save_txt: str = f"{player_name.capitalize()},{final_time}"
    
    # Save the values to the file.
    append_to_file(save_txt, "winners.txt")
    
    input("\nPress enter to continue...")

    
#endregion

# Run process from the main menu.
if __name__ == "__main__":
    main_menu()