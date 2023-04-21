""" class Node: 
    def __init__(self, val=None, children):
        self.val = val
        self.children = children """

class Solution:
    def main(self, root):
        return self.trav(root, [])
    
    def trav(self, root, l):
        if root == None:
            return False

        else:
            l.append(root.val)
            for child in root.children:
                self.trav(child, l)
            return l