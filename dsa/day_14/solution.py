"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""
#User function Template for python3


#User function Template for python3
from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = self.get_right_left_remove_count(s)
        
        results = set()
        self.get_valid_parentheses(s, left, right, results, set())
        return list(results)
        
    def get_valid_parentheses(self, s, left, right, results, cache):
        if left == 0 and right == 0:
            if self.is_valid_parentheses(s):
                results.add(s)
            
        for idx, c in enumerate(s):
            # skip strings that have already been analyzed
            temp = s[:idx] + s[idx + 1:]
            if temp in cache:
                continue     
            cache.add(temp)
            
            # remove parentheses
            if c == '(' and left > 0:
                self.get_valid_parentheses(temp, left - 1, right, results, cache)
            elif c == ')' and right > 0:
                self.get_valid_parentheses(temp, left, right - 1, results, cache)
    
    #checking left and right paranthese count
    def get_right_left_remove_count(self, s):
        left, right = 0, 0
        for c in s:
            if c == '(': left += 1
            elif c == ')': 
                right += 1
                if left > 0:
                    right -= 1
                    left -= 1
        return left, right
             
    def is_valid_parentheses(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count < 0: return False
        return count == 0


class Solution:
    def wordBreak(self, dict, s):
        res = []
        n = len(s)
        
        def dfs(i, sentence):
            if i == n:
                res.append(sentence.strip())
                return
            
            for j in range(i, n):
                word = s[i:j+1]
                if word in dict:
                    dfs(j+1, sentence + " " + word)
        
        dfs(0, "")
        return res

# Approach:
# Time Complexity:
# Space Complexity:
