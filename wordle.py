# ictprg302_AT3
#
# Author: Ashton_Anderson
# Student ID: 20152010
#
# Course: ICTPRG302
# Lecturer: Rafael Avigad

import random

# Variables and Constants
DEBUG = False
target_words = "target_words.txt"
guess_words = "all_words.txt"

# Application Functions
def random_target_word(word_list):
    word_list_length = len(word_list)

    random_num = random.randint(0, word_list_length -1)

    return word_list[random_num]

def display_score(score, guess_word):
    score_output = ""
    word_output = ""

    for i in range (len(score)):
        if score[i] == 0:
            score_output += "-"
        if score[i] == 1:
            score_output += "?"
        if score[i] == 2:
            score_output += "X"
        score_output += " "
            
    for i in range (len(score)):
        word_output += guess_word[i]

        word_output += " "

    print(score_output)
    print(word_output)
            

#Score Guess Function
def score_guess(guess_word, target_word):
    """Determines the score of a users guess compared to the target
    Arguments
    ---------
    guess_word: The word that has been input by the user
    target_word: The randomly selected word from target_words.txt that the user is
    trying to guess

    Returns
    -------
    score_list: This is the returned list that determines the users score. 0 for an
    incorrect letter, 1 for a correct letter in the wrong position, 2 for a correct
    letter in the correct position

    Examples
    --------
    guess_word = hello
    target_word = world
    guess_score = 0,1,0,2,0

    guess_word = hello
    target_word = hello
    guess_score = 2,2,2,2,2"""

    target_list = list(target_word)
    guess_list=list(guess_word)

    score_list = [0] * len(target_list)


    for i in range(len(target_list)):
        if guess_list[i] == target_list[i]:
            score_list[i] = 2
            target_list[i] = None
            
    for i in range(len(target_list)):
        if score_list[i] == 0 and guess_list[i] in target_list:
            score_list[i] = 1
            target_list[target_list.index(guess_list[i])] = None
            

    return score_list


# Read File Into Word List Function
def read_words_into_list(filename):
    list_of_words = []

    with open(filename, 'r') as f:
        for line in f:
            list_of_words.append(line.strip())
        
    return list_of_words


# Display Greeting Function
def show_greeting():
    print("""
Welcome to
+===================================================+
|██╗0000██╗0██████╗0██████╗0██████╗0██╗00000███████╗|
|██║0000██║██╔═══██╗██╔══██╗██╔══██╗██║00000██╔════╝|
|██║0█╗0██║██║000██║██████╔╝██║00██║██║00000█████╗00|
|██║███╗██║██║000██║██╔══██╗██║00██║██║00000██╔══╝00|
|╚███╔███╔╝╚██████╔╝██║00██║██████╔╝███████╗███████╗|
|0╚══╝╚══╝00╚═════╝0╚═╝00╚═╝╚═════╝0╚══════╝╚══════╝|
+===================================================+
""")

    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's play!")
    return player_name


#Display Instructions Function
def show_instructions(player_name):
    show_instruction = input(f"Do you need the instructions {player_name}? ")
    if show_instruction.lower() in ('y', 'yes'):
        print(r"""
+===============================================================+
|  _                                        _                   |
| (_)           _                      _   (_)                  |
|  _ ____   ___| |_   ____ _   _  ____| |_  _  ___  ____   ___  |
| | |  _ \ /___)  _) / ___) | | |/ ___)  _)| |/ _ \|  _ \ /___) |
| | | | | |___ | |__| |   | |_| ( (___| |__| | |_| | | | |___ | |
| |_|_| |_(___/ \___)_|    \____|\____)\___)_|\___/|_| |_(___/  |
+===============================================================+
-You will be given 5 tries to guess a 5 letter word!
-For each try your guess will be scored!
-If a letter you guess is in the word and in the correct position you will get a X
-If a letter you guess is in the word but in the incorrect position you will get a ?
-If a letter you guess is not in the word you will get a -
-For example:
|------------------| |------------------------------|
|Target: H e l l o | |- = Incorrect                 |
| Guess: W o r l d | |? = Correct (Wrong Position)  |
|Score: (- ? - X -)| |X = Correct (Correct Position)|
|------------------| |------------------------------|
If you do not guess the word in 5 tries it's game over!
- Type --help at any time to see the instructions again.
Good Luck!""")
        input("Ready?\n")
    else:
        print("Okay!\n")

#Any Optional Additional Functions
def play_again(answer):
    if answer.lower() in ("y" , "yes"):
        return True
    else:
        return False

def validate_input(guess_word,guess_list):
    if len(guess_word) != 5:
        print("your guess must be 5 letters\n")
        return False

    if guess_word.lower() not in guess_list:
        print("Invalid word. Try again\n")
        return False

    return True
def avg_attempts_from_log(filename="Win_Log.txt"):
    attempts_list = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.split()
                if "attempts in parts":
                    idx = parts.index("attempt/s")
                    try:
                        attempts = int(parts[idx-1])
                        attempts_list.append(attempts)
                    except (ValueError, IndexError):
                        continue

            if attempts_list:
                avg_attempts = sum(attempts_list) / len(attempts_list)
                print(f"Average attempts per win: {avg_attempts}")
            else:
                print("No valid attempt data found in log.")

    except FileNotFoundError:
        print("log file not found")

#Play Game Function
def play_game():
    #play again y/n loop
    play_again_bool = True
    
    player_name = show_greeting()
    show_instructions(player_name)

    #main playagain loop
    while play_again_bool == True:

        target_list = read_words_into_list(target_words)
        target_word = random_target_word(target_list)

        guess_list = read_words_into_list(guess_words)

        max_attempts = 5
        attempts = 0


        while attempts < max_attempts:
            guess_word = input("Guess The Word: \n")

            # show instructions
            if guess_word == "--help":
                show_instructions(player_name)

            if not validate_input(guess_word,guess_list):
                continue

            print(target_word)
            attempts += 1

            #Last attempt warning
            if attempts == (max_attempts -1):
                print(f"Last attempt! Attempt Number: {attempts}/5")
            else:
                print(f"Attempt Number: {attempts}/5")

            #Display Score
            score_list = score_guess(guess_word, target_word)
            display_score(score_list, guess_word)
            print("\n")

            #If win
            if guess_word.lower() == target_word.lower():
                print(f"You guessed the word!!\n {target_word.upper()}")
                with open('Win_Log.txt','a') as f:
                    f.write(f"{player_name} won in {attempts} attempt/s with the word {target_word}\n")
                avg_attempts_from_log()
                break
        #Lose
        else:
            print(f"""Unlucky, the word was
      {target_word.upper()}\n""")
            
        #playagain input
        answer = input("Play Again? y/n: \n")
        play_again_bool = play_again(answer)

        #New word notif
        if play_again_bool == True:
            print("Generating new word...\n")
    #If end
    print("Thanks, For Playing!")
        

#Testing
def test_game():
    guess_word = "heelo"
    target_word = "heelo"
    guess_word = input ("Guess The Word: \n")

    score = score_guess(guess_word, target_word)
    display_score(score, guess_word)

    print("Score:", score, "Expected:", [2, 2, 2, 2, 2])
     
# Main Program
if DEBUG:
    test_game()
else:
    play_game()



