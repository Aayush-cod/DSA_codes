class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        newnode.next = self.head
        temp.next = newnode
        self.head = newnode

    def insert_at_end(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp= temp.next

        temp.next = newnode
        newnode.next = self.head

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            deleted = self.head.data
            self.head = None
            print(f"Deleted at beginning: {deleted}")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        deleted = self.head.data
        temp.next = self.head.next
        self.head = self.head.next
        print(f"Delete at beg: {deleted}")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            deleted = self.head.data
            self.head = None
            print(f"Deleted at end: {deleted}")
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        deleted = temp.next.data

        temp.next = self.head
        print(f"Deleted at end: {deleted}")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cl = Circular_linked_list()
cl.insert_at_beginning(10)
cl.insert_at_beginning(20)
cl.insert_at_end(30)

cl.display()
cl.delete_at_beginning()
cl.delete_at_end()
cl.display()
