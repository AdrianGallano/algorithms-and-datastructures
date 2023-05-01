class UnderflowError(Exception):
    pass

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedStack:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        return "->".join([str(x.val) for x in self])

    def append(self, item):
        item.next = self.head
        self.head = item

    def pop(self):
        if not self.head:
            raise UnderflowError
      
        temp = self.head
        self.head = self.head.next
        return temp

if __name__ == "__main__":
    n1 = Node(55)
    n2 = Node(20)
    n3 = Node(100)

    l1 = LinkedStack()

    l1.append(n1)
    l1.append(n2)
    l1.append(n3)
    l1.pop()
    l1.pop()
    l1.pop()
    l1.pop() #Throws exception
    print(l1)