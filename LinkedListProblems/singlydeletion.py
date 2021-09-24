'''Wap to delete the node from the linkedlist'''
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self,new_data):
        new_node = node(new_data)
        if (self.head is None):
            self.head = new_node
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = new_node
    #deleting the node from the linkedlist
    def deleteingNode(self,new_data):
        temp = self.head
        if (temp is None):
            return
        else:
            if (temp is not None):
                if temp.data==new_data:
                    self.head=temp.next
                    temp = None
                    return
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ->")
            temp = temp.next
        print("Null")
if __name__=="__main__":
    llist = linkedlist()
    llist.append(12)
    llist.printlist()
    print("again appending the node at the end of the node ")
    llist.append(15)
    llist.printlist()
    llist.deleteingNode(12)
    print("after deleting the node from the singly linkedlist")
    llist.printlist()
    llist.deleteingNode(15)
    print("again deleting the node from the list is")
    llist.printlist()
    llist.append(121)
    llist.printlist()