class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

    def trav(self, root):
        if root:
            return False

        else:
            for child in self.children:
                self.trav(child)