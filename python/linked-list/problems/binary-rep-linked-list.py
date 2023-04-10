class Node:
    def __init__(self, data):
        assert data == 1 or data == 0, "Can only accept 1s and 0s"
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def find_int_in_binary(self):
        """ 
        return:int - find the integer representation of a binary linked list  
        """
        num = self.head.data
        while(self.head.next):
            num = num << 1 | self.head.next.data
            self.head = self.head.next
        return num


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(0)
    n3 = Node(1)
    n4 = Node(1)
    n5 = Node(1)

    l1 = LinkedList(n1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    res = l1.find_int_in_binary() # returns 23