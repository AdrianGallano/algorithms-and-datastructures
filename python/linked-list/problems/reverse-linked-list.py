class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def __repr__(self):
      datalist = []
      while(self.head):
        datalist.append(str(self.head.data))
        self.head = self.head.next

      return "->".join(datalist)

    def reverse_linked_list(self):
        prev = None
        while(self.head): # 1->2->3->4->5->None 
            nextData = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nextData
        return prev

    
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

    l1.head = l1.reverse_linked_list()

    print(l1)

    while(l1.head):
        print(l1.head.data)
        l1.head = l1.head.next