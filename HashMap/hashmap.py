"""
Hash Map API

Use Seperate Chaining to handle collisions.

"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class SeparateChainingHashMap:
    #initializes HashMap
    def __init__(self, capacity):
        self.map = [Node("dummy", "dummy") for _ in range(capacity)]
        self.capacity = capacity

    #returns index that key is stored
    def hashedIndex(self, key):
        return key % self.capacity

    #adds an item to the hash map. uses separate chaining for collisions
    def put(self, key, val):
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while cur.next:
            cur = cur.next
        cur.next = Node(key, val)

    #finds item with given key and returns associated val
    def get(self, key):
        idx = self.hashedIndex(key)
        cur = self.map[idx].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return None

    #deletes a key and its val from the hashmap
    def delete(self, key):
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


    #overrides toString method for debugging
    def __str__(self):
        out = ""
        for idx in range(len(self.map)):
            out += "Index " + str(idx) + ":"
            cur = self.map[idx].next
            while cur:
                out += str(cur.val) + " "
                cur = cur.next
            out += "\n"
        return out


if __name__ == '__main__':
    #test cases
    map = SeparateChainingHashMap(5)
    for i in range(18):
        map.put(i,i * 2)
    #0 6
    #2 8
    #4
    print(map)
    print(f"value at with key 4: {map.get(4)}")
    for i in range(3):
        map.delete(i)

    print("Map after removing 0, 1, 2 key")
    print(map)