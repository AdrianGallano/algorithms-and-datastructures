""" 
class Node: 
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
          """

class Solution:
    def trav(self, root):
        if not root: return []
        output = []
        stack = [root]

        while stack:
            popped = stack.pop()
            output.append(popped)
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
        return output[::-1]
