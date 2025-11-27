"""
Day: day_XX – <Problem Name>
Platform:
Difficulty:
Date:
"""

# Function to find the longest path using backtracking
def dfs(mat, visited, i, j, x, y):
    m = len(mat)
    n = len(mat[0])
    
    # If destination is reached
    if i == x and j == y:
        return 0
    
    # If cell is invalid, blocked, or already visited
    if i < 0 or i >= m or j < 0 or j >= n or mat[i][j] == 0 or visited[i][j]:
        return -1  # Invalid path
    
    # Mark current cell as visited
    visited[i][j] = True
    
    maxPath = -1
    
    # Four possible moves: up, down, left, right
    row = [-1, 1, 0, 0]
    col = [0, 0, -1, 1]
    
    for k in range(4):
        ni = i + row[k]
        nj = j + col[k]
        
        pathLength = dfs(mat, visited, ni, nj, x, y)
        
        # If a valid path is found from this direction
        if pathLength != -1:
            maxPath = max(maxPath, 1 + pathLength)
    
    # Backtrack - unmark current cell
    visited[i][j] = False
    
    return maxPath

def longestPath(mat, xs, ys, xd, yd):
    m = len(mat)
    n = len(mat[0])
    
    # Check if source or destination is blocked
    if mat[xs][ys] == 0 or mat[xd][yd] == 0:
        return -1
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    return dfs(mat, visited, xs, ys, xd, yd)

if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    xs, ys = 0, 0 
    xd, yd = 1, 7 
    
    result = longestPath(mat, xs, ys, xd, yd)
    
    if result != -1:
        print(result)
    else:
        print(-1)




# Approach:
# Time Complexity:
# Space Complexity:
