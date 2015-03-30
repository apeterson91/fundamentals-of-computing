"""
Monte Carlo Tic-Tac-Toe Player
http://www.codeskulptor.org/#user39_9JMeob2f3J_38.py
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """
        runs Monte Carlo Trial - choosing moves at
        random until board is in a "finished" state
        """
    current_player = player
    while board.check_win() == None:
        ## get a list of empty positions
        ## randomly pick one of them for player's move
        current_move = random.choice(board.get_empty_squares())
        board.move(current_move[0], current_move[1], current_player)
        # Switch players
        current_player = provided.switch_player(current_player)

def mc_update_scores(scores, board, player):
    """
        Updates "scoreboard" to include results of
        input parameter board by reference
        """
    if board.check_win() == player:
        for row_position in range(board.get_dim()):
            for column_position in range(board.get_dim()):
                if board.square(row_position, column_position) == player:
                    scores[row_position][column_position] += SCORE_CURRENT
                elif board.square(row_position, column_position) == provided.switch_player(player):
                    scores[row_position][column_position] -= SCORE_OTHER
    elif board.check_win() == provided.switch_player(player):
        for row_position in range(board.get_dim()):
            for column_position in range(board.get_dim()):
                if board.square(row_position, column_position) == player:
                    scores[row_position][column_position] -= SCORE_CURRENT
                elif board.square(row_position, column_position) == provided.switch_player(player):
                    scores[row_position][column_position] += SCORE_OTHER
    else:
        ## Board is a draw
        pass

def get_best_move(board, scores):
    """
        Determines which position is best for next move
        and returns tuple denoting that position
        if there are multiple "best" positions, one of
        them is returned randomly.
        Additionally, if the board has no empty squares
        it returns nothing.
        """
    ## get empty positions in board
    empty_scores = {}
    for pos in board.get_empty_squares():
        empty_scores[pos] = scores[pos[0]][pos[1]]
    #    empty_scores = {pos:scores[pos[0]][pos[1]] for pos in board.get_empty_squares()}
    ## if there are no empty squares then return nothing
    if len(empty_scores) < 1:
        return
    # determine which score is best of the empty square scores
    best_score = max([score for score in empty_scores.values()])
    if len([pos for pos,score in empty_scores.items() if score == best_score]) > 1:
        return random.choice([pos for pos,score in empty_scores.items() if score == best_score])
    else:
        return [pos for pos, score in empty_scores.items() if score==best_score][0]

def mc_move(board, player, trials):
    """
        Takes a board, which player is playing and the number of trials to run
        for a MC simulation, returns a position for the machine player to take
        in the form a (row, column) tuple.
        """
    scoreboard = [[0 for _ in range(board.get_dim())] for _ in range(board.get_dim())]
    for _ in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scoreboard,board_copy, player)
    return get_best_move(board, scoreboard)




# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

