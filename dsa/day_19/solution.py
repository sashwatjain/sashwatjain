"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""
MOD = 10**9 + 7
# Multiply contents of two linked lists
def multiplyTwoLists(first, second):
    num1 = 0
    num2 = 0

    # Traverse the first list and 
    # construct the number with modulo
    while first is not None:
        num1 = (num1 * 10 + first.data) % MOD
        first = first.next

    # Traverse the second list and 
    # construct the number with modulo
    while second is not None:
        num2 = (num2 * 10 + second.data) % MOD
        second = second.next

    # Return the product of the two
    # numbers with modulo
    return (num1 * num2) % MOD
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Step 1: find length of linked list
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        # If we need to remove the head node
        if n == length:
            return head.next
        
        # Step 2: find the (length - n)-th node
        temp = head
        pos = length - n  # this is the position BEFORE the node to delete
        
        while pos > 1:
            temp = temp.next
            pos -= 1
        
        # Step 3: delete the next node
        temp.next = temp.next.next
        
        return head






class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head

        # Detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:   # Loop found
                break

        # If no loop
        if fast is None or fast.next is None:
            return head

        # Move slow to head, keep fast at meeting point
        slow = head

        # Find the node just before loop start
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Now fast is the node before loop start
        while fast.next != slow:
            fast = fast.next

        # Break loop
        fast.next = None

        return head


# Approach:
# Time Complexity:
# Space Complexity:
