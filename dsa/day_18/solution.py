"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""
class Solution:
    # Function to remove duplicates from an unsorted linked list.
    def removeDuplicates(self, head):
        if not head:
            return head
        
        seen = set()
        seen.add(head.data)
        
        curr = head
        
        while curr.next:
            if curr.next.data in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.data)
                curr = curr.next
        
        return head
    
def sortList(head):
    if not head or not head.next:
        return head

    # Create three dummy nodes to point to beginning of 
    # three linked lists. These dummy nodes are created to 
    # avoid null checks. 
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)

    # Initialize current pointers for three 
    # lists 
    zero = zeroD
    one = oneD
    two = twoD

    # Traverse list 
    curr = head
    while curr:
        if curr.data == 0:
          
            # If the data of current node is 0, 
            # append it to pointer zero and update zero
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
          
            # If the data of cu
            # append it to pointer one and update one
            one.next = curr
            one = one.next
        else:
            # If the data of current node is 2, 
            # append it to pointer two and update two
            two.next = curr
            two = two.next
        curr = curr.next

    # Combine the three lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    # Updated head 
    head = zeroD.next

    return head    

# Approach:
# Time Complexity:
# Space Complexity:
