class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        #O(N) runtime | O(N) space
        cur = self.head
        out = "|"
        while cur:
            out += str(cur.val) + "|"
            cur = cur.next
        return out

    def insertFront(self, item):
        #O(1) runtime | O(1) space
        node = Node(item)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1

    def insertLast(self, item):
        #O(N) runtime | O(1) space
        node = Node(item)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        self.size += 1

    def removeBeginning(self):
        #O(1) runtime | O(1) space
        if not self.head:
            raise Exception("remove from an empty linked list")
        self.head = self.head.next
        self.size -= 1

    def size(self):
        #O(1) runtime | O(1) space
        return self.size

if __name__ == '__main__':
    linkedList1 = SinglyLinkedList()
    for i in range(1,6):
        linkedList1.insertFront(i)
    #should print 5 | 4 | 3 | 2 | 1|
    print(f"LinkedList1: {linkedList1}")
    linkedList2 = SinglyLinkedList()
    for i in range(1, 6):
        linkedList2.insertLast(i)
    # should print | 1 | 2 | 3 | 4 | 5 |
    print(linkedList2)
    linkedList2.removeBeginning()
    linkedList2.removeBeginning()
    #should print 3,4,5
    print(f"LinkedList2: {linkedList2}")
    for i in range(6,11):
        linkedList2.insertLast(i)
    #should print 3,4,5,6,7,8,9,10
    print(f"LinkedList2: {linkedList2}")