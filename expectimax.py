import string
from math import inf as infitity
from typing import List

import constants as c
from heuristics import test_heuristic

MAX_NODE = "max"
CHANCE_NODE = "chance"

class Node:
    def __init__(self, value: float):
        self.value = value                   # value from heuristic
        self.children: List[Node] = []
        self.state_matrix: List[List[int]] = None
        self.action_history: List[str] = None
        
    def isTerminal(self) -> bool:
        return not self.children
    
    def generateAllPossibleCpuMoves(self):
        positions = []  # List to store the positions of zeros
        for row_idx, row in enumerate(self.state_matrix):
            for col_idx, value in enumerate(row):
                if value == 0:
                    positions.append((row_idx, col_idx))  # Add position as a tuple
        return positions
    
    def generateChildren(self, isMaxNode: bool):
        # child nodes action history should be the same when initialized and added onto later
        
        
        
        # max nodes children come from the action taken
        if isMaxNode:
            self.children.extend([c.KEY_UP, c.KEY_DOWN, c.KEY_LEFT, c.KEY_RIGHT])
        # chance nodes children come from the possible actions the cpu could take
        else:
            open_positions = self.generateAllPossibleCpuMoves()
            self.children.extend(open_positions)
        return

def newMaxNode(value: float) -> Node:
    return Node(value)

def newChanceNode() -> Node:
    return Node(0)

# need this to also return history of moves, how to record history of move, {score, {move 1, move2, ... , moveN}}
# depthlimit must be even number
def expectimax(node: Node, node_type:str, heuristic_evaluation, current_depth: int, depth_limit:int=2):    
    if not(depth_limit % 2 == 0):
        print("depth_limit must be even")
        return
    
    #generate children nodes, breaks isTerminal, needs depth limit
    node.generateChildren()
    
    # Terminal node
    if (current_depth == depth_limit):
        return heuristic_evaluation(node)

    # Maximizer node
    if node_type == MAX_NODE:
        # update action history
        
       return max(expectimax(child, CHANCE_NODE, heuristic_evaluation) for child in node.children)

    # Chance node
    return sum(expectimax(child, MAX_NODE, heuristic_evaluation) for child in node.children) / len(node.children)


def printTree(node:Node):
    if node.isTerminal():
        print(f'value: {node.value}')
        return
    
    for child in node.children:
        printTree(child)
        
        
def exampleTreeRun():
    root = Node(0)
    
    # depth 1
    chance1 = newChanceNode()
    chance2 = newChanceNode()
    # chance3 = newChanceNode()
    root.children.extend([chance1, chance2])
    
    # depth 2
    node_c1_m1 = newMaxNode(0)
    node_c1_m2 = newMaxNode(0)
    node_c1_m3 = newMaxNode(0)
    chance1.children.extend([node_c1_m1, node_c1_m2, node_c1_m3])
    
    node_c2_m1 = newMaxNode(0)
    node_c2_m2 = newMaxNode(0)
    node_c2_m3 = newMaxNode(0)
    chance2.children.extend([node_c2_m1, node_c2_m2, node_c2_m3])
    
    # depth 3
    node_c1_m1_c1 = newChanceNode()     # left most tree
    node_c1_m1_c2 = newChanceNode()
    node_c1_m1.children.extend([node_c1_m1_c1, node_c1_m1_c2])
    
    node_c1_m2_c1 = newChanceNode()     # left middle tree
    node_c1_m2_c2 = newChanceNode()
    node_c1_m2.children.extend([node_c1_m2_c1, node_c1_m2_c2])

    
    node_c1_m3_c1 = newChanceNode()     # left right tree
    node_c1_m3_c2 = newChanceNode()
    node_c1_m3.children.extend([node_c1_m3_c1, node_c1_m3_c2])
    
    node_c2_m1_c1 = newChanceNode()     # middle left tree
    node_c2_m1_c2 = newChanceNode()
    node_c2_m1.children.extend([node_c2_m1_c1, node_c2_m1_c2])

    node_c2_m2_c1 = newChanceNode()     # middle middle tree
    node_c2_m2_c2 = newChanceNode()
    node_c2_m2.children.extend([node_c2_m2_c1, node_c2_m2_c2])
 
    
    node_c2_m3_c1 = newChanceNode()     # middle right tree
    node_c2_m3_c2 = newChanceNode()
    node_c2_m3.children.extend([node_c2_m3_c1, node_c2_m3_c2])

    # depth 4
    node_c1_m1_c1_m1 = newMaxNode(1)
    node_c1_m1_c1_m2 = newMaxNode(2)
    node_c1_m1_c1.children.extend([node_c1_m1_c1_m1, node_c1_m1_c1_m2])

    node_c1_m1_c2_m1 = newMaxNode(3)
    node_c1_m1_c2_m2 = newMaxNode(4)
    node_c1_m1_c2.children.extend([node_c1_m1_c2_m1, node_c1_m1_c2_m2])

    node_c1_m2_c1_m1 = newMaxNode(-1)
    node_c1_m2_c1_m2 = newMaxNode(8)
    node_c1_m2_c1.children.extend([node_c1_m2_c1_m1, node_c1_m2_c1_m2])

    node_c1_m2_c2_m1 = newMaxNode(2)
    node_c1_m2_c2_m2 = newMaxNode(3)
    node_c1_m2_c2.children.extend([node_c1_m2_c2_m1, node_c1_m2_c2_m2])

    node_c1_m3_c1_m1 = newMaxNode(-2)
    node_c1_m3_c1_m2 = newMaxNode(1)
    node_c1_m3_c1.children.extend([node_c1_m3_c1_m1, node_c1_m3_c1_m2])
    

    node_c1_m3_c2_m1 = newMaxNode(4)
    node_c1_m3_c2_m2 = newMaxNode(1)
    node_c1_m3_c2.children.extend([node_c1_m3_c2_m1, node_c1_m3_c2_m2])

    node_c2_m1_c1_m1 = newMaxNode(0)
    node_c2_m1_c1_m2 = newMaxNode(1)
    node_c2_m1_c1.children.extend([node_c2_m1_c1_m1, node_c2_m1_c1_m2])

    node_c2_m1_c2_m1 = newMaxNode(0)
    node_c2_m1_c2_m2 = newMaxNode(2)
    node_c2_m1_c2.children.extend([node_c2_m1_c2_m1, node_c2_m1_c2_m2])

    node_c2_m2_c1_m1 = newMaxNode(3)
    node_c2_m2_c1_m2 = newMaxNode(-2)
    node_c2_m2_c1.children.extend([node_c2_m2_c1_m1, node_c2_m2_c1_m2])

    node_c2_m2_c2_m1 = newMaxNode(6)
    node_c2_m2_c2_m2 = newMaxNode(1)
    node_c2_m2_c2.children.extend([node_c2_m2_c2_m1, node_c2_m2_c2_m2])

    node_c2_m3_c1_m1 = newMaxNode(8)
    node_c2_m3_c1_m2 = newMaxNode(2)
    node_c2_m3_c1.children.extend([node_c2_m3_c1_m1, node_c2_m3_c1_m2])

    
    node_c2_m3_c2_m1 = newMaxNode(10)
    node_c2_m3_c2_m2 = newMaxNode(3)
    node_c2_m3_c2.children.extend([node_c2_m3_c2_m1, node_c2_m3_c2_m2])



    # Call the function
    result = expectimax(root, MAX_NODE, test_heuristic)
    printTree(root)
    print(f"Expectiminimax value: {result}")
    
# Driver Code
if __name__ == "__main__":
    exampleTreeRun()
    



