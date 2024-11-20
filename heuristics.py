from expectimax import Node
import constants as c

def test_heuristic():
    return None

def highest_score_heuristic(node: Node):
    score = 0
    for row in range(c.GRID_LEN):
        for col in range(c.GRID_LEN):
            score += node.state_matrix[row][col]
    
    return score
        
    