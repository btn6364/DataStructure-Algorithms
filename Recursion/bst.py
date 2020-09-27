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

    #INSERTION: O(h) runtime | O(h) space.
    def _insert(self, value, cur_node):
        if not cur_node:
            return Node(value)
        elif cur_node.val < value:
            cur_node.right = self._insert(value, cur_node.right)
        else:
            cur_node.left = self._insert(value, cur_node.left)
        return cur_node

    def insert(self, value):
        self.root = self._insert(value, self.root)

    #SEARCHING: O(h) runtime | O(h) space.
    def _search(self, value, cur_node):
        if not cur_node:
            return False
        if cur_node.val == value:
            return True
        elif cur_node.val < value:
            return self._search(value, cur_node.right)
        else:
            return self._search(value, cur_node.left)

    def search(self, value):
        return self._search(value, self.root)

    #DELETION: O(h) runtime | O(h) space.

    def findSmallestAndDelete(self, cur_node, prev_node):
        while cur_node.left:
            prev_node = cur_node
            cur_node = cur_node.left
        if prev_node.left is cur_node:
            prev_node.left = cur_node.right
        else:
            prev_node.right = cur_node.right
        return cur_node

    def _delete(self, value, cur_node):
        #Base case
        if not cur_node:
            return None
        elif cur_node.val > value:
            #Value belongs to the left
            cur_node.left = self._delete(value, cur_node.left)
        elif cur_node.val < value:
            cur_node.right = self._delete(value, cur_node.right)
        else: #Found the value, remove it from the tree.
            #Case 1: if the tree has no left and right children
            if not cur_node.left and not cur_node.right:
                return None
            elif cur_node.left and cur_node.right:
                #find the smallest element in the right subtree and remove it.
                smallest = self.findSmallestAndDelete(cur_node.right, cur_node)
                #Assign new pointer of smallest
                smallest.left = cur_node.left
                smallest.right = cur_node.right
                return smallest
            else:
                if cur_node.left:
                    return cur_node.left
                else:
                    return cur_node.right
        return cur_node

    def delete(self, value):
        self.root = self._delete(value, self.root)



if __name__ == '__main__':
    bst = BST()
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(1)
    bst.insert(0)
    bst.insert(9)
    bst.insert(8)
    print(bst)
    print(bst.search(10))
    bst.delete(3)
    print(bst)
    bst.delete(3)
    print(bst)
    bst.delete(4)
    print(bst)
    bst.delete(5)
    print(bst)

