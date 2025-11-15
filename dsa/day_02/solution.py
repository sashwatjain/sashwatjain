"""
Day 2 – counting sort
Platform: GFG
Difficulty: Easy 
Date: 2025-11-15
"""

class Solution:
    def count_sort(arr):
        if not arr:
            return []

        n = len(arr)
        maxval = max(arr)

        # create and initialize cntArr
        cntArr = [0] * (maxval + 1)

        # count frequency of each element
        for v in arr:
            cntArr[v] += 1

        # compute prefix sums
        for i in range(1, maxval + 1):
            cntArr[i] += cntArr[i - 1]

        # build output array
        ans = [0] * n
        # iterate in reverse to keep it stable
        for i in range(n - 1, -1, -1):
            v = arr[i]
            ans[cntArr[v] - 1] = v
            cntArr[v] -= 1

        return ans





"""
Approach:
- Counting Sort is a non-comparison-based sorting algorithm. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted.
Advantage, of Counting Sort:
Counting sort generally performs faster than all comparison-based sorting algorithms, such as merge sort and quicksort, if the range of input is of the order of the number of input.
Stable Algorithm
Disadvantage of Counting Sort:
Does not work on decimal values.
Inefficient if the range of values to be sorted is very large.
Not an In-place sorting algorithm, It uses extra space for sorting the array elements.

Time Complexity: O(N+M) in all cases, where N and M are the size of inputArray[] and countArray[] respectively.
Auxiliary Space: O(N+M), where N and M are the space taken by outputArray[] and countArray[] respectively.
"""
