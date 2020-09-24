from LinkedList.singly_linkedlist import Node

class Stack:
    # creates an empty Stack
    def __init__(self):
        self.head = None
        self.size = 0

    #prints out stack in order
    def __str__(self):
        cur = self.head
        out = "|"
        while cur:
            out += str(cur.val) + "|"
            cur = cur.next
        return out

    # adds an item to the top stack
    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    # removes and returns the most recently added item
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        removed = self.head.val
        self.head = self.head.next
        return removed

    # Returns a boolean indicating if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # returns the number of items in the stack
    def size(self):
        return self.size

if __name__ == '__main__':
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack) # 4, 3, 2, 1, 0

    for _ in range(3):
        #should print 4,3,2
        print(stack.pop())

    for i in range(5,10):
        stack.push(i)
    #9,8..5, 1,0
    print(stack)