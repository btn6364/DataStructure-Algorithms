from Recursion.prettyPrint import *

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def __str__(self):
        return binaryTreeToStr(self.root)

    def helper_insert(self, val, curNode):
        if not curNode:
            return Node(val)
        elif val < curNode.val:
            curNode.left = self.helper_insert(val, curNode.left)
        else:
            curNode.right = self.helper_insert(val, curNode.left)
        return curNode

    def insert_recursive(self, val):
        self.root = self.helper_insert(val, self.root)


if __name__ == '__main__':
    bst = BST()
    bst.insert_recursive(3)
    bst.insert_recursive(2)
    bst.insert_recursive(4)
    bst.insert_recursive(5)
    bst.insert_recursive(6)
    bst.insert_recursive(1)
    bst.insert_recursive(0)
    bst.insert_recursive(9)
    bst.insert_recursive(8)
    print(bst)

