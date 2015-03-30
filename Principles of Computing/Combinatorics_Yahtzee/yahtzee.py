"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
http://www.codeskulptor.org/#user39_tPLOVHmrmi_47.py
"""

# Used to increase the timeout, if necessary
import codeskulptor
from collections import Counter 
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: sorted tuple representing a full Yahtzee hand

    Returns an integer score 
    """
    hand_count = Counter(hand)
    max_value = float('-inf')
    for key,value in hand_count.items():
        if key*value>max_value:
            max_value = key*value
    return max_value
    
               
def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: a sorted tuple representing dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    possible_die_rolls = set()
    for roll in gen_all_sequences(list(range(1,num_die_sides+1)),num_free_dice):
        possible_die_rolls.add(tuple(list(roll)))
    scores_list = [(score(possible_die_roll+held_dice)) for possible_die_roll in possible_die_rolls]
    return float(sum(scores_list))/float(len(possible_die_rolls))


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: sorted tuple representing a full Yahtzee hand

    Returns a set of sorted tuples, where each tuple is dice to hold
    """
    all_holds = set([()])
    for subset_length in range(1,len(hand)+1):
        for subset in gen_all_sequences(hand,subset_length):
            if all([hand.count(number) >= subset.count(number) for number in subset]):
                all_holds.add(tuple(sorted(list(subset))))
    return all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: sorted tuple representing a full Yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    possible_hands = gen_all_holds(hand)
    expected_values = {}
    for possible_hand in possible_hands:
        expected_values[possible_hand] = expected_value(possible_hand,num_die_sides,len(hand)-len(possible_hand))
    max_ev = max(expected_values.values())
    max_hand = [key for key in expected_values.keys() if expected_values[key] == max_ev][0]
    return (max_ev, max_hand)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 2, 2)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)