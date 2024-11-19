import string
from math import inf as infitity
from typing import List

MAX_NODE = "max"
CHANCE_NODE = "chance"

class Node:
    def __init__(self, value: float):
        self.value = value
        self.children: List[Node] = []
        
    def isTerminal(self) -> bool:
        return not self.children

def newMaxNode(value: float) -> Node:
    return Node(value)

def newChanceNode() -> Node:
    return Node(0)

def expectimax(node: Node, node_type:string):    
    # Debugging output
    print(f"Node value: {node.value}, Node type: {node_type}")
    
    # Terminal node
    if (node.isTerminal()):
        return node.value

    # Maximizer node
    if node_type == MAX_NODE:
       return max(expectimax(child, CHANCE_NODE) for child in node.children)

    # Chance node
    return sum(expectimax(child, MAX_NODE) for child in node.children) / len(node.children)

# Driver Code
if __name__ == "__main__":
        # Build the tree
    # root = Node(0)  # Max node

    # # Add children to the root
    # child1 = Node(0)  # Min node
    # child2 = Node(0)  # Chance node
    # root.children.extend([child1, child2])

    # # Add children to child1 (Min node)
    # child1.children.extend([Node(10), Node(20), Node(15)])  # Terminal nodes

    # # Add children to child2 (Chance node)
    # child2.children.extend([Node(5), Node(25), Node(30)])  # Terminal nodes
    
    root = Node(0)
    chance1 = newChanceNode()
    chance2 = newChanceNode()
    chance3 = newChanceNode()
    root.children.extend([chance1, chance2, chance3])
    
    chance1.children.extend([Node(2), Node(1), Node(7)])  # Terminal nodes
    chance2.children.extend([Node(3)])  # Terminal nodes
    chance3.children.extend([Node(5), Node(2)])  # Terminal nodes


    # Call the function
    result = expectimax(root, MAX_NODE)
    print(f"Expectiminimax value: {result}")



