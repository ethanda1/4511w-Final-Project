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

def highest_score_heuristic(state_matrix):
    score = 0
    matrix = state_matrix        # 2048 game holds state_matrix in form (matrix, boolean)
    print(matrix)
    for row in matrix:
        for element in row:
            score += element
    
    return score
        
def fewest_filled_tiles(state_matrix):
    score = 0
    for row in state_matrix:
        for element in row:
            if (element == 0):
                score += 1
    return score

def moveTilesDown(state_matrix):
    score = 0
    for row in range(0, c.GRID_LEN):
        for col in range(0, c.GRID_LEN):
            score += (row * 0.1) * state_matrix[row][col]
    return score

def numberOfTilesInSameLocation(state_matrix):
    '''score will go down as more tiles are in the same location, suggesting the game is stuck'''
    ROW_LEN = len(state_matrix)
    COL_LEN = len(state_matrix[0])
    score = 0
    copied_matrix = copy.deepcopy(state_matrix)
    return 0

if __name__ == "__main__":
    numberOfTilesInSameLocation(TEST_GRID)
