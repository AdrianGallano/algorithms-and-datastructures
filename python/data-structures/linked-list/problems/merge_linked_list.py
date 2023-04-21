class Node:
    def __init__(self, data = 0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    def __init__(self, head):
        self.head = head


    def __iter__(self):
        current = self.head
        while(current):
            yield current.data
            current = current.next
        return True

    def __repr__(self):
        return "->".join(str(data) for data in self)


def mergeTwoLists(list1, list2):
    # iterate to this to list head 
    # 1 2 3 - 1 2 4
    # should result into 1 1 2 2 3 4
    # so my solution is 
    # if l1 > l2 make that first one as the head
    # then trav1 = trav1.next 
    # or smthn like that
    new_head = trav = Node()

    while(list1 and list2):
        if list1.data <= list2.data:
            trav.next = list1
            list1 = list1.next
            trav = trav.next
        else:
            trav.next = list2
            list2 = list2.next
            trav = trav.next

    if list1 or list2:
        trav.next = list1 if list1 else list2
    return new_head.next




if __name__ == "__main__":
    n0 = Node(1)
    n1 = Node(2)
    n2 = Node(3)

    n3 = Node(1)
    n4 = Node(2)
    n5 = Node(4)

    l1 = LinkedList(n0)
    n0.next = n1
    n1.next = n2
    n2.next = None

    l2 = LinkedList(n3)
    n3.next = n4
    n4.next = n5
    n5.next = None

    rs = mergeTwoLists(l1.head, l2.head)
