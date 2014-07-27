#############BattleShip Game###################
##### Practice using Conditionals, lists, dictionaries, etc. ######

# from random import randint
# 
# board = []
# 
# for x in range(5):
#     board.append(["O"] * 5)
# 
# def print_board(board):
#     for row in board:
#         print " ".join(row)
# 
#     
# print "Let's play Battleship!"
# print_board(board)
# 
# def random_row(board):
#     return randint(0, len(board) - 1)
# 
# def random_col(board):
#     return randint(0, len(board[0]) - 1)
# 
# ship_row = random_row(board)
# ship_col = random_col(board)
# 
# for turn in range(4):
#     # Everything from here on should go in your for loop!
#     # Be sure to indent four spaces!
#     
#     guess_row = int(raw_input("Guess Row:"))
#     guess_col = int(raw_input("Guess Col:"))
#     
#     if guess_row == ship_row and guess_col == ship_col:
#         print "Congratulations! You sunk my battleship!"
#         break
#     else:
#         if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
#             print "Oops, that's not even in the ocean."
#         elif(board[guess_row][guess_col] == "X"):
#             print "You guessed that one already."
#         else:
#             print "You missed my battleship!"
#             board[guess_row][guess_col] = "X"
#         # Print (turn + 1) here!
#         print "Turn", turn+1 
#     if turn == 3 :
#         print "Game Over"
#         print_board(board)
#         
# 


### Function that checks if a number is prime
# def is_prime(x):
#     if x==2:
#         return True
#     elif x<=1:
#         return False
#     else:
#         for n in range(2,x):
#             if (x%n==0):
#                 return False
#     return True
#     
# choice = int(raw_input("Pick a number to check if prime: "))
# 
# print (is_prime(choice))


stri = "WORDSWORTH"

def reverse(text):
    revd=""
    for i in range(len(text)-1,-1,-1):
        revd=revd + text[i]
    return revd


def is_vowel(letter):
    vowels=["a","e",'i','o','u', "A","E","I","O","U"]
    for i in vowels:
        if i==letter:
            return True
    else:
    	return False 

def anti_vowel(text):
	string=[]
	for i in text:
		if not is_vowel(i):
			string.append(i)
	string = string.join("")
	return string
    
print anti_vowel("hey Look at these words")
    
    