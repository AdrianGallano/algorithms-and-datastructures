from collections import deque
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val})"

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self): # inorder traversal
        if not self.root: return "No tree"

        rep = []
        queue = deque([self.root])
        
        while queue:
            popped = queue.popleft()

            
            if not popped:
                rep.append("x") # represents a non child
                continue

            rep.append(str(popped.val))
            if popped.left:
                queue.append(popped.left)
            else:
                queue.append(None)

            if popped.right:
                queue.append(popped.right)
            else:
                queue.append(None)


        return " ".join(rep)
    

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    b1 = BinaryTree(n1)

    n1.right = n2
    n1.left = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n5.left = n10
    print(b1)
    """ 
            1
        3   |   2
      6   7 | 4    5
     x x x x 8 9 10
    """