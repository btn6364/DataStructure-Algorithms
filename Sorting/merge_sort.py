"""
Merge sort algorithm.
Runtime: O(NlogN)
Space: O(N)
"""

def mergeSort(nums):
    helper_mergeSort(nums)
    return nums

def helper_mergeSort(nums):
    if len(nums) <= 1:
        return
    mid = len(nums) // 2
    left_nums, right_nums = nums[:mid], nums[mid:]
    helper_mergeSort(left_nums)
    helper_mergeSort(right_nums)
    merge(nums, left_nums, right_nums)

def merge(nums, left_nums, right_nums):
    #The current index of nums
    idx = 0
    #Initialize the current index of left_nums and right_nums
    left, right = 0, 0
    while left < len(left_nums) and right < len(right_nums):
        if left_nums[left] <= right_nums[right]:
            nums[idx] = left_nums[left]
            left += 1
        else:
            nums[idx] = right_nums[right]
            right += 1
        idx += 1
    # if left pointer reach the end first, extend right_nums. Otherwise, extend left_nums
    if left == len(left_nums):
        #extend right_nums
        while right < len(right_nums):
            nums[idx] = right_nums[right]
            right += 1
            idx += 1
    # extend right_nums
    while left < len(left_nums):
        nums[idx] = left_nums[left]
        left += 1
        idx += 1

if __name__ == '__main__':
    nums = [4, 6, 2, 1, 2, 2, 2, 4, 4, 3, 5, 7]
    print(mergeSort(nums))
