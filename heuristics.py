from expectimax import Node
import constants as c
from expectimax import print2048Matrix
import copy

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
    
    print("Previous State Matrix")
    print2048Matrix(previous_state_matrix)
    
    print("How it will be altered after this move")
    print2048Matrix(state_matrix)
    print()
    
    for i in range(0, ROW_LEN):
        for k in range(0, COL_LEN):
            if (state_matrix[i][k] != previous_state_matrix[i][k]):
                score += 1
    return score

if __name__ == "__main__":
    numberOfTilesInSameLocation(TEST_GRID)
