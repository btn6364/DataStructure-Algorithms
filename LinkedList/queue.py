from LinkedList.singly_linkedlist import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        cur = self.head
        out = "|"
        while cur:
            out += str(cur.val) + "|"
            cur = cur.next
        return out

    def enqueue(self, val):
        node = Node(val)
        if not self.tail:
            self.tail = node
            self.head = self.tail
            return
        self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Dequeue from an empty queue")
        removed = self.head.val
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return removed

    def isEmpty(self):
        return self.size == 0

if __name__ == "__main__":
    queue = Queue()
    for i in range(5):
        queue.enqueue(i)
    print(f"Queue: {queue}")
    while not queue.isEmpty():
        print(queue.dequeue())
    try:
        print(queue.dequeue())
    except Exception as e:
        print(f"Exception: {e}")
