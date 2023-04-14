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
        return self.head

    def remove_node(self, node):
        if node == self.head:
            self.head = node.next
            return node

        for n in self:
            prev = None
            if n == node and prev != None:
                prev.next = node.next
                return node
            prev = n
        return False

    def add_tail(self, node):
        return self.add_to_nth_node(self.__len__(), node)

    def remove_nth_node(self, nth):
        if nth >= 0 or nth <= self.__len__() - 1:
            if nth == 0:
                self.head = self.head.next
                return self.head
            else:
                prev = None
                current = self.head
                for _ in range(nth):
                    prev = current
                    current = current.next
                print(current)
                print(prev)
                prev.next = current.next
                
                return current
        else:
            raise "Out of bounds"

    def add_to_nth_node(self, nth, node):
        if self.__len__() >= nth or nth >= 0 :
            if nth == 0:
                node.next = self.head
                self.head = node
            else:
                curr = self.head.next
                prev = self.head

                for _ in range(1, nth):
                    curr = curr.next
                    prev = prev.next
                prev.next = node
                node.next = curr

            return self.head
        else:
            raise "Out of bounds"

if __name__ == "__main__":
    n1 = Node(55)
    n2 = Node(20)
    n3 = Node(100)

    l1 = LinkedList()
    l1.head = n1
    n1.next = n2
    n2.next = n3

    print(f"Linked List head: {l1.head}")
    print("length:", len(l1))
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

    l1.add_to_nth_node(1, Node(16))
    print(f"after adding to 1", Node(16))
    print(l1)
    print()

    l1.add_to_nth_node(0, Node(80))
    print(f"after adding to 0", Node(80))
    print(l1)
    print()

    l1.add_to_nth_node(4, Node(250))
    print(f"after adding to 4", Node(250))
    print(l1)
    print()

    l1.remove_nth_node(len(l1) - 1)
    print(f"after removing 1st node")
    print(l1)
    print()