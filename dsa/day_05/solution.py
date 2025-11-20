"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

# class Solution:
#     def inversionCount(self, arr):
#         def merge_sort(arr):
#             if len(arr) <= 1: return arr, 0
#             mid = len(arr) // 2
#             left, invL = merge_sort(arr[:mid])
#             right, invR = merge_sort(arr[mid:])
#             merged, i = [], 0
#             inv = invL + invR
#             j = k = 0
#             while j < len(left) and k < len(right):
#                 if left[j] <= right[k]:
#                     merged.append(left[j]); j += 1
#                 else:
#                     merged.append(right[k]); inv += len(left) - j; k += 1
#             merged += left[j:] + right[k:]
#             return merged, inv
#         return merge_sort(arr)[1]


# # Python code to find duplicates in an array
# # using hashmap

# def findDuplicates(arr):
  
#     # Step 1: Create an empty dictionary
#     # to store element frequencies
#     freqMap = {}
#     result = []

#     # Step 2: Iterate through the array and
#     # count element frequencies
#     for num in arr:
#         freqMap[num] = freqMap.get(num, 0) + 1

#     # Step 3: Iterate through the dictionary to
#     # find duplicates
#     for key, value in freqMap.items():
#         if value > 1:
#             result.append(key)

#     # Step 4: If no duplicates found, add -1 to the result
#     if not result:
#         result.append(-1)

#     # Step 6: Return the result list containing
#     # duplicate elements or -1
#     return result


# Approach:
# Time Complexity:
# Space Complexity:
