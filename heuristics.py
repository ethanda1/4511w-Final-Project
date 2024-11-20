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
        
    