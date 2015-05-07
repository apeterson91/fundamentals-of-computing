http://www.codeskulptor.org/#user39_jC7vswDwSd_506.py
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            print direction
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction
            print self
            
    ##################################################################
    # Phase one methods

    def get_correct_number(self, target_row, target_col):
        """
        determines what number should be located at a 
        specific location
        """
        return target_row * self.get_width() + target_col
    
    def get_tile_position(self, target_num):
        """
        Returns the row,column tuple denoting 
        the target_num's position within the grid
        """
        for row_index in range(self.get_height()):
            for column_index in range(self.get_width()):
                if self._grid[row_index][column_index] == target_num:
                    target_indices = (row_index, column_index)
        return target_indices

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        switch = False
        if self._grid[target_row][target_col] != 0:
            print self
            print "error here"
            return False
        if target_col+1 == self.get_width():
            row_index = target_row + 1
            column_index = 0
        else:
            column_index = target_col + 1
            row_index = target_row
        while row_index < self.get_height():
            if column_index == self.get_width() and switch==True:
                column_index = 0
            while column_index < self.get_width():
                if self._grid[row_index][column_index] != (row_index)*self.get_width() + column_index:
                    return False
                column_index+=1
            row_index += 1
            switch = True
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        #find position of desired number
        target_num = (target_row) * self.get_width() + (target_col)
        target_indices = self.get_tile_position(target_num)
        move_string = ""
        if target_indices[0] == target_row: 
            # only need to move left and cycle
            move_string += "l" * (target_col-target_indices[1])
            # put zero to the left of the target num
            move_string += "urrdl" * (target_col-target_indices[1]-1)
        else:
            ## target number above the zero - and to the right or left
            move_string += "u" * abs(target_row-target_indices[0])
            if target_col - target_indices[1] < 0:
                move_string += "r" * abs(target_col-target_indices[1])
                move_string += "dlu"
                move_string += "lddru" * (abs(target_row-target_indices[0])-1)
                move_string += "ld"
            elif target_col - target_indices[1] > 0:
                move_string += "l" * abs(target_col-target_indices[1])
                move_string += "dru"
                move_string += "lddru" * (abs(target_row - target_indices[0])-1)
                move_string += "rdl"
            else:
                move_string+= "lddru" * int(float(self.get_height())/2.0)
                move_string+= "ld"
        print move_string
        self.update_puzzle(move_string)
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        target_num = self.get_correct_number(target_row,0)
        if self._grid[target_row-1][0] == target_num:
            move_string = 'ur'
        else:
            target_indices = self.get_tile_position(target_num)
            if target_indices[0] == target_row-1:
                if target_indices[1] == 1:
                    move_string = 'url'
                elif target_indices[1] > 1:
                    move_string = 'ur'
                    move_string += 'r' * (target_indices[1]-1)
                    move_string += 'ulldr' * (target_indices[1]-1)
                    move_string += 'ulld'
            else:
                ## more than one row above zero tile
                move_string = 'u' * abs(target_indices[0] - target_row)
                move_string += 'r' * abs(target_indices[1]-1)
                move_string += 'rdlu'
                move_string += 'rddlu' * abs(target_row-2-target_indices[0])
                move_string += 'rdl'
                if target_indices[1] -1 > 0:
                    move_string += 'ulldr' * (target_indices[1]-1)
                    move_string += 'ulld'
            move_string += 'ruldrdlurdluurddlur'
        move_string += 'r' * (self.get_width() - 2)
        self.update_puzzle(move_string)
        
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[0][target_col] == 0:
            if self._grid[1][2] == self.get_correct_number(1,2):
                for column_index in range(target_col+1, self.get_width()):
                    if self._grid[0][column_index] != self.get_correct_number(0,column_index):
                        return False
                    if self._grid[1][column_index] != self.get_correct_number(1,column_index):
                        return False
                for row_index in range(2,self.get_height()):
                    for column_index in range(self.get_width()):
                        if self._grid[row_index][column_index] != self.get_correct_number(row_index,column_index):
                            return False  
                return True
            else:
                return False
        else:
            return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if self._grid[1][target_col] == 0:
            for column_index in range(target_col+1,self.get_width()):
                if self._grid[1][column_index] != self.get_correct_number(1,column_index):
                    return False
            for row_index in range(2,self.get_height()):
                for column_index in range(self.get_width()):
                    if self._grid[row_index][column_index] != self.get_correct_number(row_index,column_index):
                        return False
        else:
            return False
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        target_num = self.get_correct_number(0,target_col)
        target_indices = self.get_tile_position(target_num)
        move_string = 'ld'
        if target_indices != (0,target_col-1):
            if target_indices[0] == 1:
                move_string += 'l' * (abs(target_col - target_indices[1])-1)
                if self.get_width()>3: ## not sure about this move
                    num_shifts = abs(target_col-target_indices[1])/2 if target_indices[1] == 0 else (abs(target_col-target_indices[1])-1)/2
                    move_string += 'urrdl' * num_shifts
                ### need to move target tile into (1,j-1) position 
                ## with zero tile in (1,j-2) position
            elif target_indices[0] == 0:
                move_string += 'l' * (abs(target_col - target_indices[1])-1)
                move_string += 'urdl'
            print move_string
            move_string += 'urdlurrdluldrruld'
        self.update_puzzle(move_string)
        return move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # two cases, either on the same row, or one row above
        target_num = self.get_correct_number(1,target_col)
        target_indices = self.get_tile_position(target_num)
        # same row:
        if target_indices[0] == 1:
            move_string = 'l' * abs(target_col - target_indices[1])
            move_string += 'urrdl' * (abs(target_col-target_indices[1])-1)
        #different row
        elif target_indices[0] == 0:
            if target_indices[1] == target_col:
                move_string = 'u'
            else:
                move_string = 'l' * abs(target_indices[1] - target_col)
                move_string += 'urdl'
                if abs(target_indices[1]-target_col)>1:
                    move_string += 'urrdl' * (abs(target_indices[1] - target_col)-1)
        move_string += 'u'
        move_string += 'r' 
        self.update_puzzle(move_string)
        return move_string

    ###########################################################
    # Phase 3 methods
    
    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_string = ''
        if self._grid[0][0] != 0 : 
            if self._grid[0][1] == 0:
                move_string += 'l'
            if self._grid[1][1] == 0:
                move_string += 'ul'
            if self._grid[1][0] == 0:
                move_string += 'u'
        self.update_puzzle(move_string)
        new_move_string = ''
        quick_check = list(self._grid[0] + self._grid[1])
        if all(quick_check[i] <= quick_check[i+1] for i in xrange(len(quick_check)-1)):
            return move_string
        if self._grid[0][1] > self._grid[1][1]:
            if self._grid[0][1] > self._grid[1][0]:
                new_move_string += 'drul'
            else:
                new_move_string += 'rdul'
        else:
            return False
        
        self.update_puzzle(new_move_string)
        return move_string + new_move_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move_string = ''
        quick_check = list()
        for row_index in range(self.get_height()-1,-1,-1):
            for column_index in range(self.get_width()-1,-1,-1):
                if self._grid[row_index][column_index] != self.get_correct_number(row_index,column_index):
                    zero_target = (row_index, column_index)
                    break
            if type(zero_target) == tuple:
                break
        if self._grid[self.get_height()-1][self.get_width()-1] != 0:
            zero_position = self.get_tile_position(0)
            if zero_target[1] - zero_position[1] > 1:
                move_string += 'r' * (zero_target[1] - zero_position[1])
            else:
                move_string += 'l' * (zero_position[1] - zero_target[1])
            if zero_target[0] - zero_position[0] > 0:
                move_string += 'd' * (zero_target[0] - zero_position[0])
            else:
                move_string += 'u' * (zero_position[0] - zero_target[0])
        self.update_puzzle(move_string)
        column_index = zero_target[1]
        for row_index in range(zero_target[0],-1,-1):
            while column_index >= 0:
                print row_index, column_index
                if row_index > 1 and column_index >0:
                    print row_index, column_index
                    assert self.lower_row_invariant(row_index,column_index) == True #, "Row # %r invariant false", % row_index
                    move_string += self.solve_interior_tile(row_index,column_index)
                    assert self.lower_row_invariant(row_index,column_index-1) == True #, "Row # %r invariant false", % row_index
                elif row_index > 1 and column_index == 0:
                    assert self.lower_row_invariant(row_index, column_index) == True #, "Row # %r invariant false", % row_index
                    move_string += self.solve_col0_tile(row_index)
                    assert self.lower_row_invariant(row_index-1, self.get_width()-1)
                elif row_index == 1 and column_index > 1:
                    assert self.row1_invariant(column_index) == True #, "Row 1, column %r invariant is false", % column_index
                    move_string += self.solve_row1_tile(column_index)
                elif row_index == 0 and column_index > 1:
                    assert self.row0_invariant(column_index) == True #, "Row 0, column %r invariant is false", % column_index
                    move_string += self.solve_row0_tile(column_index)
                column_index += 0
            column_index = self.get_width()-1
        move_string += self.solve_2x2()
        return move_string

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))

obj = Puzzle(4, 5, [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]])
obj.solve_puzzle()