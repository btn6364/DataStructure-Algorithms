"""

    p    c    n
 <- 1    2 -> 3 -> 4 -> None

n = c.next
c.next = p
p = c
c = n


"""
from LinkedList.singly_linkedlist import SinglyLinkedList

def reverse(linkedlist):
    prev, cur = None, linkedlist.head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    linkedlist.head = prev


if __name__ == '__main__':
    singlyLinkedList1 = SinglyLinkedList()
    singlyLinkedList2 = SinglyLinkedList()
    # edge case 1: linked list is empty
    reverse(singlyLinkedList1)
    print(f"LinkedList1 after reversed: {singlyLinkedList1}")
    for i in range(1, 6):
        singlyLinkedList2.insertLast(i)
    print(f"LinkedList2 before reversed: {singlyLinkedList2}")
    reverse(singlyLinkedList2)
    print(f"LinkedList2 after reversed: {singlyLinkedList2}")
