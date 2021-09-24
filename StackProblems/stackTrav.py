def stackTraversal():
    size = int(input("enter the size of the stack"))
    stack1 = list()
    for i in range(size):
        data = int(input("enter the data for the stack"))
        stack1.append(data)
    for i in range(size):
        print(stack1.pop(),end=" ")
stackTraversal()

#Implementation of the stack using Queue as data structure
from queue import LifoQueue
stack2 = LifoQueue(maxsize=5)
stack2.put(1)
stack2.put(2)
stack2.put(3)
stack2.put(4)
stack2.put(5)
print("checking whether the stack is full or not")
print(stack2.full())
print("getting the stack element from the ")
print(stack2.get())


