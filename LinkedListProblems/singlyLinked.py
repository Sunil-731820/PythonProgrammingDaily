'''WAP to insert the node in the singly LinkedList'''
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    #pushing the node at the begginning of the node in the linkedlist
    def push(self,new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    #inserting the node at the anywhere in the linkedlist
    def insert(self,prev_node,new_data):
        if (prev_node is None):
            return
        else:
            new_node = node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
    #appending the node at the end of the linkedlist
    def append(self,new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next =new_node
    #displaying the singly linkedlist
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end='->')
            temp = temp.next
        print("NULL")
if __name__=="__main__":
    llist = Linkedlist()
    llist.push(12)
    llist.push(20)
    llist.push(30)
    llist.printlist()
    llist.insert(llist.head,122)
    llist.insert(llist.head.next,323)
    llist.insert(llist.head.next,878)
    print("after inserting the new node the output will be")
    llist.printlist()
    llist.append(2000)
    print("after appending the data at the end of the singly linkedlist is ")
    llist.printlist()
