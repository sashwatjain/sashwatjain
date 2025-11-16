# """
# Day: day_03 – DSA – Arrays – Medium  
# Platform:
# Difficulty:
# Date:
# """

# "# Sol 1 Function to find common elements in three arrays"
# def commonElements(arr1, arr2, arr3):
#     i, j, k = 0, 0, 0
#     common = []

#     while i < len(arr1) and j < len(arr2) and k < len(arr3):
#         if arr1[i] == arr2[j] == arr3[k]:
#             common.append(arr1[i])
#             i += 1
#             j += 1
#             k += 1

#             while i < len(arr1) and arr1[i] == arr1[i - 1]:
#                 i += 1
#             while j < len(arr2) and arr2[j] == arr2[j - 1]:
#                 j += 1
#             while k < len(arr3) and arr3[k] == arr3[k - 1]:
#                 k += 1

#         elif arr1[i] < arr2[j]:
#             i += 1
#         elif arr2[j] < arr3[k]:
#             j += 1
#         else:
#             k += 1

#     return common


# # Sample Input
# arr1 = [1, 5, 10, 20, 30]
# arr2 = [5, 13, 15, 20]
# arr3 = [5, 20]
# common = commonElements(arr1, arr2, arr3)
# if len(common) == 0:
#     print(-1)
# print(*common)

# "# Splution of Q2 Python 3 program to search an element in an array" 
# # where difference between adjacent elements is atmost k

# # x is the element to be searched in arr[0..n-1]
# # such that all elements differ by at-most k.
# def search(arr, n, x, k):

#     # Traverse the given array starting from
#     # leftmost element
#     i = 0
#     while (i < n):
    
#         # If x is found at index i
#         if (arr[i] == x):
#             return i

#         # Jump the difference between current
#         # array element and x divided by k
#         # We use max here to make sure that i
#         # moves at-least one step ahead.
#         i = i + max(1, int(abs(arr[i] - x) / k))
    

#     print(""number is not present!"")
#     return -1


# # Driver program to test above function
# arr = [2, 4, 5, 7, 7, 6]
# x = 6
# k = 2
# n = len(arr)
# print(""Element"", x, ""is present at index"",search(arr, n, x, k))


# #Solution of Q3

# #User function Template for python3
# class Solution:
#     def findCeil(self, arr, x):
#         n = len(arr)
#         for i in range(n):
#             if arr[i] >= x:
#                 return i
#         return -1  


# # solution of Q4
# from typing import List


# class Solution:
#     def findPair(self, arr: List[int], x: int) -> int:
#         # code here
#         n = len(arr)
#         arr.sort()
#         max_diff = arr[n-1] - arr[0]
#         if max_diff < x :
#             return 0
#         for i in range(n-1,-1,-1):
#             j = 0
#             while j < i : 
#                 if arr[i] - arr[j] == x :
#                     return 1
#                 elif  arr[i] - arr[j] > x:
#                    j += 1 
#                 else :
#                    break
#         return 0            
        
# # This code is contributed
# # by Smitha Dinesh Semwal"





# # Approach:
# # Time Complexity:
# # Space Complexity:
