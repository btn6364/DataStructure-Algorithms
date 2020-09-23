"""
Reverse a string
"""

def reverseString(string):
    #base case
    if len(string) == 0:
        return string
    else:
        return reverseString(string[1:]) + string[0]

if __name__ == '__main__':
    string = "hello world"
    print(reverseString(string))
