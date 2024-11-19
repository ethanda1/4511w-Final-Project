import string
from math import inf as infitity
from typing import List

from heuristics import test_heuristic

MAX_NODE = "max"
CHANCE_NODE = "chance"

class Node:
    def __init__(self, value: float):
        self.value = value                   # value from heuristic
        self.children: List[Node] = []
        self.state_matrix: List[List[int]] = None
        
    def isTerminal(self) -> bool:
        return not self.children

def newMaxNode(value: float) -> Node:
    return Node(value)

def newChanceNode() -> Node:
    return Node(0)

def expectimax(node: Node, node_type:string, heuristic_evaluation):    
    # Debugging output
    if node.value:
        print(f"Node value: {node.value}, Node type: {node_type}")
    
    # Terminal node
    if (node.isTerminal()):
        return node.value

    # Maximizer node
    if node_type == MAX_NODE:
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
    



