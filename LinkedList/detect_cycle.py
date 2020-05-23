from LinkedList.singly_linkedlist import Node

def hasCycle(head):
    if not head:
        return False
    fast, slow = head.next, head
    while fast and fast.next:
        if fast is slow:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    print(f"Has Cycle: {hasCycle(node1)}")