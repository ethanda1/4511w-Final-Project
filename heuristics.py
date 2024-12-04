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
    print(matrix)
    for row in matrix:
        for element in row:
            score += element
    
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

if __name__ == "__main__":
    numberOfTilesInSameLocation(TEST_GRID)
