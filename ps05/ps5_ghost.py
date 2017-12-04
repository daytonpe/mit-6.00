# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print('Loading word list from file...')
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', encoding='ascii')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def word_ends_game(word, word_list):
    if len(word)<4:
        return False
    else:
        if word.lower() in word_list:
            return True
        else: 
            return False

def word_can_be_formed(word, word_list):
    for entry in word_list:
        if word.lower() == entry[0:len(word)]:
            return True
    return False



def play_game(word_list):

    print()
    print()

    turn = 1;

    word = ''

    while (True):
        if turn%2==1:
            letter = input("Player 1: ")
            
        else:
            letter = input("Player 2: ")

        if letter not in string.ascii_letters:
            print("That's not a letter. Please Try again.")
            continue


        turn = turn + 1
        word = word+letter

        if word_can_be_formed(word, word_list)==False:
            print('GAME OVER! ' +str(word.upper())+' does not start a word')
            word = ''
            return 0

        print()
        print(word.upper())

        if(word_ends_game(word, word_list)):
            print('GAME OVER! ' +str(word.upper())+' is a word.')
            word = ''
            return 0


def play_ghost(word_list):
    print()
    print('GHOST')
    while True:
        cmd = input('n: new game\ne: end game\n')
        if cmd == 'n' or cmd == 'N':
            play_game(word_list)
            print()
        elif cmd == 'e' or cmd == 'E':
            break
        else:
            print("Invalid command.") 


play_ghost(wordlist)



