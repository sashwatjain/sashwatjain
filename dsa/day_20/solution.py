"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""


class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        temp = head1
        while temp.next:
            temp = temp.next
        temp.next = head1
        
        fast,slow = head2, head2
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        slow = head2
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow    
    
def flatten_list(head):

    # Base case
    if head is None:
        return

    # Find tail node of first level
    tail = head
    while tail.next is not None:
        tail = tail.next

    # traverse through all nodes of first level 
    curr = head

    while curr != None:

        # If current node has a child
        if curr.child is not None:

            # then append the child at the end of current list
            tail.next = curr.child

            # and update the tail to new last node
            tmp = curr.child
            while tmp.next is not None:
                tmp = tmp.next
            tail = tmp

            # Remove link between curr and child node
            curr.child = None

        # Change current node
        curr = curr.next    
# Approach:
# Time Complexity:
# Space Complexity:
