class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self, head):
        self.head = head

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            print(slow, fast)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("met at", slow, fast)
                slow = self.head
                while(slow != fast):
                    print("recycle", slow, fast)
                    slow = slow.next
                    fast = fast.next
                return "result is", slow
        return None




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
    n10 = Node(10)

    l1 = LinkedList(n1)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9
    n9.next = n10
    n10.next = n5

    result = l1.detect_cycle()
    print(result)