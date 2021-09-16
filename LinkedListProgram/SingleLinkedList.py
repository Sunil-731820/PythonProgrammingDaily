''''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")       
            temp= temp.next
        print(end="NULL")
if __name__=="__main__":
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    llist.head.next=second
    second.next = third
    third.next = fourth
    llist.printlist()
'''
'''class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insertAtBeggining(self):
        pass
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
        print(end="Null")
if __name__=="__main__":
    #size = int(input("enter the size of the linkedlist"))
    # list1 = list()
    # for i in range(size):
    #     data = int(input("enter the size for the linkedlist"))
    #     list1.append(data)
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(10)
    llist.head.next= second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    llist.printlist()
'''
'''WAP to insert the element the node at the beggining in the linkedlist
 , in the middle anywhere and at the end of the list'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
        print(end="NULL")
    #inserting the element at the beggining of the node in the linkedlist
    def pushAtbeg(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    #inserting the node in the middle of the in the linkedlist
    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print("the previous node must initialised")
            return
        else:
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
    #inserting the node at the end of the linkedlist
    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

                

if __name__=="__main__":
    llist = linkedlist()
    llist.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    fifth = Node(50)
    llist.head.next = second
    second.next = third
    third.next = fourth 
    fourth.next = fifth
    llist.printlist()
    print("after the inserting the element at the begging of the linkedlist")
    llist.pushAtbeg(30)
    llist.printlist()
    print("again inserting the node at the begginnig of the linedklist")
    llist.pushAtbeg(90)
    llist.printlist()
    print("after inserting the element at the middle of the linkedlist")
    llist.insertafter(second.next,70)
    llist.printlist()
    print("inserting the new node at the end of the linekdlist")
    llist.insertAtEnd(500)
    llist.printlist()



