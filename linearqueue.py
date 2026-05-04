class LinearQueue:
    size = 5
    queue = [None] * size
    front = -1
    rear = -1

    def enqueue(self, value):
        if self.rear == self.size - 1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = value
            print(value, "inserted")

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            value = self.queue[self.front]
            self.front += 1
            print(value, "deleted")

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
        else:
            print("Queue elements:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Example usage
q = LinearQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()
q.display()