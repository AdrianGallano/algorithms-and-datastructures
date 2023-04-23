""" 
class Node: 
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
          """
from collections import deque


class Solution:
    def trav(self, root):
        queue = deque()
        output = []

        queue.append(root)
        while queue:
            curr = queue.popleft()

            if curr:
                output.append(curr)
                queue.append(curr.left)
                queue.append(curr.right)
        return output
