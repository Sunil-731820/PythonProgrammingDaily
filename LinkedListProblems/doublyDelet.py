import gc
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoublylinList:
    def __init__(self):
        self.head = None

    #adding the node at the end of the linkedlist
    def append(self,new_data):
        new_node = Node(new_data)
        if (self.head is None):
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
    #printing the doubly linkedlist
    def printlist(self,node):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
            last = node
            node = node.next
        print("NULL")
    #deleting the node from the linkedlist
    def deleting(self,delnode):
        temp1 = self.head
        if(self.head is None):
            print("the node not found")
            return
        if self.head==delnode:
            self.head = delnode.next
        if  delnode.next is not None:
            delnode.next.prev = delnode.prev
        if delnode.prev is not None:
            delnode.prev.next = delnode.next
        gc.collect()
if __name__=="__main__":
    llist = DoublylinList()
    llist.append(12)
    llist.append(23)
    llist.append(34)
    llist.printlist(llist.head)
    llist.append(45)
    print("again appending then after this the doubly linkedlist will be ")
    llist.printlist(llist.head)
    llist.deleting(llist.head)
    llist.printlist(llist.head)
    llist.deleting(llist.head.next)
    llist.printlist(llist.head)




