
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = 0
        self.right = 0

class Binarytree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)

        if not self.root:
            self.root = newnode
            return
        

        queue = deque([self.root])

        while queue:

            temp = queue.popleft()

            if not temp.left:
                temp.left = newnode
                return
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = newnode
                return
            else:
                queue.append(temp.right)

    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")




# root = Node(1)

# nodeA = Node(2)
# nodeB = Node(3)
# nodeC = Node(4)
# nodeD = Node(5)

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# print("Simple Binary Tree \n", root.right.data)

bt = Binarytree()

bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(6)



print("Inorder: ")
bt.inorder(bt.root)

print("\nPreorder: ")
bt.preorder(bt.root)

print("\nPostorder: ")
bt.postorder(bt.root)


