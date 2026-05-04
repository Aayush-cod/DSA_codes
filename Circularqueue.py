class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue more elements.")
            return
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No element to dequeue.")
            return None
        
        item = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
            
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        
        print("Queue elements (Front to Rear): ", end="")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


# Create a circular queue with capacity 5
q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

q.dequeue()
q.dequeue()

q.display()

# After dequeue, space is reused due to circular nature
q.enqueue(60)
q.enqueue(70)

q.display()

print("Front element:", q.peek())