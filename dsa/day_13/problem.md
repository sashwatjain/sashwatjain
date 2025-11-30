# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0

https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1

https://www.geeksforgeeks.org/dsa/the-knights-tour-problem/

---

# 🔥 **Goal**

We want to check whether the array can be split into **two subsets with equal sum**.

Example:
`arr = [1, 5, 11, 5]`
Total = 22 → target = 11
So we must check:
👉 **Is there a subset whose sum is 11?**
If yes → array can be divided into two equal partitions.

---

# 🧠 **DP Concept Used**

We keep a **set of all possible subset sums** we can make using the numbers seen so far.

Example:
Start with `{0}`
→ means before using any number, we can make sum **0**.

Each time we take a number, we add it to all existing sums.

---

# 📝 **Line-by-line Explanation**

### **1. Total sum**

```python
total = sum(arr)
```

### **2. If total is odd, answer is impossible**

```python
if total % 2 != 0:
    return False
```

Odd numbers cannot be split into two equal integers.

---

### **3. Target subset sum**

```python
target = total // 2
```

---

### **4. DP set: all sums we can create**

```python
dp = set([0])
```

Initially, we can only form **0**.

---

### **5. Loop through each number**

```python
for num in arr:
```

---

### **6. Copy current possible sums**

```python
new_dp = dp.copy()
```

We try to add the new number to each already possible sum.

Example:
If dp = {0, 5} and num = 6
Then new possible sums:
→ 0 + 6 = 6
→ 5 + 6 = 11

---

### **7. Check all existing sums**

```python
for s in dp:
```

---

### **8. If new sum equals target → found subset**

```python
if s + num == target:
    return True
```

---

### **9. If new sum < target → add to new dp**

```python
if s + num < target:
    new_dp.add(s + num)
```

We only keep sums ≤ target because sums bigger than target are useless.

---

### **10. Update dp**

```python
dp = new_dp
```

---

### **11. If loop ends without finding target**

```python
return False
```

---

# 🎨 **Short Visual Example**

Given `arr = [1, 5, 11, 5]`:

### Start:

`dp = {0}`

### Use 1:

Possible sums = {0, 1}

### Use 5:

From 0 → 5
From 1 → 6
So dp = {0, 1, 5, 6}

### Use 11:

From 0 → 11 → 🎉 TARGET FOUND → return True

Done.

---

# 🧩 Why this method is fast

* DP set grows but only up to `target` numbers
* Much faster than recursion
* Time complexity: **O(n * target)**
* Works perfectly for medium-sized arrays

---

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