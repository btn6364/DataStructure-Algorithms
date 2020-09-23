"""
Ex:
             8
           /  \
          4    7
         / \  / \
       2   1 3  5

[__, 8, 4, 7, 2, 1, 3, 5 ]

Current element index: k
- parent node: k // 2
- left node: 2k
- right node: 2k + 1

"""
class MaxHeap:
    def __init__(self):
        #None, 3, 1, 2
        self.arr = [None]

    def insert(self, value):
        self.arr.append(value)
        self.swim()

    def swim(self):
        #get the last index, which is the index of the added number
        #index i: parent: i // 2
        idx = len(self.arr) - 1

        #while the current still has a parent node and its value is greater then the parent node, swap
        while (idx//2 > 0 and self.arr[idx] > self.arr[idx//2]):
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx // 2

    def getMax(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Popping from an empty array.")
        return self.arr[1]

    def delMax(self):
        if self.isEmpty():
            raise Exception("[ERROR]: Popping from an empty array.")
        #swap the first and the last value
        self.arr[1], self.arr[len(self.arr) - 1] = self.arr[len(self.arr) - 1], self.arr[1]
        #eliminate the last element
        value = self.arr.pop()
        #sink the value
        self.sink()
        return value

    """
    Sink the value to make it become a valid heap
    """
    def sink(self):
        idx = 1
        #when it still has a left child
        while (idx * 2 < len(self.arr)):
            cur = self.arr[idx]
            left = self.arr[idx*2]
            right = float("-inf")
            if idx * 2 + 1 < len(self.arr):
                right = self.arr[idx * 2 + 1]
            #compare cur to left and right
            if cur >= left and cur >= right:
                return
            if left > right:
                self.arr[idx], self.arr[idx*2] =  self.arr[idx*2], self.arr[idx]
                idx = idx * 2
            else:
                self.arr[idx], self.arr[idx * 2 + 1] = self.arr[idx*2+1], self.arr[idx]
                idx = idx * 2 + 1

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.arr) - 1

def heapsort(arr):
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)

    idx = 0
    while not heap.isEmpty():
        arr[idx] = heap.delMax()
        idx += 1
    return arr

if __name__ == '__main__':
    arr = [6, 4, 5, 1, -1, 2, 3, 1, 2, 3, 10]
    print(heapsort(arr))




