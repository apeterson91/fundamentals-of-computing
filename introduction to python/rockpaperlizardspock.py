# Rock-paper-scissors-lizard-Spock template
# http://www.codeskulptor.org/#user37_fukXg7hnQY_8.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
import math

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    if name=="rock":
        return 0
    elif name =="Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "You didn't pick an appropriate name!"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the follwing pass statement and fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "That isn't an acceptable number!"
        
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the follwing pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print "\n"
    # print out the message for the player's choice
    print "The player chose: " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = int(random.randrange(0,4))
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "The computer chose: " + comp_choice

    # compute difference of comp_number and player_number modulo five
    decision= (player_number- comp_number) % 5
    # use if/elif/else to determine winner, print winner message
    if decision==1 or decision ==2:
        print "Player wins!"
    elif decision ==3 or decision ==4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

