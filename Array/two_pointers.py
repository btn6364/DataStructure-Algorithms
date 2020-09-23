"""
Given n non-negative integers a_1, a_2, ..., a_n , where each represents a point at coordinate (i, a_i).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""

def containerMostWater(arr):
    start, end = 0, len(arr) - 1
    maxContainer = -1
    while start < end:
        curContainer = (end - start) * min(arr[start], arr[end])
        maxContainer = max(maxContainer, curContainer)
        if arr[end] > arr[start]:
            start += 1
        else:
            end -= 1
    return maxContainer


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max container: {containerMostWater(arr)}")