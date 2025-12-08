"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class Solution:
    def zigzag(self, head_node):
        # Complete this function
        curr = head_node
        flag = True
        while curr.next:
            if flag and curr.data >= curr.next.data :
                curr.data,curr.next.data = curr.next.data,curr.data
            elif not flag and curr.data <= curr.next.data :   
                curr.data,curr.next.data = curr.next.data,curr.data
            curr = curr.next
            flag = not flag
        return head_node

class Solution:
    def reverse(self, head):
        # code here
        
        curr = head
        ptemp = curr.prev
        
        while curr :
            temp = curr.next
            ntemp = curr.next
            curr.next = curr.prev
            curr.prev = ntemp
            ptemp = curr
            curr = temp

        
        return ptemp    
# Approach:
# Time Complexity:
# Space Complexity:
