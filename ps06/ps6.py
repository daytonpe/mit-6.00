# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time
import json
import itertools


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
points_dict = {}
rearrange_dict = {}


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0

    for i in word:
        score = score + SCRABBLE_LETTER_VALUES.get(i)

    if len(word) == n:
        score = score + 50

    return score
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print() out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print( letter, end=' ' )            # print() all on the same line
    print()                              # print() an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n / 3) #******* I CHANGED THIS FOR PYTHON3 *****
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    for letter in word:
        hand[letter] = hand.get(letter,0) - 1
    return hand

# PS05 Implementation of is_valid_word (unused)
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    hand2 = hand.copy()

    for letter in word:
        if hand2.get(letter, 0) == 0: #if letter is not in hand (or letter has run out)
            return False
        hand2[letter] = hand2.get(letter,0) -1 #decrement letter in hand

    if word in word_list:
        return True
    else: 
        return False

# PS06 Implementation of is_valid_word
def is_valid_word_points(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """

    hand2 = hand.copy()

    for letter in word:
        if hand2.get(letter, 0) == 0: #if letter is not in hand (or letter has run out)
            return False
        hand2[letter] = hand2.get(letter,0) -1 #decrement letter in hand

    if word in points_dict:
        return True
    else: 
        return False

def pick_best_word(hand, points_dict):

    """ Return the highest scoring word from points_dict that can be made with thegiven hand.
    Return '.' if no words can be made with the given hand.
    """
    current_max = 0
    current_word = "."

    for word in word_list:
        if is_valid_word_points(word, hand, points_dict) and points_dict[word]>current_max:
            current_max = points_dict[word]
            current_word = word
    return current_word

def pick_best_word_faster(hand, rearrange_dict):
    hand_subsets = get_hand_subsets(hand)
    current_max = 0
    current_word = '.'
    for subset in hand_subsets:
        if subset in rearrange_dict:
            temp_word = rearrange_dict[subset] #unscramble sorted word
            if points_dict[temp_word] > current_max:
                current_max = points_dict[temp_word]
                current_word = temp_word
    return current_word

def get_hand_subsets(hand):
    """
    hand_subsets is subsets of the letters of hand.
    """
    letters = [c for c in hand for i in range(hand[c])]
    hand_subsets = ()
    for i in reversed(range(1, len(letters)+1)):
        for tup in set(itertools.combinations(letters, i)):
            hand_subsets += (''.join(sorted(tup)), )
    return hand_subsets

def get_words_to_points(word_list):
    """ Return a dict that maps every word in word_list to its point value.
    """
    for word in word_list:
        score = get_word_score(word, len(word))
        points_dict[word] = score

    # WRITE THE POINTS_DICT TO JSON
    # with open('scores.txt', 'w') as file:
    #  file.write(json.dumps(points_dict))

    return points_dict

def get_word_rearrangements(word_list):
    for word in word_list:
        sorted_word = ''.join(sorted(word))
        rearrange_dict[sorted_word] = word
    return

def get_time_limit(points_dict, k):
    """
    Return the time limit for the computer player as a function of the
    multiplier k.
    points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word, HAND_SIZE)
    end_time = time.time()
    return (end_time - start_time) * k


# word_list = load_words()
# print(is_valid_word('honey', {'n': 0, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}, word_list))

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """

    score = 0
    elapsed_time = 0;
    print()
    # while True:
    #     try:
    #         time_limit = float(input("Enter time limit, in seconds, for players: "))
    #         break
    #     except ValueError:
    #         print("Please enter a valid number...")

    time_limit = TIME_LIMIT  
    
    while(True):

        if sum(hand.values())==0:
            break;

        print()
        print('Current Hand')
        display_hand(hand)
        # print(sum(hand.values()))
        
        start_time = time.time()
        # guess = input("Enter word, or a . to indicate that you are finished: ")
        # guess = pick_best_word(hand, points_dict)
        guess = pick_best_word_faster(hand, rearrange_dict)
        end_time = time.time()


        word_time = end_time - start_time
        if word_time<.1:
            word_time = .1;

        elapsed_time = elapsed_time + word_time


        print('It took %0.2f seconds to provide an answer.' % word_time)

        if elapsed_time>time_limit:
            print('\nTotal time exceeds {0:0.0f} seconds. You scored {1:0.2f} points.'.format(time_limit, score))
            return 0

        if guess == '.':
            print()
            break
        
        # if (is_valid_word(guess, hand, word_list)==False):
        #     print()
        #     print("Invalid guess. Try again:")
        #     print()

        else: 
            hand = update_hand(hand, guess)
            points = get_word_score(guess, HAND_SIZE) / word_time
            score = score + points
            print(str(guess).upper()+' earned %0.2f points' % points)
            print('Total Score: %0.2f' % score) 
            print()
            
    print('********************')
    print('TOTAL SCORE: '+str(score))
    print('********************')
    return 0     

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """k
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    # print("play_game not implemented.")         # delete this once you've completed Problem #4
    # play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    # play_hand({'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}, word_list)
    ## uncomment the following block of code once you've completed Problem #4
   
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list, points_dict)
            print()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list, points_dict)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.") 

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    get_words_to_points(word_list)
    get_word_rearrangements(word_list)
    TIME_LIMIT = get_time_limit(points_dict,5)
    play_game(word_list)
    # print('TIME LIMIT: ', TIME_LIMIT)


# PS06 Problem #5
# It seems that...
# pick_best_word will be O(n) where n is the number of words in the word list
# pick_best_word_faster will be O(1) since our hand size is fixed
# ...thus our number of hand multisets will remain constant as well
# ...leaving us just about the same number of operations each time
# ...some minimal variation depending on length of our words if we pick more than one


