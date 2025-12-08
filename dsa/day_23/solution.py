"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

# Python program to point to next higher value
# with an arbitrary pointer using merge sort approach
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.arbit = None


# Function to merge two sorted lists
def SortedMerge(left, right):
  
    # If one list is empty, return the other
    if not left:
        return right
    if not right:
        return left

    result = None
    curr = None

    # Initialize result with the smaller node
    if left.data <= right.data:
        result = left
        left = left.arbit
    else:
        result = right
        right = right.arbit
    curr = result

    # Merge the two lists
    while left and right:
        if left.data <= right.data:
            curr.arbit = left
            left = left.arbit
        else:
            curr.arbit = right
            right = right.arbit
        curr = curr.arbit

    # Attach remaining nodes
    curr.arbit = left if left else right
    return result


# Function to split the list into two halves
def split(head):
  
    # If list is empty or has one node
    if not head or not head.arbit:
        return None

    slow = head
    fast = head.arbit

    # Move slow and fast pointers to find middle
    while fast and fast.arbit:
        slow = slow.arbit
        fast = fast.arbit.arbit

    # Split the list into two halves
    second = slow.arbit
    slow.arbit = None
    return second


# Recursive merge sort for arbit pointers
def MergeSort(head):
  
    # If list is empty or has one node
    if not head or not head.arbit:
        return head

    # Split the list into two halves
    left = head
    right = split(head)

    # Recursively sort both halves
    left = MergeSort(left)
    right = MergeSort(right)

    # Merge the two sorted halves
    return SortedMerge(left, right)


# Function to populate arbit pointers
def populateArbit(head):
    curr = head

    # Initialize arbit pointers to next nodes
    while curr:
        curr.arbit = curr.next
        curr = curr.next

    # Sort the list using arbit pointers
    return MergeSort(head)


def printListArbit(node):
    curr = node

    while curr:
        print(curr.data, end=" ")
        curr = curr.arbit
    print()


if __name__ == "__main__":
  
    # Create a hardcoded linked list
    # List: 5 -> 10 -> 2 -> 3
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(2)
    head.next.next.next = Node(3)

    # Populate arbit pointers to next higher node
    head = populateArbit(head)

    printListArbit(head)




'''
# Node Class
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def reorderList(self, head):
  
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None      # cut the list into two halves
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is now head of reversed 2nd list
        
        # Step 3: Merge two lists
        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2


# Approach:
# Time Complexity:
# Space Complexity:
