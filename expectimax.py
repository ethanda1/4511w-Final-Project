import string
from math import inf as infitity
from typing import List
from copy import deepcopy

import logic as game_logic
import constants as c


MAX_NODE = "max"
CHANCE_NODE = "chance"

GAME_ACTIONS = [c.KEY_UP, c.KEY_DOWN, c.KEY_LEFT, c.KEY_RIGHT]

def print2048Matrix(matrix):
    for row in matrix:
        print(row)

class ExpectimaxValue:
    def __init__(self, score, action_history: List):
        self.score = score
        self.action_history = action_history
        

class Node:
    def __init__(self, value=None, children=[], state_matrix=[], action_history=[], action=None):
        self.value = value                   # value from heuristic
        self.children: List[Node] = children
        self.state_matrix = state_matrix
        self.action_history: List[str] = action_history
        self.action = action
        
    def isTerminal(self) -> bool:
        return not self.children
    
    def generateAllPossibleCpuMoves(self):
        positions = []  # List to store the positions of zeros
        for row_idx, row in enumerate(self.state_matrix):
            for col_idx, value in enumerate(row):
                if value == 0:
                    positions.append((row_idx, col_idx))  # Add position as a tuple
        return positions
    
    def generateChildren(self, node_type: str, heuristic):
        generated_children = []
    
        print("\nactual matrix")
        print2048Matrix(self.state_matrix)
        # max nodes children come from the action taken, generate a child node for each movement action
        if node_type == MAX_NODE:
            for game_action in GAME_ACTIONS:
                result_matrix = None
                new_action_history = deepcopy(self.action_history)
                new_action_history.append(game_action)
                
                if game_action == c.KEY_UP:
                    result_matrix = game_logic.up(self.state_matrix)[0]        # result matrix is the matrix if the move is taken
                elif game_action == c.KEY_DOWN:
                    result_matrix = game_logic.down(self.state_matrix)[0]
                elif game_action == c.KEY_RIGHT:
                    result_matrix = game_logic.right(self.state_matrix)[0]
                elif game_action == c.KEY_LEFT:
                    result_matrix = game_logic.left(self.state_matrix)[0]
                
                # Taking this move results in same matrix, don't take it
                if (result_matrix == self.state_matrix):
                    continue
                
                evaluated_score = heuristic(result_matrix)
                node = Node(evaluated_score, [], result_matrix, new_action_history, game_action)
                generated_children.append(node)
          
        # chance nodes children come from the possible actions the cpu could take, generate children from all open board positions
        else:
            open_positions = self.generateAllPossibleCpuMoves()
            for position in open_positions:
                node = Node(value=0, children=[], state_matrix=self.state_matrix, action_history=self.action_history, action=position)
                generated_children.append(node)
                
        self.children.extend(generated_children)

# need this to also return history of moves, how to record history of move, {score, {move 1, move2, ... , moveN}}
# depthlimit must be even number
def expectimax(node: Node, node_type:str, heuristic, current_depth: int, depth_limit:int=2):    
    if not(depth_limit % 2 == 0):
        print("depth_limit must be even")
        return
    
    #generate children nodes, breaks isTerminal, needs depth limit
    node.generateChildren(node_type, heuristic)
    
    # Terminal node
    if (current_depth == depth_limit):
        return ExpectimaxValue(node.value, node.action_history)

    # Maximizer node
    if node_type == MAX_NODE:
        # update action history

        max_score = 0
        best_action_history = None
        
        for child in node.children:
            ret_val: ExpectimaxValue = expectimax(child, CHANCE_NODE, heuristic, current_depth + 1, depth_limit)
            if (ret_val.score >= max_score):
                max_score = ret_val.score
                best_action_history = ret_val.action_history
        return ExpectimaxValue(max_score, best_action_history)
        

    # Chance node
    sum = 0
    for child in node.children:
        ret_val: ExpectimaxValue = expectimax(child, MAX_NODE, heuristic, current_depth + 1, depth_limit)
        sum += ret_val.score
    average_sum = sum / len(node.children)
    return ExpectimaxValue(average_sum, node.action_history)


def printTree(node:Node):
    if node.isTerminal():
        print(f'value: {node.value}')
        return
    
    for child in node.children:
        printTree(child)
    
# Driver Code
if __name__ == "__main__":
    print()
