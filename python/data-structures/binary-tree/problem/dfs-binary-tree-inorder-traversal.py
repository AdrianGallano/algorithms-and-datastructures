""" 
class Node: 
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
          """

class Solution:
    def trav(self, root):
        output = []
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                popped = stack.pop()
                output.append(popped)
                root = popped.right
        return output
