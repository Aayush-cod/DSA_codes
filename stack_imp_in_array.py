# Stack implementation using Python list (array)

class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, item):
        # Add (push) an element to the top of the stack
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        # Remove (pop) the top element from the stack
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.stack.pop()

    def peek(self):
        # View the top element without removing it
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.stack[-1]

    def display(self):
        # Display all elements in the stack
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements:", self.stack)


# ----------- Testing the Stack -----------

# Create a stack object
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Display stack
s.display()

# Peek top element
print("Top element:", s.peek())

# Pop element
print("Popped element:", s.pop())

# Display stack after pop
s.display()