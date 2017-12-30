import itertools

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

hand = {'n': 0, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}

print(get_hand_subsets(hand))