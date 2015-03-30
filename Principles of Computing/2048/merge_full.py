"""
Clone of 2048 game.
http://www.codeskulptor.org/#user39_x3p2vi9Ufp_207.py
"""



#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}




def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
        # replace with your code
    result_list_one = [0 for index in range(len(line))]
    result_list_index = 0
    for index in range(len(line)):
        if line[index] != 0:
            result_list_one[result_list_index] = line[index]
            result_list_index += 1
    result_list_two = list(result_list_one)
    for index in range(len(result_list_one)-1):
        if result_list_one[index+1] == result_list_one[index]:
            result_list_two[index] = 2*result_list_one[index]
            result_list_two[index+1] = 0
            result_list_one[index+1] = 0
    result_list_final = [0 for index in range(len(line))]
    result_list_index = 0
    for index in range(len(result_list_two)):
        if result_list_two[index] != 0:
            result_list_final[result_list_index] = result_list_two[index]
            result_list_index += 1
    
    return result_list_final

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your cod
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._initial_indices = {
            1 :[(0,i) for i in range(grid_width)],
            2 :[(grid_height-1,i) for i in range(grid_width)],
            3 :[(i,0) for i in range(grid_height)],
            4 :[(i,grid_width-1) for i in range(grid_height)]
        }
        self._directions_map= {1: (1, 0),
           2: (-1, 0),
           3: (0, 1),
           4: (0, -1)}                            
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [ [0 for _ in range(self.get_grid_width())] for _ in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        print_str = ""
        for row in range(self.get_grid_height()):
            print_str += str(self._grid[row])
            print_str += "\n"
        return print_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direct = self._directions_map[direction]
        num_steps = self.get_grid_height() if direction == 1 or direction == 2 else self.get_grid_width()
        ## Collect entries from appropriate row/column, up/down/left/right perspective for mergin
        list_of_merge_lists = [[self._grid[start_index[0] + step * direct[0]]
            [start_index[1] + step * direct[1]] for step in range(num_steps)] 
            for start_index in self._initial_indices[direction]]
        ## Merge all entries
        merged_lists = [merge(line) for line in list_of_merge_lists]
        grid_copy = [list(row) for row in self._grid]
        
        ### Determine how to input merged lists back into 
        ### Grid based upon the direction
        
        for index in range(len(merged_lists)):
            grid_counter = self.get_grid_width()-1
            for j_index in range(len(merged_lists[0])):
                if direction == 1:
                    self._grid[j_index][index] = merged_lists[index][j_index]
                elif direction == 2:
                    k_index,l_index = self.get_grid_height()-1-j_index,index
                    self._grid[k_index][l_index] = merged_lists[index][j_index]
                elif direction == 3:
                    self._grid = list(merged_lists)
                elif direction == 4:
                    self._grid[index][grid_counter] = merged_lists[index][j_index]
                    grid_counter -= 1
        

        ### Might still need to add in check that 
        ### Sees if previous grid and new merged grid are the same
        ### Before adding new tile
        if self._grid != grid_copy:
            self.new_tile()
       
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if 0 in [entry for row in range(self.get_grid_height()) for entry in self._grid[row]]:
            choice = 2 if random.random() < .9 else 4
            row,col = random.randrange(0,self.get_grid_height()), random.randrange(0,self.get_grid_width())
            if self._grid[row][col] != 0:
                while self._grid[row][col] != 0:
                    row,col = random.randrange(0,self.get_grid_height()), random.randrange(0,self.get_grid_width())
            self._grid[row][col] = choice


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))