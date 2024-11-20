from expectimax import Node
import constants as c

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