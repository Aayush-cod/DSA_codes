
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        
        self.head = None

    def insert_at_begining(self,data):
        newnode = Node(data)
        newnode.next = self.head

        self.head = newnode

    def insert_at_end(self,data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    def delete_from_begining(self):
        if self.head is None:
            print("List is empty")

        deleted = self.head.data
        self.head = self.head.next
        print(f"Deleted value beginning : ", {deleted})
        

        
        
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            print(f"Deleted value end one data : {deleted} ")
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next

        delete = temp.next.data
        temp.next = None
        print(f"Deleted from end: {delete}")



    def display(self):

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = linked_list()
ll.insert_at_begining(10)
ll.insert_at_begining(20)
ll.insert_at_begining(25)
ll.insert_at_end(30)



ll.display()

ll.delete_from_begining()
ll.delete_from_end()


