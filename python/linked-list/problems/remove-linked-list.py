class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node(Data: {self.data} Pointer: {self.next})"

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def __repr__(self):
        datalist = []
        current = self.head
        while current:
            datalist.append(str(current.data))
            current = current.next
        return "->".join(datalist)
    
    def remove(self, n):
        """ 
        return: int - returns the value that has been remove  
        None if value does not exist
          """
        prev = None
        current = self.head
        temp = None
        while current:
            if current.data == n:
                if prev == None:
                    self.head = current.next
                else:
                    prev.next = current.next
                    temp = current
                    current = None
                    return temp.data
                
            prev = current
            current = current.next
        return None

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

    res = l1.remove(3)
    print(l1)
    print(res)


