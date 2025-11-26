"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class Solution:
    def targetSumComb(self, arr, target):
        # code here
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i, path, total + arr[i])
                path.pop()

        arr.sort()  # Optional: sort for consistent order
        backtrack(0, [], 0)
        return result

# Approach:
# Time Complexity:
# Space Complexity:
