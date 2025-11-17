"""
Day: day_04 – <Problem Name>
Platform:
Difficulty:
Date:
"""


# class Solution:
#     def majorityElement(self, arr):
#         # python solution O(1) space
        
#         ### first pass to find majority element using moore's algo #####
#         element = 0
#         count = 0
#         for i in range(len(arr)):
#             if count == 0:
#                 element = arr[i]
#                 count = 1
#             elif element == arr[i]:
#                 count += 1
#             else:
#                 count -= 1
#         ##### finding the actual count of that element ######    
#         count_for_element = 0
#         for i in range(len(arr)):
#             if arr[i] == element:
#                 count_for_element += 1
#         ###### if it appears more than half times return it ######
#         if count_for_element > len(arr)//2:
#             return element
#         ##### its a tie means -1 #########
#         return -1    
    
#     Q2
#     for i in range(0,n-2):
        
#         # Initialize other two elements as corner elements 
#         # of subarray arr[j+1..k] 
#         j = i + 1
#         k = n-1

#         # Use Meet in the Middle concept 
#         while(j < k):
            
#             # If sum of current triplet is more or equal, 
#             # move right corner to look for smaller values
#             if (arr[i]+arr[j]+arr[k] >=sum):
#                 k = k-1
            
#             # Else move left corner 
#             else:
                
#                 # This is important. For current i and j, there 
#                 # can be total k-j third elements. 
#                 ans += (k - j)
#                 j = j+1
    
#     return ans



# Approach:
# Time Complexity:
# Space Complexity:
