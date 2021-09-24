class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def PreOrderTraversal(root):
    if root is None:
        return
    nodestacked = []
    nodestacked.append(root)
    while(len(nodestacked)>0):
        node = nodestacked.pop()
        print(node.data,end='->')
        if (node.right is not None):
            nodestacked.append(node.right)
        if (node.left is not None):
            nodestacked.append(node.left)
    print("Null")
root = node(10)
root.left = node(8)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(5)
root.right.left = node(2)
root.right.right=node(12)
PreOrderTraversal(root)


