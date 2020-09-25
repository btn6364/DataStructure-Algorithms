"""
Idea:
- Search for a suffix that's also a prefix.

m = len(pattern) and n = len(string)

Runtime: O(m + n)
Space: O(m)
"""
def createSkipTable(pattern):
    skip_table = [-1] * len(pattern)

    #there's no suffix that is also a prefix for a string of size 1.
    skip_table[0] = 0

    i, j = 0, 1
    while j < len(pattern):
        #If there's a suffix and prefix match
        if pattern[i] == pattern[j]:
            skip_table[j] = i + 1
            i += 1
            j += 1
        #If there's a mismatch when there was no match before
        elif i == 0:
            skip_table[j] = 0
            j += 1
        #If there's a mismatch when there was at least 1 match before
        else:
            i = skip_table[i-1]
    return skip_table

def KMP_search(string, pattern):
    #skip_table[i]: the number of characters we can skip with there's a mismatch at pattern[i + 1]
    skip_table = createSkipTable(pattern)

    #i: pointer at pattern, j: pointer at the string
    i, j = 0, 0
    while j < len(string):
        #When there's a match and i is at the end of the pattern.
        #This means we have found the pattern in string.
        if pattern[i] == string[j] and i == len(pattern) - 1:
            return True
        #If there's a match and i is NOT at the end of the pattern.
        elif pattern[i] == string[j]:
            i += 1
            j += 1
        #If there's a mismatch, do a backtrack using the skip_table
        else:
            i = skip_table[i-1]
            if i == 0:
                j += 1
    return False


if __name__ == '__main__':
    string = "adsgwadsxdsgwadsgz"
    pattern = "dsgwadsgz"
    print(KMP_search(string, pattern))



