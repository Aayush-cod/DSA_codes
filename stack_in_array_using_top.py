class Stack:
    def __init__(self, size):
        # Maximum size of stack
        self.size = size
        
        # Create a fixed-size array (list filled with None)
        self.stack = [None] * size
        
        # Top pointer (initially -1 means stack is empty)
        self.top = -1

    def is_empty(self):
        # Stack is empty when top = -1
        return self.top == -1

    def is_full(self):
        # Stack is full when top reaches last index
        return self.top == self.size - 1

    def push(self, item):
        # Check overflow condition
        if self.is_full():
            print("Stack Overflow! Cannot push.")
            return
        
        # Move top pointer up
        self.top += 1
        
        # Insert element at top position
        self.stack[self.top] = item
        
        print(f"{item} pushed to stack")

    def pop(self):
        # Check underflow condition
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return None
        
        # Get top element
        item = self.stack[self.top]
        
        # Remove element (optional: set to None)
        self.stack[self.top] = None
        
        # Move top pointer down
        self.top -= 1
        
        return item

    def peek(self):
        # View top element
        if self.is_empty():
            print("Stack is empty!")
            return None
        
        return self.stack[self.top]

    def display(self):
        # Show stack elements
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack elements:", self.stack[:self.top + 1])


# -------- Testing --------

s = Stack(5)   # stack of size 5

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

print("Top element:", s.peek())

print("Stack isfull: ", s.is_full())

print("Popped:", s.pop())



s.display()