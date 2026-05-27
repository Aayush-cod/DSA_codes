class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
 
nodeA = Node(2)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(5)

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD

print("Binary tree ", root.left.left.data)