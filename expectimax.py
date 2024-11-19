MAX_NODE = "max"
MIN_NODE = "min"
CHANCE_NODE = "chance"

class Node:
    def __init__(self, value, node_type):
        self.value = value
        self.left = None
        self.right = None
        self.node_type = node_type
        
    def isTerminal(self) -> bool:
        return self.left == None and self.right == None

def newNode(v):
    return Node(v)

def expectimax(node: Node, is_max, is_min=False):
    # Debugging output
    node_type = node.node_type
    print(f"Node value: {node.value}, Node type: {node_type}")
    
    # Terminal node
    if node.left is None and node.right is None:
        return node.value

    # Maximizer node
    if is_max:
        return max(expectimax(node.left, False, True), expectimax(node.right, False, True))

    # Minimizer node
    if is_min:
        return min(expectimax(node.left, True, False), expectimax(node.right, True, False))

    # Chance node
    return (expectimax(node.left, True, False) + expectimax(node.right, True, False)) / 2

# Driver Code
if __name__ == "__main__":
    # Build the tree
    root = newNode(0, MAX_NODE)
    root.left = newNode(0, MIN_NODE)
    root.right = newNode(0, MIN_NODE)
    
    root.left.left = newNode(10, MAX_NODE)
    root.left.right = newNode(20, MAX_NODE)
    root.right.left = newNode(5, MAX_NODE)
    root.right.right = newNode(100, MAX_NODE)

    # Call the function
    result = expectimax(root, True)
    print(f"Expectimax value: {result}")
