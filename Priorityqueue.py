class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue more elements.")
            return
        
        # Store as tuple (item, priority). Higher priority number = higher priority
        new_element = (item, priority)
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = new_element
        else:
            # Insert at correct position to keep highest priority at front
            i = self.rear
            while i >= self.front and self.queue[i][1] < priority:
                self.queue[i + 1] = self.queue[i]
                i -= 1
            self.queue[i + 1] = new_element
            self.rear += 1
        
        print(f"Enqueued: {item} (Priority: {priority})")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No element to dequeue.")
            return None
        
        item = self.queue[self.front][0]
        self.front += 1
        
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
            
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[self.front][0]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        
        print("Queue (Item, Priority) - Front to Rear:")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()

# Create priority queue with capacity 6
pq = PriorityQueue(6)

pq.enqueue("Task A", 3)
pq.enqueue("Task B", 5)   # Higher priority
pq.enqueue("Task C", 1)
pq.enqueue("Task D", 5)   # Same priority as B
pq.enqueue("Task E", 4)

pq.display()

pq.dequeue()
pq.dequeue()

pq.display()

pq.enqueue("Task F", 6)   # Highest priority

pq.display()