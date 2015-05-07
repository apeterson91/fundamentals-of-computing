#http://www.codeskulptor.org/#user39_OJxWveqOZX_9.py
"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    print board, board.check_win()
    if board.check_win() == None:
        scores = []
        for position in board.get_empty_squares():
            board_clone = board.clone()
            board_clone.move(position[0],position[1],player)
            scores.append((position,mm_move(board_clone,provided.switch_player(player))[0]))
        if player == provided.PLAYERX:
            result = -1, (-1,-1)
            for score in scores:
                if score[1] == 1:
                    result = score[1],score[0]
                if score[1] > result[0]:
                    result = score[1],score[0]
            return result
        else:
            result = 1, (-1,1)
            for score in scores:
                if score[1] == -1:
                    result = score[1],score[0]
                    return result
                if score[1] < result[0]:
                    result = score[1],score[0]
            return result
    elif board.check_win() == provided.PLAYERX:
        #print board
        return 1, (-1,-1)
    elif board.check_win() == provided.PLAYERO:
        #print board
        return -1,(-1,-1)
    else:
        return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

#test_board = provided.TTTBoard(3)
#test_board.move(0,0,provided.PLAYERO)
#test_board.move(0,1,provided.PLAYERX)
#test_board.move(1,0,provided.PLAYERO)
#test_board.move(1,1,provided.PLAYERX)
#test_board.move(2,1,provided.PLAYERO)
#test_board.move(2,2,provided.PLAYERX)
#test_board.move(0,2,provided.PLAYERX)
#score, position = mm_move(test_board,provided.PLAYERO)
#print score, position
#test_board = provided.TTTBoard(3)
#test_board.move(0,0,provided.PLAYERO)
#test_board.move(0,1,provided.PLAYERX)
#test_board.move(1,0,provided.PLAYERO)
#print test_board
#print mm_move(test_board,provided.PLAYERO)