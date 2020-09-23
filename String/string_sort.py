def create_freq_arr(string, alphabet_size):
    freq_arr = [0] * alphabet_size
    for ch in string:
        idx = ord(ch) - ord('a')
        freq_arr[idx] += 1
    return freq_arr

def string_sort(string):
    alphabet_size = 26
    #break into frequency array
    freq_arr = create_freq_arr(string, alphabet_size)

    #create sorted string
    sorted_str = []

    #loop through the freq_arr
    for i, freq in enumerate(freq_arr):
        if freq > 0:
            sorted_str.append(chr(i + ord('a')) * freq)

    #return the out put
    return "".join(sorted_str)

if __name__ == '__main__':
    string = "abdkwdfaqasdqsa"
    print(f"Sorted string: {string_sort(string)}")

    string = ""
    print(f"Sorted string: {string_sort(string)}")