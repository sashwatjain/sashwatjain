# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0


Q1 https://www.geeksforgeeks.org/problems/stickler-theif-1587115621/1

---

# 🧠 Maximum Sum of Non-Adjacent Elements — Explanation

This function computes the **maximum possible sum** from an array such that **no two selected elements are adjacent**.
It uses **dynamic programming** with **O(1) space** optimization.

---

## 🧩 Problem Idea

Given an array:

```
arr = [a1, a2, a3, ... an]
```

You must pick numbers such that:

* No two chosen numbers are next to each other.
* The total sum is as large as possible.

Example:

```
[3, 2, 5, 10, 7]
→ Maximum sum = 15 (3 + 5 + 7 or 3 + 10)
```

---

## 💡 DP Logic (Recurrence)

For each index `i`, you have **two choices**:

### 1. **Take** `arr[i]`

If you take it, you must skip `arr[i-1]`, so you add it to the best sum until `i-2`:

```
arr[i] + dp[i-2]
```

### 2. **Skip** `arr[i]`

Then your best is just the best sum until `i-1`:

```
dp[i-1]
```

So:

```
dp[i] = max(arr[i] + dp[i-2], dp[i-1])
```

---

## 🔧 Space Optimization

Instead of keeping the whole DP array, the code stores only:

| Variable     | Meaning                             |
| ------------ | ----------------------------------- |
| `secondLast` | dp[i-2] — best up to two steps back |
| `last`       | dp[i-1] — best up to previous index |
| `res`        | dp[i] — current result              |

This reduces memory from **O(n)** to **O(1)**.

---

## 🏃‍♂️ Code

```python
def findMaxSum(arr):
    n = len(arr)

    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    # dp[i-2] and dp[i-1]
    secondLast = 0
    last = arr[0]

    for i in range(1, n):
        # dp[i] = max(take current, skip current)
        res = max(arr[i] + secondLast, last)

        # Move window forward
        secondLast = last
        last = res

    return res
```

---

## 🏁 Step-by-Step Example

For:

```
arr = [3, 2, 5, 10, 7]
```

| i | arr[i] | secondLast | last | res = max(arr[i] + secondLast, last) |
| - | ------ | ---------- | ---- | ------------------------------------ |
| 1 | 2      | 0          | 3    | 3                                    |
| 2 | 5      | 3          | 3    | 8                                    |
| 3 | 10     | 3          | 8    | 13                                   |
| 4 | 7      | 8          | 13   | 15                                   |

Final result: **15**

---

## ✔️ Complexity

* **Time:** O(n)
* **Space:** O(1)

This is the most efficient solution for this problem.

---

Q2 https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

---

# 🔄 Merging Two Sorted Arrays *Without Extra Space* — Explanation

This solution merges two arrays `a` and `b` **in-place** (using no extra array) such that:

* Both arrays end up sorted
* All smaller elements remain in `a`
* All larger elements end up in `b`

This is often called the **"in-place merge of two sorted arrays"** problem.

---

## 🧠 **Goal**

Given:

```
a = [sorted array]
b = [sorted array]
```

Rearrange values (without using extra space) so that:

* The final `a` contains the **smallest elements**
* The final `b` contains the **largest elements**
* Both remain sorted

---

## 💡 **Core Idea**

We use a **two-pointer technique**:

* `i` starts from the **end of array a**
* `j` starts from the **beginning of array b**

```
i = len(a) - 1  → largest in a
j = 0           → smallest in b
```

We compare:

```
a[i]  vs  b[j]
```

### ✔️ If `a[i] < b[j]`

Both are already in correct order → do nothing.

Move left in `a`:

```
i -= 1
```

### 🔄 If `a[i] >= b[j]`

They are out of order → swap them:

```
a[i], b[j] = b[j], a[i]
```

Then move:

```
i -= 1
j += 1
```

This ensures smaller values go to `a` and larger ones to `b`.

---

## 🧼 **Final Step: Sort Both Arrays**

After the swapping process, both arrays might not be fully sorted internally, so we apply:

```
a.sort()
b.sort()
```

This ensures both final arrays are properly sorted.

---

## 🏃 Example Walkthrough (Conceptually)

Suppose:

```
a = [1, 5, 9, 10]
b = [2, 3, 8]
```

We compare from opposite ends:

| Compare (a[i], b[j]) | Action                      |
| -------------------- | --------------------------- |
| (10, 2) → 10 > 2     | Swap → small to a, big to b |
| (9, 3) → 9 > 3       | Swap                        |
| (5, 8) → 5 < 8       | Correct → move only i       |

Finally sort both arrays.

---

## 🧾 Full Code (Given)

```python
class Solution:
    def mergeArrays(self, a, b):
        i = len(a) - 1
        j = 0
    
        # Swap smaller elements from b[] with
        # larger elements from a[]
        while i >= 0 and j < len(b):
            if a[i] < b[j]:
                i -= 1
            else:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
    
        # Sort both arrays
        a.sort()
        b.sort()
```

---

## 📌 **Time Complexity**

* Swapping loop: **O(min(n, m))**
* Sorting both arrays: **O(n log n + m log m)**

## 📌 **Space Complexity**

* **O(1)** extra space (in-place)


