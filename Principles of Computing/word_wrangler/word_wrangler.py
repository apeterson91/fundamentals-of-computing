http://www.codeskulptor.org/#user39_MqvJKT77Jh_22.py
"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided
from math import floor

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    seen = []
    new_list = []
    for item in list1:
        if item not in seen:
            new_list.append(item)
            seen.append(item)
    return seen

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = [ _ for _ in list1 if _ in list2]
    new_list = new_list + [ _ for _ in list2 if _ in list1]
    return remove_duplicates(new_list)



# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in list1 and list2.

    This function can be iterative.
    """
    if float('inf') in list1:
        list1.remove(float('inf'))
    if float('inf') in list2:
        list2.remove(float('inf'))
    list1 = list(list1)
    list2 = list(list2)
    list1.append(float('inf'))
    list2.append(float('inf'))
    listone_index = 0
    listtwo_index = 0
    index = 0
    new_list = [None] * (len(list1) + len(list2)-2)
    while None in new_list:
        if list1[listone_index] <= list2[listtwo_index]:
            new_list[index] = list1[listone_index]
            index+=1
            listone_index+=1
        else:
            new_list[index] = list2[listtwo_index]
            index+=1
            listtwo_index+=1
    return list(new_list)

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) > 1:
        mid = int(floor(len(list1)/2))
        lone = merge_sort(list(list1[:mid]))
        ltwo = merge_sort(list(list1[mid:]))
        return merge(lone,ltwo)
    elif len(list1)==1:
        return list1
    else: return list1


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """

    if len(word) == 1:
        return [word, ""]
    elif len(word) == 0:
        return [word]
    else:
        new_list = []
        all_strings_gen = gen_all_strings(word[1:])
        for item in all_strings_gen:
            for index in range(len(item)+1):
                new_list.append(item[:index] + word[0] + item[index:])
        return new_list+all_strings_gen

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    words = urllib2.urlopen(codeskulptor.file2url(filename))
    words = [word.strip() for word in words.readlines()] 
    return words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()