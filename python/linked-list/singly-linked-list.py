class Node:
    """ 
    blueprint for a single node
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({(self.data)})"


class LinkedList:
    """ 
    blueprint for a single node
    """

    def __init__(self):
        self.head = None

    def __iter__(self):
        # what do we want to return?
        # say we have this node(1) -> node(2)
        # how do we iterate
        current = self.head
        while (current):
            yield current
            current = current.next
        return True

    def __repr__(self):
        """
        return a string representation of the object (LinkedList) 
        """
        return "->".join(str(item.data) for item in self)

    def __len__(self):
        """
        return the len of a linked list
        """
        return len([str(item.data) for item in self])

    def add_head(self, node):
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def remove_node(self, node):
        prev = None
        if node == self.head:
            self.head = node.next
            return True

        for n in self:
            if n == node and prev != None:
                prev.next = node.next
                return True
            prev = n
        return False
    
    # def add_to_nth_node(self, nth, node):

if __name__ == "__main__":
    n1 = Node(55)
    n2 = Node(20)
    n3 = Node(100)

    l1 = LinkedList()
    l1.head = n1
    n1.next = n2
    n2.next = n3

    print(f"Linked List head: {l1.head}")
    print("length:",len(l1))
    print()

    print("before removing", l1)
    l1.remove_node(n1)
    print("after removing", l1)
    print()
    
    print("before adding", l1)
    l1.add_head(Node(1))
    print("after adding", l1)
    print()

    print("before removing", l1)
    l1.remove_node(n2)
    print("after removing", l1)
    print()