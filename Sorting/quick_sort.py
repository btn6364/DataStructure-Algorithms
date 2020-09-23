"""
Quicksort algorithm.

Runtime: O(NlogN) on average - O(N^2) worst case.
Space: O(N)
"""

def quickSort(nums):
    return helper_quickSort(nums)

def helper_quickSort(nums):
    if len(nums) <= 1:
        return nums

    #Pick nums[0] as the pivot, seperate the smaller numbers to the left and larger numbers to the right.
    pivot = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[0]:
            pivot += 1
            #swap nums[i] and nums[pivot]
            nums[i], nums[pivot] = nums[pivot], nums[i]

    #swap the pivot to the correct position
    nums[0], nums[pivot] = nums[pivot], nums[0]

    # Now the array look like this [left] - pivot - [right]
    #Recursive call the quickSort on the left and right subarrays.
    left = helper_quickSort(nums[:pivot])
    right = helper_quickSort(nums[pivot+1:])
    return left + [nums[pivot]] + right

if __name__ == '__main__':
    nums = [4, 6, 2, 1, 2, 2, 2, 4, 4, 3, 5, 7]
    print(quickSort(nums))