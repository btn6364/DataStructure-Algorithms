class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        out = "(" + str(self.key) + " -> " + str(self.val) + ")"
        return out

class DoublyLinkedList:
    def __init__(self):
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        out = ""
        cur = self.head
        while cur != self.tail:
            out += cur.__str__() + " <-> "
            cur = cur.next
        return out + self.tail.__str__()

    def addToHead(self, node):
        #head <-> tail
        # head <-> 1 <-> tail
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def updateHead(self, node):
        if self.head.next is node:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.addToHead(node)

    def removeTail(self):
        if self.head.next is self.tail:
            raise Exception("[ERROR]: Trying to remove from an empty linked list")
        removedNode = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next.next = None
        self.tail.prev.next.prev = None
        self.tail.prev.next = self.tail
        return removedNode

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.nodes = DoublyLinkedList()
        self.size = 0

    def __str__(self):
        out = "Cache: \n"
        out += "{"
        for key in self.cache:
            out += str(key) + " -> " + self.cache[key].__str__() + ", "
        out += "}"
        out += "\n"
        out += self.nodes.__str__()
        return out

    def get(self, key):
        if key not in self.cache:
            return None
        node = self.cache[key]
        #update the node to be the head of the linked list
        self.nodes.updateHead(node)
        return node.val

    def put(self, key, val):
        # if the key is already in the cache
        if key in self.cache:
            #update the cache and the nodes
            self.cache[key].val = val
            node = self.cache[key]
            self.nodes.updateHead(node)
        # if the cache is not full
        elif self.size != self.capacity:
            node = Node(key, val)
            self.cache[key] = node
            self.nodes.addToHead(node)
            self.size += 1
        else:
            # if the cache is full
            #remove the node from the nodes and the cache
            removedNode = self.nodes.removeTail()
            del self.cache[removedNode.key]
            #add new node into the cache and the linked list
            node = Node(key, val)
            self.cache[key] = node
            self.nodes.addToHead(node)

if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(2, 2)
    cache.put(1, 1)
    print(cache, end="\n\n")

    #update key 2
    cache.put(2, 1)
    print(cache, end="\n\n")

    #put key 3
    cache.put(3, 3)
    print(cache, end="\n\n")

    #get key 2
    print(f"value at key 2: {cache.get(2)}", end="\n\n")
    print(cache, end="\n\n")

    #put key 4 - evicts key 1
    cache.put(4, 10)
    print(cache)