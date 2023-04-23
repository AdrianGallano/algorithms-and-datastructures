""" class Node: 
    def __init__(self, val=None, children):
        self.val = val
        self.children = children """

class Solution:
    # depth first search
    def trav(self, root):
        arr = []
        stack = []
        stack.append(root) 
        while stack:
            curr = stack.pop()
            arr.append(curr.val)
            for c in reversed(curr.children):
                stack.append(c)
        return arr





