# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0


---

# 📘 Algorithms Explanation: Inversion Count & Find Duplicates

This document explains two algorithms:

1. **Inversion Count using Merge Sort**
2. **Finding Duplicates using a Frequency Map**

---

# 1️⃣ Inversion Count (Using Modified Merge Sort)

## 🔍 What Is an Inversion?

An **inversion** is a pair of indices `(i, j)` such that:

* `i < j`, and
* `arr[i] > arr[j]`

It represents how far the array is from being sorted.

---

## 🧠 Approach: Merge-Sort Based Counting

During the merge step:

* If `left[j] <= right[k]` → no inversion
* Else (`left[j] > right[k]`):
  This means **every element from `left[j]` onward is greater than `right[k]`**.
  So we add:

```
inversions += len(left) - j
```

This technique reduces time complexity from **O(n²)** to **O(n log n)**.

---

## 🧩 Code

```python
class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            # Base case
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2

            # Recursive division
            left, invL = merge_sort(arr[:mid])
            right, invR = merge_sort(arr[mid:])

            merged = []
            inv = invL + invR  # Accumulate inversions
            j = k = 0

            # Merge process
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    merged.append(left[j])
                    j += 1
                else:
                    merged.append(right[k])
                    inv += len(left) - j  # Count inversions
                    k += 1

            # Append remaining items
            merged += left[j:] + right[k:]

            return merged, inv

        # Return only inversion count
        return merge_sort(arr)[1]
```

---

# 2️⃣ Finding Duplicates (Using Frequency Map)

## 🧠 Idea

* Use a dictionary to count how many times each element appears.
* Any element that appears more than once is a **duplicate**.
* If no duplicates exist, return **[-1]**.

---

## 🧩 Code

```python
def findDuplicates(arr):

    # Step 1: Frequency dictionary
    freqMap = {}
    result = []

    # Step 2: Count occurrences
    for num in arr:
        freqMap[num] = freqMap.get(num, 0) + 1

    # Step 3: Collect duplicates
    for key, value in freqMap.items():
        if value > 1:
            result.append(key)

    # Step 4: If no duplicates, return -1
    if not result:
        result.append(-1)

    return result
```

---

# ✅ Summary Table

| Problem             | Technique             | Time Complexity | Space Complexity |
| ------------------- | --------------------- | --------------- | ---------------- |
| **Inversion Count** | Modified Merge Sort   | `O(n log n)`    | `O(n)`           |
| **Find Duplicates** | Hash Map / Dictionary | `O(n)`          | `O(n)`           |

---

# 🎯 Final Notes

* The **inversion count** algorithm is optimal and commonly asked in coding interviews.
* Using a **frequency map** is the simplest and most efficient way to detect duplicates in an array.

---
