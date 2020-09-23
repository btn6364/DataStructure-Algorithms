"""
Implement a max stack.
- push(val): push value into the stack.
- pop(): pop off and return the top most element of the stack.
- max: return the current maximum number of the stack.

All methods should run in O(1) time.
"""
"""
Assumptions:
- any value to push into the stack. 

Input: 

push(4)
push(3)
push(2)
push(1)
push(5)

maxValue = 5

stack = [4, 3, 2, 1]
max   = [4, 4, 4, 4]

Runtime: O(1) 
Space: O(N) 
"""

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []
        self.maxValue = float("-inf")
    def push(self, value):
        self.stack.append(value)
        self.maxValue = max(self.maxValue, value)
        if not self.maxStack or self.maxValue > self.maxStack[-1]:
            self.maxStack.append(self.maxValue)
    def pop(self):
        if not self.stack:
            raise Exception("ERROR: Pop from an empty stack.")
        top = self.stack.pop()
        self.maxStack.pop()
        self.maxValue = self.maxStack[-1]
        return top
    def max(self):
        return self.maxValue

if __name__ == '__main__':
    maxStack = MaxStack()
    maxStack.push(4)
    maxStack.push(2)
    maxStack.push(3)
    maxStack.push(6)
    print(maxStack.max())
    print(maxStack.pop())
    print(maxStack.max())
    maxStack.push(5)
    print(maxStack.max())
    print(maxStack.pop())
    print(maxStack.max())