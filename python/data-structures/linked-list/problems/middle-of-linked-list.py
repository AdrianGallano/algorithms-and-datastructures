class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def find_middle(self):
        """ 
        return:int - return the value of the middle data 
        return the second data if there are two middle data
        """
        middle = self.head
        end = self.head

        while end != None and end.next != None:
            middle = middle.next
            end = end.next.next
        
        return middle.data

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    l1 = LinkedList(n1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    res = l1.find_middle()