# remove
from collections import deque
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Node({self.val})"

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def __repr__(self):
        if not self.root:
            return "Tree is empty"
        """ 
        Binary search tree - level traversal
        and x as no child
        """
        output = []
        queue = deque([self.root])
        while queue:
            item = queue.popleft()
            if not item:
                output.append("x")
                continue
            
            output.append(str(item.val))
            if item.left:
                queue.append(item.left)
            else:
                queue.append(None)
            if item.right:
                queue.append(item.right)
            else:
                queue.append(None)

        return " ".join(output)

    def insert(self, data):
        if not data:
            return False

        if not self.root:
            self.root = data
            return True
        
        current_root = self.root
        while current_root:
            if data.val < current_root.val:
                if current_root.left:
                    current_root = current_root.left
                else:
                    current_root.left = data
                    break
            elif data.val > current_root.val:
                if current_root.right:
                    current_root = current_root.right
                else:
                    current_root.right = data
                    break
            else:
                return False
        return True

    def search(self, value):
        if not self.root:
            return "Tree is empty"
        
        queue = deque([self.root])
        while queue:
            pop = queue.popleft()
            if pop.val == value:
                return pop
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)
        else:
            return False
    
    def remove(self):
        pass


if __name__ == "__main__":
    n1 = Node(20)
    n2 = Node(15)
    n3 = Node(30)
    n4 = Node(12)
    n5 = Node(18)
    n6 = Node(28)
    n7 = Node(35)
    n8 = Node(8)
    n9 = Node(7)
    b1 = BinarySearchTree(n1)
    b1.insert(n1)
    b1.insert(n2)
    b1.insert(n3)
    b1.insert(n4)
    b1.insert(n5)
    b1.insert(n6)
    b1.insert(n7)
    b1.insert(n8)
    b1.insert(n9)
    print(b1)
    print(b1.search(35))