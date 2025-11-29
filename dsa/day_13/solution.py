"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

class Solution:
    def equalPartition(self, arr):

        total = sum(arr)
        if total % 2 != 0:
            return False

        target = total // 2
        
        dp = set([0])

        for num in arr:
            new_dp = dp.copy()
            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    new_dp.add(s + num)
            dp = new_dp

        return False
class Solution:
    def equalPartition(self, arr):
        # code here
        if (sum(arr)/2 != 0):
            return false
        
        def check_sum(sumfinal,sum,arr,idx):
            if sum == sumfinal:
                return true 
            elif idx+1 == len(arr):
                return false
            elif sum < sumfinal:
                return check_sum(sumfinal,sum + arr[idx],arr,idx+1) or check_sum(sumfinal,sum ,arr,idx+1)
            else :
                return false
                
        sum = 0
        sumfinal = sum(arr)/2
        return check_sum(sumfinal,sum,arr,0)
    
class Solution:
    def knightTour(self, n):
        # code here
        if n == 1:
            return [[0]]
        if n <= 4:
            return []
        board = [[-1 for _ in range(n)] for _ in range(n)]
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        def get_degree(x, y):
            count = 0
            for dx, dy in moves:
                if is_safe(x + dx, y + dy):
                    count += 1
            return count
            
        def is_safe(x,y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1
        
        def solve(x, y, move_count):
            board[x][y] = move_count
            
            if move_count == n * n - 1:
                return True
            
            next_moves = []
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy
                if is_safe(next_x, next_y):
                    degree = get_degree(next_x, next_y)
                    next_moves.append((degree, next_x, next_y))
            
            next_moves.sort() 
            
            for _, next_x, next_y in next_moves:
                if solve(next_x, next_y, move_count + 1):
                    return True
            
            board[x][y] = -1
            return False
        
        if solve(0, 0, 0):
            return board
        else:
            return []    
# Approach:
# Time Complexity:
# Space Complexity:
