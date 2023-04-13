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
            yield current.data
            current = current.next
        return True

    def __repr__(self):
        """
        return a string representation of the object (LinkedList) 
        """

        arr = []
        for i in self:
            arr.append(str(i))
        return "->".join(arr)


if __name__ == "__main__":
    n1 = Node(55)
    n2 = Node(20)
    n3 = Node(100)

    l1 = LinkedList()
    l1.head = n1
    n1.next = n2
    n2.next = n3

    print(f"Linked List head: {l1.head}")

    print(n1)
    print(n2)
    print(n3)
    print(l1)
