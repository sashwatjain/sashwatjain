"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        return False        
# Approach:
# Time Complexity:
# Space Complexity:
