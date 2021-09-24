class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def InorderTraversal(root):
    if root is None:
        return
    nodestacked = []
    current = root
    done = 0
    while True:
        if current is not None:
            nodestacked.append(current)
            current = current.left
        elif nodestacked:
            current = nodestacked.pop()
            print(current.data,end='->')
            current = current.right
        else:
            break
    print("Null")


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
InorderTraversal(root)