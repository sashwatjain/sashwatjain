"""
Day: day_08 – Product array puzzle

Platform:
Difficulty:
Date:
"""

#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        idx = -1
        zeros = 0
        prod = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                idx = i
                zeros += 1
            else:
                prod *= arr[i]
        prod_arr = [0]*len(arr)     
        if zeros == 0:
            for i in range(len(arr)):
                prod_arr[i] = prod//arr[i]
        if zeros == 1:
            prod_arr[idx] = prod
        
        return prod_arr    
    
def minCostToMakeElementsEqual(arr):
    arr.sort()
    n = len(arr)

    # median
    median = arr[n // 2]

    # calculate cost
    cost = sum(abs(x - median) for x in arr)
    return cost


# Example
arr = [1, 100, 101]
print(minCostToMakeElementsEqual(arr))   # Output: 100


def canBeSortedByReversing(arr):
    n = len(arr)

    # Step 1: find first index i where order breaks
    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Already sorted
    if i == n - 1:
        return True

    # Step 2: find j where decreasing ends
    j = i
    while j < n - 1 and arr[j] > arr[j + 1]:
        j += 1

    # Step 3: boundary checks
    if i > 0 and arr[j] < arr[i - 1]:
        return False
    
    if j < n - 1 and arr[i] > arr[j + 1]:
        return False

    # Step 4: ensure from j onward is sorted
    k = j
    while k < n - 1:
        if arr[k] > arr[k + 1]:
            return False
        k += 1

    return True


class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        n = len(arr)
        result = []
    
        for a in range(n - 3):
    
            # skip duplicate a
            if a > 0 and arr[a] == arr[a - 1]:
                continue
    
            for b in range(a + 1, n - 2):
    
                # skip duplicate b
                if b > a + 1 and arr[b] == arr[b - 1]:
                    continue
    
                c, d = b + 1, n - 1
    
                while c < d:
                    s = arr[a] + arr[b] + arr[c] + arr[d]
    
                    if s == k:
                        result.append([arr[a], arr[b], arr[c], arr[d]])
    
                        # skip duplicates
                        c += 1
                        d -= 1
                        while c < d and arr[c] == arr[c - 1]:
                            c += 1
                        while c < d and arr[d] == arr[d + 1]:
                            d -= 1
    
                    elif s < k:
                        c += 1
                    else:
                        d -= 1
    
        return result

# Example
print(canBeSortedByReversing([1, 2, 5, 4, 3]))  # True
print(canBeSortedByReversing([1, 2, 4, 5, 3]))  # False


    

# Approach:
# Time Complexity:
# Space Complexity:
