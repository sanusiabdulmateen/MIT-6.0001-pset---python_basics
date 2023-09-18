# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    length = len(secret_word)
    count = 0
    guessed = False
    for letter in secret_word:
        if letter in letters_guessed:
            count += 1
        else:
            continue
    if count == length:
        guessed = True
    return guessed

# secret_word = 'apple' 
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(is_word_guessed(secret_word, letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_ '
    return guessed_word

# secret_word = 'apple'  
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_guessed_word(secret_word, letters_guessed)) 



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in alphabets:
            alphabets = alphabets.replace(letter, "")
    return alphabets
    
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
# print(get_available_letters(letters_guessed))

def correct_input(string):
    """
    Takes an argument(string) which is to be a string 
    if string is an alphabet, it converts it to lower case and returns true
    else it returns false
    """ 
    if string.isalpha():
        return True
    else:
        return False


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guess = 6
    warning = 3
    vowel = 'aeiou'
    my_guessed_letters = []
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long. ')        
    result = True
    while result:
        if is_word_guessed(secret_word, my_guessed_letters):
            result = False
            break
        if guess <= 0:
            break 
        print('------------------')
        print(f'You have {guess} guesses left. ')
        print('Available letters:',get_available_letters(my_guessed_letters))
        letter_to_check = input('Please guess a letter:')
        if correct_input(letter_to_check):
            letter_to_check = letter_to_check.lower()
            if letter_to_check in my_guessed_letters:
                warning -= 1            
                if warning == 0:
                    print('Oops! You\'ve already guessed that letter. You have no warning left:',get_guessed_word(secret_word, my_guessed_letters))                
                else:
                    print(f'Oops! You\'ve already guessed that letter. You now have {warning} warnings left:',get_guessed_word(secret_word, my_guessed_letters))                
                if warning < 0: 
                    guess -= 1
                    warning = 3            
            else: 
                my_guessed_letters.append(letter_to_check)
                if letter_to_check in secret_word:
                    print('Good guess:' , get_guessed_word(secret_word, my_guessed_letters))
                elif letter_to_check in vowel:
                    guess -= 2
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, my_guessed_letters))           
                else:
                    guess -= 1
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, my_guessed_letters))
        
        else:
            warning -= 1            
            if warning == 0:
                print(' Oops! That is not a valid letter. You have no warning left:',get_guessed_word(secret_word, my_guessed_letters))                
            else:
                print(f' Oops! That is not a valid letter. You now have {warning} warnings left:',get_guessed_word(secret_word, my_guessed_letters))                
            if warning < 0: 
                guess -= 1
                warning = 3
        
    unique_letters = len(set(list(secret_word)))
    Total_score = guess * unique_letters
    if is_word_guessed(secret_word, my_guessed_letters) :    
        print('Congratulations, you won! ')
        print('Your total score for this game is:', Total_score)
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ','')
    if len(my_word) != len(other_word):
        return False
    letters_in_my_word = my_word.replace('_','')
    result = 0
    i = 0
    while i < len(my_word):
        if my_word[i] == '_' :
            i += 1
            continue
        if my_word[i] == other_word[i]:
            result += 1
        i += 1
    if result == len(letters_in_my_word):
        return True
    else:
        return False
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) >= 1:
        possible_matches = ' '.join(possible_matches)
        return possible_matches
    else:
        return 'No matches found'
    

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guess = 6
    warning = 3
    vowel = 'aeiou'
    my_guessed_letters = []
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long. ') 
    print('You can ask for help when you enter " * " as a guess, after you have guesses at least one letter correctly.', '\nGoodluck !!')    
    result = True
    while result:
        if is_word_guessed(secret_word, my_guessed_letters):
            result = False
            break
        if guess <= 0:
            break 
        print('------------------')
        print(f'You have {guess} guesses left. ')
        print('Available letters:',get_available_letters(my_guessed_letters))
        letter_to_check = input('Please guess a letter:')
        if letter_to_check == '*':
            word_to_check = get_guessed_word(secret_word, my_guessed_letters)
            word_to_check_new = word_to_check.replace(' ', '').replace('_', '')
            if len(word_to_check_new) > 1:
                print('Possible word matches are:')
                print(show_possible_matches(word_to_check))
                continue
        if correct_input(letter_to_check):
            letter_to_check = letter_to_check.lower()
            if letter_to_check in my_guessed_letters:
                warning -= 1            
                if warning == 0:
                    print('Oops! You\'ve already guessed that letter. You have no warning left:',get_guessed_word(secret_word, my_guessed_letters))                
                else:
                    print(f'Oops! You\'ve already guessed that letter. You now have {warning} warnings left:',get_guessed_word(secret_word, my_guessed_letters))                
                if warning < 0: 
                    guess -= 1
                    warning = 3            
            else: 
                my_guessed_letters.append(letter_to_check)
                if letter_to_check in secret_word:
                    print('Good guess:' , get_guessed_word(secret_word, my_guessed_letters))
                elif letter_to_check in vowel:
                    guess -= 2
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, my_guessed_letters))           
                else:
                    guess -= 1
                    print('Oops! That letter is not in my word:',get_guessed_word(secret_word, my_guessed_letters))
        
        else:
            warning -= 1            
            if warning == 0:
                print(' Oops! That is not a valid letter. You have no warning left:',get_guessed_word(secret_word, my_guessed_letters))                
            else:
                print(f' Oops! That is not a valid letter. You now have {warning} warnings left:',get_guessed_word(secret_word, my_guessed_letters))                
            if warning < 0: 
                guess -= 1
                warning = 3
        
    unique_letters = len(set(list(secret_word)))
    Total_score = guess * unique_letters
    if is_word_guessed(secret_word, my_guessed_letters) :    
        print('Congratulations, you won! ')
        print('Your total score for this game is:', Total_score)
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')
   
    
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

##############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)