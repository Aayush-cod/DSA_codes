class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    # ✅ Insert at Beginning
    def insert_at_beginning(self, data):
        newnode = Node(data)

        if self.head is None:
            newnode.next = newnode
            newnode.prev = newnode
            self.head = newnode
            return

        last = self.head.prev

        newnode.next = self.head
        newnode.prev = last

        last.next = newnode
        self.head.prev = newnode

        self.head = newnode

    # ✅ Insert at End
    def insert_at_end(self, data):
        newnode = Node(data)

        if self.head is None:
            newnode.next = newnode
            newnode.prev = newnode
            self.head = newnode
            return

        last = self.head.prev

        newnode.next = self.head
        newnode.prev = last

        last.next = newnode
        self.head.prev = newnode

    # ✅ Delete from Beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            deleted = self.head.data
            self.head = None
            print(f"Deleted: {deleted}")
            return

        last = self.head.prev
        deleted = self.head.data

        self.head = self.head.next
        self.head.prev = last
        last.next = self.head

        print(f"Deleted: {deleted}")

    # ✅ Delete from End
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            deleted = self.head.data
            self.head = None
            print(f"Deleted: {deleted}")
            return

        last = self.head.prev
        second_last = last.prev
        deleted = last.data

        second_last.next = self.head
        self.head.prev = second_last

        print(f"Deleted: {deleted}")

    # ✅ Display Forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # ✅ Display Backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head.prev  # start from last
        start = temp
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev
            if temp == start:
                break
        print("(back to last)")


dll = DoublyCircularLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)

dll.display_forward()
dll.display_backward()

dll.delete_from_beginning()
dll.display_forward()

dll.delete_from_end()
dll.display_forward()