def bubbleSort(array):
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        counter += 1
    return array

if __name__ == '__main__':
    nums = [4, 6, 2, 1, 2, 2, 2, 4, 4, 3, 5, 7]
    print(bubbleSort(nums))