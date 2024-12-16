from expectimax import Node
import constants as c
from expectimax import print2048Matrix
import copy
from typing import List


TEST_GRID = [
    [2, 4, 8, 16],
    [32, 64, 128, 256],
    [512, 1024, 2048, 0],
    [0, 0, 0, 0]
]

def test_heuristic():
    return None

def highest_score_heuristic(state_matrix, previous_state_matrix):
    score = 0
    matrix = state_matrix        # 2048 game holds state_matrix in form (matrix, boolean)
    for row in matrix:
        for element in row:
            score += element
    
    return score

# This was heuristic was completed with some ChatGPT code.
def most_potential_tile_merges(state_matrix, previous_state_matrix):
    score = 0

    for row in range(0, c.GRID_LEN):
        for col in range(0, c.GRID_LEN):
            current_value = state_matrix[row][col]
            
            # Check left (i, col-1)
            if col - 1 >= 0 and state_matrix[row][col - 1] == current_value:
                score += 1
            
            # Check right (i, col+1)
            if col + 1 < c.GRID_LEN and state_matrix[row][col + 1] == current_value:
                score += 1
            
            # Check up (i-1, col)
            if row - 1 >= 0 and state_matrix[row - 1][col] == current_value:
                score += 1
            
            # Check down (i+1, col)
            if row + 1 < c.GRID_LEN and state_matrix[row + 1][col] == current_value:
                score += 1
    return score

def fewest_filled_tiles(state_matrix, previous_state_matrix):
    score = 0
    for row in state_matrix:
        for element in row:
            if (element == 0):
                score += 1
    return score

def moveTilesDown(state_matrix, previous_state_matrix):
    score = 0
    for row in range(0, c.GRID_LEN):
        for col in range(0, c.GRID_LEN):
            score += (row * 0.1) * state_matrix[row][col]
    return score

def numberOfTilesInSameLocation(state_matrix, previous_state_matrix):
    '''score will go up as less tiles are in the same location '''
    ROW_LEN = len(state_matrix)
    COL_LEN = len(state_matrix[0])
    score = 0
    
    for i in range(0, ROW_LEN):
        for k in range(0, COL_LEN):
            if (state_matrix[i][k] != previous_state_matrix[i][k]):
                
                score += 1
    return score

def highTilesAlongSingleEdge(state_matrix, previous_state_matrix):
    ROW_LEN = len(state_matrix)
    
    top_row: List[int] = state_matrix[0]
    bottom_row: List[int] = state_matrix[-1]
    
    # Left Edge
    left_edge: List[int] = []
    for i in range(0, ROW_LEN):
        left_edge.append(state_matrix[i][0])
        
    # Right Edge
    right_edge: List[int] = []
    for i in range(0, ROW_LEN):
        right_edge.append(state_matrix[i][-1])
    
    top_edge_score = sum(top_row)
    bottom_edge_score = sum(bottom_row)
    left_edge_score = sum(left_edge)
    right_edge_score = sum(right_edge)
    
    score = max([top_edge_score, bottom_edge_score, left_edge_score, right_edge_score])
    
    return score

def monotonicity_heuristic(state_matrix, previous_state_matrix):
    ROW_LEN = len(state_matrix)
    COL_LEN = len(state_matrix[0])

    # Calculates monotonicity for a single row or column
    def calculate_monotonicity(line):
        increasing = 0
        decreasing = 0
        for i in range(len(line) - 1):
            if line[i] > line[i + 1]:
                decreasing += line[i] - line[i + 1]
            elif line[i] < line[i + 1]:
                increasing += line[i + 1] - line[i]
        return min(increasing, decreasing)

    # Calculate monotonicity for rows
    row_monotonicity = sum(calculate_monotonicity(row) for row in state_matrix)

    # Calculate monotonicity for columns 
    col_monotonicity = sum(calculate_monotonicity([state_matrix[row][col] for row in range(ROW_LEN)]) for col in range(COL_LEN))

    score = row_monotonicity + col_monotonicity
    
    return score


if __name__ == "__main__":
    numberOfTilesInSameLocation(TEST_GRID)
