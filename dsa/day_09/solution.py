"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class Solution:
    def medianOf2(self, A, B):
        n, m = len(A), len(B)
        total = n + m
        mid = total // 2

        i = j = 0
        prev = curr = 0

        # We only need to walk until 'mid'
        for _ in range(mid + 1):
            prev = curr

            # If A is exhausted, take from B
            if i >= n:
                curr = B[j]
                j += 1

            # If B is exhausted, take from A
            elif j >= m:
                curr = A[i]
                i += 1

            # Choose the smaller element
            elif A[i] < B[j]:
                curr = A[i]
                i += 1
            else:
                curr = B[j]
                j += 1

        # If total length is odd → median is curr
        if total % 2 == 1:
            return curr
        # If even → average of last two
        return (prev + curr) / 2

class Solution:
    def getMedian(self, arr):
        ans = []
        prefix = []

        for i in range(len(arr)):
            prefix.append(arr[i])
            prefix.sort()

            n = len(prefix)
            mid = n // 2

            if n % 2 == 1:
                ans.append(prefix[mid])
            else:
                ans.append((prefix[mid] + prefix[mid - 1]) / 2)

        return ans
  
            

# Approach:
# Time Complexity:
# Space Complexity:
