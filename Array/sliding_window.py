"""
Given n non-negative integers a_1, a_2, ..., a_n and a target k,
count the number of contiguous subarrays that are less than k.
Example:
  Input: nums = [1,2,3,2,1], k = 3
  Output: 7
  Explanation: The 8 subarrays that have sum less than 3 are: [1], [2], [3], [2], [1], [1,2], [2,1]
"""

def numSubArr(nums, k):
    start = 0
    curSum = 0
    count = 0
    for end in range(len(nums)):
        curSum += nums[end]
        while curSum > k:
            curSum -= nums[start]
            start += 1
        count += end - start + 1
    return count

def numSubArr_while(nums, k):
    start, end = 0, 0
    curSum, count = 0, 0
    while end < len(nums):
        curSum += nums[end]
        while curSum > k:
            curSum -= nums[start]
            start += 1
        count += end - start + 1
        end += 1
    return count

if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1]
    k = 3
    print(f"Number of arrays: {numSubArr(nums, k)}")
    print(f"Number of arrays: {numSubArr_while(nums, k)}")
