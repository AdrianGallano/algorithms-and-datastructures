class Node:
    def __init__(self, val = 0):
        self.val = val
        self.right: Node | None
        self.left: Node | None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self): # inorder traversal
        if not self.root: return "No tree"

        rep = []
        stack = []
        curr = self.root
        while curr or stack: 
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                popped = stack.pop()
                rep.append(popped)
                curr = popped.right
        return " ".join(rep)