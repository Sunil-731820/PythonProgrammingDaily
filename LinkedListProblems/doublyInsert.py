class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    def printlist(self,node):
        node = self.head
        #linking the linkedlist in the forward direction only
        while(node):
            print(node.data,end='->')
            last = node
            node = node.next
        print("Null")
        print("\n")

        #reversing the doubly linkedlist
        while(last):
            #print("NULL\t")
            print(last.data,end="<-")
            last = last.prev
        #print("Null")

llist = LinkedList()
llist.append(12)
llist.append(23)
llist.append(35)
llist.printlist(llist.head)


