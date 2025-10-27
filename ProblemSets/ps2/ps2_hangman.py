import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "ProblemSets/ps2/words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    secr = secret_word[:]
    for i in letters_guessed:
        if i in secr:
            secr = secr.replace(i,"")
    return len(secr) ==0
  

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    output = secret_word[:]
    for char in output:
        if char not in letters_guessed:
            output = output.replace(char, "*")
    return output        
    


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # get all letters
    available_letters = string.ascii_lowercase
    for i in letters_guessed:
        # remove letters that guessed
        available_letters = available_letters.replace(i, "")
    return available_letters
    

def helper_letter(secret_word, available_letters):
    """
    secret_word: string, the lowercase word the user is guessing
    available_letters : string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    returns :  chooese a letter that are not guessed and revelaed yet
    """
    intersect_letters = []
    for i in secret_word:
        for j in available_letters:
            if i ==j:
                intersect_letters.append(i)
    return random.choice(intersect_letters)
    



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("--------------")
    # set total guess 
    total_guess = 10
    # unique letters in secret word
    unq_secret_letter = []
    for i in secret_word:
        if i not in unq_secret_letter:
            unq_secret_letter.append(i)
    # unique guessed letters from user 
    guessed_letters = []
    while total_guess > 0:
        # print left guessed
        print(f"You currently have {total_guess} guesses left.")
        # print available letters
        print(f"Available letters: {get_available_letters(guessed_letters)}")
        # take input from user
        char = str(input("Please guess a letter: ")).lower()
        # check if help is active
        if (with_help) and (char == "!") and (total_guess >=3):
            revealed_letter = helper_letter(secret_word, get_available_letters(guessed_letters))
            guessed_letters.append(revealed_letter)
            get_word_progress(secret_word, revealed_letter)
            print(f"Letter revealed: {revealed_letter} \n{get_word_progress(secret_word, guessed_letters)}")
            total_guess -= 3
        elif (with_help) and (char == "!") and (total_guess < 3):
            print("You do not have enough guesses!") 
        else:
            # check if the input is valid
            if (char not in string.ascii_letters and char != "!") or (len(char) != 1):
                print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, guessed_letters)}")
            # check if the user have already guessed
            elif char in guessed_letters:
                print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, guessed_letters)}")
            else:
                # append guessed letter to list
                guessed_letters.append(char)
                # check if the guess is correct 
                if char in secret_word:
                    print(f"Letter revealed: {char} \n{get_word_progress(secret_word, guessed_letters)}")
                elif (char not in secret_word) and (char in "aeiuo"):
                    print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, guessed_letters)}")
                    total_guess -= 2
                elif (char not in secret_word) and (char in "bcdfghjklmnpqrstvwxyz"):
                    print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, guessed_letters)}")
                    total_guess -= 1
        # check if the user won
        if has_player_won(secret_word, guessed_letters):
            print(f"Good guess: {secret_word}\n--------------\nCongratulations, you won!\nYour total score for this game is: {(total_guess+4*len(unq_secret_letter))+ (3 * len(secret_word))}")
            break
        print("--------------")
        # check if there is guess left
        if total_guess == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break
            
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)