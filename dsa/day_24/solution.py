"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class TwoStacks:
    def __init__(self):
        self.stk1_index = 0
        self.stk2_index = 0
        self.lst = []

    def push1(self, x):
        self.lst.append(x)
        self.stk1_index += 1

    def push2(self, x):
        self.lst.insert(0, x)
        self.stk2_index -= 1

    def pop1(self):
        if self.stk1_index > 0:
            self.stk1_index -= 1
            return self.lst.pop()
        else: return -1
            
    def pop2(self):
        if self.stk2_index < 0:
            self.stk2_index += 1
            return self.lst.pop(0)
        else: return -1


import operator
class Solution:
    def evaluatePostfix(self, arr):
        # code here
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a,b: a//b,
            "^": operator.pow
        }
        n = len(arr)-1
        i = 0
        
        stack = []
        while i <= n:
            token = arr[i]
            if token not in ops:
                stack.append(int(token))
            else:
                first = stack.pop()
                second = stack.pop()
                res = ops[token](second,first)
                stack.append(res)
            i+=1
        return stack.pop()    
            
                
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
    
class Solution:
    def reverseQueue(self, q):
        # code here
        stack = []
        while q:
            stack.append(q.popleft())
    
        while stack:
            q.append(stack.pop())
            
        return q    
    
class Solution:
    def reverseFirstK(self, q, k):
        if k <= 0 or k > len(q):
            return q
        
        stack = []

        # 1. Push first k elements into the stack
        for _ in range(k):
            stack.append(q.popleft())

        # 2. Put them back into queue (reversed order)
        while stack:
            q.append(stack.pop())

        # 3. Move the remaining (len(q) - k) elements to back
        size = len(q)
        for _ in range(size - k):
            q.append(q.popleft())

        return q    
    
class Solution:
    def deleteMid(self, stack):
        k = (len(stack)//2)+1
        self.middle(stack,k)
        
    def middle(self, s, k):
        if(k==1):
            s.pop()
            return
        temp = s.pop()
        self.middle(s, k-1)
        s.append(temp)
        #code here    

# Approach:
# Time Complexity:
# Space Complexity:
