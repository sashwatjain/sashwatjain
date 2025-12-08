"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class Solution:
    def compute(self,head):
        #Your code here
        curr = head
        prev = None
        while curr:
            n_ext = curr.next
            curr.next = prev
            prev = curr
            curr = n_ext
            
        head1 = prev    
        
        maximum = head1.data
        
        curr = head1
        
        while curr.next:
            if curr.next.data < maximum :
                curr.next = curr.next.next
                continue
            maximum = max(maximum, curr.next.data)
            curr = curr.next
            
        curr = head1
        prev = None
        while curr:
            n_ext = curr.next
            curr.next = prev
            prev = curr
            curr = n_ext    
            
        return prev    
    

class Solution:
    def divide(self, head):
        # code here
        even = node()
        even.next = None
        evencurr = even
        
        odd = node()
        odd.next = None
        oddcurr = odd
        curr = head
        
        while curr:
            if curr.data % 2 == 0:
                evencurr.next = curr
                evencurr = evencurr.next
            else:   
                oddcurr.next = curr
                oddcurr = oddcurr.next
            curr = curr.next    
                
        oddcurr.next = None        
        evencurr.next = odd.next
        
        return even.next if even.next else odd.next


# Approach:
# Time Complexity:
# Space Complexity:
