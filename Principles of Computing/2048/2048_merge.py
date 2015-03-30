"""
    Merge function for 2048 game.
    http://www.codeskulptor.org/#user39_HoE5rKkqM7_0.py
"""

def merge(line):
    """
        Function that merges a single row or column in 2048.
        """
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