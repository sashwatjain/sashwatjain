"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

def findMaxSum(arr):
    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # Set previous 2 values
    secondLast = 0
    last = arr[0]

    # Compute current value using previous two values
    # The final current value would be our result
    res = 0
    for i in range(1, n):
        res = max(arr[i] + secondLast, last)
        secondLast = last
        last = res

    return res

arr = [6, 5, 5, 7, 4]
print(findMaxSum(arr))


# sOL 2


class Solution:
    def mergeArrays(self, a, b):
        # code here
        i = len(a) - 1
        j = 0
    
        # Swap smaller elements from b[] with
        # larger elements from a[]
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                i -= 1
            else:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
    
        # Sort both arrays
        a.sort()
        b.sort()
# Approach:
# Time Complexity:
# Space Complexity:
