"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        # Attach remaining part
        temp.next = list1 if list1 else list2
        
        return dummy.next




class Solution:
    def deleteNode(self, del_node):
        # code here
        next_node = del_node.next
        del_node.data = next_node.data
        del_node.next = del_node.next.next
# Approach:
# Time Complexity:
# Space Complexity:
