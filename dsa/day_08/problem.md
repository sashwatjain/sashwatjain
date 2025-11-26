# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0

https://www.geeksforgeeks.org/problems/product-array-puzzle4525/1

https://leetcode.com/problems/minimum-cost-to-make-array-equal/solutions/2734625/dp-solution-intuitive-and-clear-python-b-dpdr/

🧠 Intuition

The median minimizes the sum of absolute deviations.

The mean (average) minimizes the sum of squared deviations, which is a different problem.

So if the question was:
"Make all elements equal with minimum cost where cost = (x - y)²"
➡️ Then average would be correct.

But here cost = |x - y|, so only the median works.

https://www.geeksforgeeks.org/dsa/check-reversing-sub-array-make-array-sorted/

https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1

Below is a roadmap of the **core patterns** that appear again and again in these kinds of array / pointer / subarray problems.

---

# ✅ **1. Sorting + Two Pointers Pattern**

Used in:

* 2-sum (sorted)
* 3-sum
* 4-sum
* k-sum
* Pair sum
* Triplets
* Count pairs with given sum
* Find closest sum
* Remove duplicates
* Two sum in sorted matrix

**Core idea:**

1. Sort array.
2. Fix some indices.
3. Move two pointers `l` and `r` inside.

If sum < target → move `l++`
If sum > target → move `r--`
If equal → found answer

➡️ This solves 60% of “sum”, “quadruple”, “triplet”, “reverse to sort” type questions.

---

# ✅ **2. Boundary + Breakpoint Technique (Your reversal problem)**

Used in:

* Check if reversing a subarray sorts the array
* Check if array is nearly sorted
* Check if array is sorted + one swap
* Check if array can be sorted by one rotation
* Bitonic array problems

**Core idea:**

1. Find first breakpoint
2. Find second breakpoint
3. Validate boundaries
4. Everything else must remain sorted

This is also a powerful pattern.

---

# ✅ **3. Using Set / HashMap for Uniqueness**

Used in:

* 2-sum unsorted
* Count distinct pairs
* Longest consecutive sequence
* Find duplicates
* Subarrays with sum K

Hash maps give O(1) lookups and solve everything involving:

* seen before?
* counting?
* frequency?
* unique combinations?

---

# ✅ **4. Avoiding Duplicates Carefully**

Most medium+ level array problems break because of duplicates.

Learn:

* skip duplicates at the top of loops
* skip duplicates after finding answers
* use sets only when required

This pattern appears in:

* 3-sum
* 4-sum
* k-sum
* subsets with duplicates
* permutations II
* combination sum 2

---

# ✅ **5. Understanding Time Complexity Tradeoffs**

For example:

* Brute force 4-sum → O(n^4)
* Using sorting + two pointers → O(n^3)
* Using hashing → O(n^2)

Always aim for a better pattern, not brute force.

---

# ✅ **6. Break Down the Problem Into Smaller Decisions**

Example:
Your 4-sum code had duplicated loops and checks.

This comes from **not having clarity on the pattern**.

Instead, think:

* Fix 2 numbers → O(n²)
* Find remaining 2 using two pointers → O(n)
* Total O(n³)

Once you understand this skeleton, 4-sum becomes easy.

---

# ⭐ The Formula You Should Internalize

If you see:

### “Find pair / triplet / quadruple / k numbers with…”

👉 Sorting + Two Pointers

### “Array almost sorted / fix one subarray / can one operation solve?”

👉 Breakpoint + Boundary Check Pattern

### “Check existence / frequencies / repeating patterns”

👉 Hash map / Set

### “Need unique combinations”

👉 Duplicate-skipping pattern (critical for sorted arrays)

### “Need all combinations”

👉 Backtracking patterns

---

# 🧠 How to Master These Patterns?

Here’s your practice checklist:

### **Learn these 5 patterns deeply:**

1. **Two Pointers**
2. **Sliding Window**
3. **Hashmap / Set**
4. **Sorting + Binary Search**
5. **Prefix Sum / Difference Array**

AND solve the following 20 classic problems:

### Two Pointers:

* 2-sum sorted
* 3-sum
* 4-sum
* Container with most water
* Trapping rainwater

### Boundary problems:

* Reverse subarray to sort
* Sort array with one swap
* Almost sorted array

### Hashmap:

* Two sum
* Subarray sum equals k
* Longest consecutive sequence

### Sliding window:

* Longest substring without repeating characters
* Max sum subarray of size K
* Minimum window substring

---

Once you master these patterns, **80% of array + pointer problems become easy**.


