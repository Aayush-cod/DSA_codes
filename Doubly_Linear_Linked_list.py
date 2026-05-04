class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None


class Double_linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beginnig(self,data):
        newnode = Node(data)

        if self.head is not None:
            self.head.prev = newnode
            newnode.next = self.head


        self.head = newnode


    def insert_at_end(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp


    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")

            return
        
        deleted = self.head.data

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

        print(f"Deleted from beginning: {deleted}")

    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")

            return
        
        

        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(f"Deleted at end: {deleted}")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        deleted = temp.data
        temp.prev.next = None
        print(f"Deleted at end: {deleted}")



    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = "-> ")
            temp = temp.next
        print("None")



dli = Double_linked_List()

dli.insert_at_beginnig(10)
dli.insert_at_beginnig(20)
dli.insert_at_beginnig(25)
dli.insert_at_end(30)

dli.display()

dli.delete_at_beginning()
dli.delete_at_end()

dli.display()




