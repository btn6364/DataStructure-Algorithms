"""
- Implement a trie data structure.
"""

class Node:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    #O(M) runtime | O(1) space.
    def insert(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = Node()

            # Update the current node to the children node
            curNode = curNode.children[letter]
        curNode.isEndOfWord = True

    #O(M) runtime | O(1) space.
    def search(self, word):
        curNode = self.root
        for letter in word:
            if letter not in curNode.children:
                return False
            curNode = curNode.children[letter]
        return curNode.isEndOfWord

def test():
    trie = Trie()
    words = ["dog", "duck", "dad", "dude"]
    for word in words:
        trie.insert(word)

    print(f"Searching for 'dog': {trie.search('dog')}")
    print(f"Searching for 'duck': {trie.search('duck')}")
    print(f"Searching for 'dad': {trie.search('dad')}")
    print(f"Searching for 'dude': {trie.search('dude')}")
    print(f"Searching for 'daddy': {trie.search('daddy')}")
    print(f"Searching for 'dud': {trie.search('dud')}")

if __name__ == '__main__':
    test()

