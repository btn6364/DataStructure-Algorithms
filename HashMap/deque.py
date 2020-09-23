class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    #Initialize Deque
    def __init__(self):
        #head <-> tail
        self.size = 0
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    # Return Type: List
    # Description: construct a List holding all of the items in the deque from front to end and return it
    def __str__(self):
        out = ""
        cur = self.head
        while cur != self.tail:
            if cur.next.prev != cur:
                raise Exception("[ERROR]: Broken deque...")
            out += str(cur.val) + " <-> "
            cur = cur.next
        return out + "tail"

    # Return Type: Boolean
    # Description: Return True if the deque is empty, else False
    def isEmpty(self):
        return self.size == 0

    # Return Type: int
    # Description: Return the number of items in the deque
    def getSize(self):
        return self.size

    # Return Type: None
    # Description: Insert item to the front of the deque
    def addFirst(self, item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 2 <-> 1 <-> tail
        node = Node(item)
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        self.size += 1

    # Return Type: None
    # Description: Insert item to the end of the deque
    def addLast(self, item):
        # head <-> tail
        # head <-> 1 <-> tail
        # head <-> 1 <-> 2 <-> tail
        node = Node(item)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    # Return Type: Object
    # Description: Delete and return the item at the front of the deque
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Removing from an empty deque...")
        removed = self.head.next.val
        # head <-> 2  1 <-> tail
        # head <-> 1 <-> tail
        self.head.next = self.head.next.next
        self.head.next.prev.prev = None
        self.head.next.prev.next = None
        self.head.next.prev = self.head
        self.size -= 1
        return removed

    # Return Type: Object
    # #Description: Delete and return the item at the end of the deque
    def removeLast(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Removing from an empty deque...")
        removed = self.tail.prev.val
        # head <-> 2  1 <-> tail
        # head <-> 1 <-> tail
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next.next = None
        self.tail.prev.next.prev = None
        self.tail.prev.next = self.tail
        self.size -= 1
        return removed


if __name__ == '__main__':
    #test cases
    deque = Deque()
    for i in range(1,6):
        deque.addFirst(i)
    for i in range(6,11):
        deque.addLast(i)
    print(deque)
    firstRemoved = deque.removeFirst()
    print(f"Removed first: {firstRemoved}")
    secondRemoved = deque.removeFirst()
    print(f"Removed second: {secondRemoved}")
    thirdRemoved = deque.removeLast()
    print(f"Removed third: {thirdRemoved}")
    fourthRemoved = deque.removeLast()
    print(f"Removed fourth: {fourthRemoved}")
    print(deque)