class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def PostOrderTraversal(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while(stack1):
        node = stack1.pop()
        stack2.append(node)
        if (node.left):
            stack1.append(node.left)
        if (node.right):
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        print(node.data,end="->")
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
PostOrderTraversal(root)

