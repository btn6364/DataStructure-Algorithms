def is_anagram_arr(st1, st2):
    #Use cound array
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

from collections import defaultdict
def is_anagram_hash(st1, st2):
    if len(st1) != len(st2):
        return False
    freq_map = defaultdict(int)
    for ch1, ch2 in zip(st1, st2):
        freq_map[ch1] += 1
        freq_map[ch2] -= 1

    for ch in freq_map:
        if freq_map[ch] != 0:
            return False
    return True



if __name__ == '__main__':
    st1 = "binary"
    st2 = "brainy"
    print(f"Is anagram: {is_anagram_arr(st1, st2)}")
    print(f"Is anagram: {is_anagram_hash(st1, st2)}")