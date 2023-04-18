class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({str(self.data)})"


class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None

    def __iter__(self):
        current = self.front
        while current:
            yield current
            current = current.next
        return True

    def __repr__(self):
        return "->".join(str(x.data )for x in self)
    
    def put(self, node):
        if self.front == None:
            self.front = self.back = node
        else:
            self.back.next = node
            self.back = node
        return self.front

    def get(self):
        if self.front == None:
            raise OverflowError
        else:
            current = self.front
            self.front = self.front.next 
            return current

    def peek(self):
        return str(self.front)
    
    def rotate(self):
        current = self.front
        prev = None
        self.back = self.front
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.front = prev
        return prev

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = None

    l1 = LinkedList()
    l1.put(n1)
    l1.put(n2)
    l1.put(n3)
    print(l1)
    r = l1.get()
    print(l1)
    r1 = l1.get()
    print(l1)
    l1.put(n4)
    l1.put(n5)
    print(l1)
    l1.rotate()
    print(l1)