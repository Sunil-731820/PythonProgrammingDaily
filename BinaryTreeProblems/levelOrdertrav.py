class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printLevelOrder(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        count = len(q)
        if count>0:
            temp = q.pop(0)
            print(temp.data,end= " ")
            if temp.left :
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        count = count-1
    print(' ')
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.right = Node(50)
printLevelOrder(root)

