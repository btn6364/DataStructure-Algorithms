def is_anagram(st1, st2):
    #O(L + A) runtime | O(A) space. 
    if len(st1) != len(st2):
        return False
    count_arr = [0] * 26
    for ch1, ch2 in zip(st1, st2):
        count_arr[ord(ch1) - ord('a')] += 1
        count_arr[ord(ch2) - ord('a')] -= 1

    for value in count_arr:
        if value != 0:
            return False
    return True

if __name__ == '__main__':
    st1 = "binary"
    st2 = "braisy"
    print(f"Is anagram: {is_anagram(st1, st2)}")