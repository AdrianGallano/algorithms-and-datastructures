# remove
from collections import deque
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.parent = None
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

    def __reassign_node(self, node: Node | None, cnode: Node | None):
        if cnode:
            cnode.parent = node.parent
        if  node.parent:
            if self.is_right(node):
                node.parent.right = cnode
            else:
                node.parent.left = cnode
        else:
            self.root = None

    def is_right(self, node):
        if node.parent.right == node:
            return True
        return False
    
    def get_min(self, root = None):
        if root == None:
            if self.root == None:
                return None
            root = self.root 
        while root.left:
            root = root.left
        return root

    def get_max(self, root = None):
        if root == None:
            if self.root == None:
                return None
            root = self.root
        while root.right:
            root = root.right
        return root

    def insert(self, data):
        if not data:
            return False

        if not self.root:
            self.root = data
            return True
        parent = None
        current_root = self.root
        while current_root:
            if data.val < current_root.val:
                if current_root.left:
                    current_root = current_root.left
                else:
                    current_root.left = data
                    data.parent = parent
                    break
            elif data.val > current_root.val:
                if current_root.right:
                    current_root = current_root.right
                else:
                    current_root.right = data
                    data.parent = parent
                    break
            else:
                return False
            parent = current_root
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
    
    def remove(self, value):
        node = self.search(value)
        if not node:
            return "Node doesn't exist"
        if not node.left and not node.right:
            self.__reassign_node(node, None)
        elif not node.right:
            self.__reassign_node(node, node.left)
        elif not node.left:
            self.__reassign_node(node, node.right)
        else: # hard part
            new_node = self.get_max(node.left)
            self.remove(new_node.val)
            node.val = new_node.val
        return True

    def level_traversal(self):
        if not self.root: return "Tree is empty"
        queue = deque([self.root])
        output = []

        while queue:
            pop = queue.popleft()
            output.append(pop.val)
            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)
        return output

    def preorder_traversal(self):
        if not self.root: return "Tree is empty"
        stack = [self.root]
        output = []
        while stack:
            pop = stack.pop()
            output.append(pop.val)

            if pop.right:
                stack.append(pop.right)
            if pop.left:
                stack.append(pop.left)
        return output

    def inorder_traversal(self):
        if not self.root: return "Tree is empty"
        stack = []
        output = []
        root = self.root
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                pop = stack.pop()
                output.append(pop.val)
                root = pop.right
        return output

    def postorder_traversal(self):
        if not self.root: return "Tree is empty"
        stack = [self.root]
        output = []
        while stack:
            pop = stack.pop()
            output.append(pop.val)

            if pop.left:
                stack.append(pop.left)
            if pop.right:
                stack.append(pop.right)
        return output[::-1]

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
    print(b1.level_traversal())
    print(b1.preorder_traversal())
    print(b1.inorder_traversal())
    print(b1.postorder_traversal())