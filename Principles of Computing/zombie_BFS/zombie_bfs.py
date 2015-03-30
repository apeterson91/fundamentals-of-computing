"""
Student portion of Zombie Apocalypse mini-project
http://www.codeskulptor.org/#user39_XmwzX8Izme_78.py
"""

from random import choice
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.__init__(self, self.get_grid_height(),self.get_grid_width())
        self._zombie_list = []
        self._human_list = []
        self._obstacle_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = poc_grid.Grid(self.get_grid_height(),self.get_grid_width())
        distance_field = [[self.get_grid_width() * self.get_grid_height() for _ in range(self.get_grid_width())]
                          for __ in range(self.get_grid_height())]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            entity_type = self._human_list
        else:
            entity_type = self._zombie_list
        for item in entity_type:
            boundary.enqueue(item)
        for item in boundary:
            visited.set_full(item[0],item[1])
            distance_field[item[0]][item[1]] = 0
        while len(boundary) != 0:
            current_cell = boundary.dequeue()
            for neighbor in self.four_neighbors(current_cell[0],current_cell[1]):
                if visited.is_empty(neighbor[0],neighbor[1]) and self.is_empty(neighbor[0],neighbor[1]):
                    visited.set_full(neighbor[0],neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
        return distance_field
            
        
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        neighbors = {}
        new_human_list = []
        for human in self._human_list:
            for neighbor in self.eight_neighbors(human[0],human[1]):
                neighbors[neighbor] = zombie_distance[neighbor[0]][neighbor[1]]
            neighbors[human] = zombie_distance[human[0]][human[1]]
            potential_humans = [new_human for new_human in neighbors.keys() 
                                          if self.is_empty(new_human[0],new_human[1])]
            for index in neighbors.keys():
                if index not in potential_humans:
                    neighbors[index] = 0
            new_human_list.append(choice([new_human for new_human in potential_humans 
                                          if max(neighbors.values()) == neighbors[new_human]]))
            neighbors = {}
        self._human_list = list(new_human_list)
      
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        neighbors = {}
        new_zombie_list = []
        for zombie in self._zombie_list:
            for neighbor in self.four_neighbors(zombie[0],zombie[1]):
                neighbors[neighbor] = human_distance[neighbor[0]][neighbor[1]]
            neighbors[zombie] = human_distance[zombie[0]][zombie[1]]
            new_zombie_list.append(choice([new_zombie for new_zombie in neighbors.keys()
                                           if neighbors[new_zombie] == min(neighbors.values())
                                          and (self.is_empty(new_zombie[0],new_zombie[1]) or new_zombie == zombie)]))
            neighbors = {}
        self._zombie_list = list(new_zombie_list)
        

# Start up gui for simulation - You will need to write some code above
# before this will work without errors


#poc_zombie_gui.run_gui(Zombie(30, 40))

