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

### Function that reverses a word
# stri = "WORDSWORTH"
# 
# def reverse(text):
#     revd=""
#     for i in range(len(text)-1,-1,-1):
#         revd=revd + text[i]
#     return revd
# 
# 


### Function that removes the vowels from a word and prints out the remaining consonants
# 
# def is_vowel(letter):
#     vowels=["a","e",'i','o','u', "A","E","I","O","U"]
#     for i in vowels:
#         if i==letter:
#             return True
#     else:
#     	return False 
# 
# def anti_vowel(text):
# 	string=[]
# 	for i in text:
# 		if not is_vowel(i):
# 			string.append(i)
# 	string= "".join(string)
# 	return string
# 	
# print anti_vowel("Look at this!")


#### Function that takes a string and calculates a scrabble score based upon the string
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
#          "x": 8, "z": 10}
# 
# def scrabble_score(word):
#     total=0
#     word=word.lower()
#     for i in word:
#     	total+=score[i]
#     return total
# 
# print scrabble_score("ADAM")

### Function that replaces second parameter input with censored hashtags
# def censor(text,word):
#  	if word in text:
#  		print text.translate("*",word)
#  	else:
#  		string = "Your word is not in the text!"
# 	return string

# print censor("this hack is wack hack", "hack")


# this function takes a list and returns its median
# def median(stg):
#     #sort list
#     sortlist=sorted(stg)
#     #check to see if list is even or not
#     if len(sortlist)%2==0:
#         # if it is then average the middle two numbers together
#         med = float((sortlist[len(sortlist)/2] + sortlist[(len(sortlist)/2)-1]))/2
#     else:
#         #just pick the middle number
#         med=sortlist[len(sortlist)/2]
#     return med
#     
# someting=[3,2,2,4,3,22,12,25,3,12]
# 
# print sorted(someting)
# 
# print(median(someting))


# cubes_by_four= [ x ** 3 for x in range(1,11) if (((x**3) % 4) == 0)]
# print cubes_by_four

## List slicing
# my_list = range(1, 11) # List of numbers 1 - 10
# print my_list[::2]


## learning functional programming
# my_list = range(16)
# print filter(lambda x: x % 3 == 0, my_list)

# threes_and_fives = [i for i in range (1,16) if (i%3==0 or i%5==0)]
# print threes_and_fives

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six  = 0b110
seven = 0b111
eight =0b1000
nine = 0b1001
ten = 0b1010  
eleven = 0b1011
twelve = 0b1100

print one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve

