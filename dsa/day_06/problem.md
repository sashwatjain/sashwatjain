# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0



# 📘 **Radix Sort in Python — Detailed Explanation**

This program implements **Radix Sort**, a sorting algorithm that sorts numbers **digit by digit**, starting from the **least significant digit (LSD)** (units place) to the **most significant digit (MSD)**.

Radix Sort uses **Counting Sort** as a subroutine to sort numbers based on a particular digit.

---

# 🧠 **How Radix Sort Works**

1. Find the **largest number** in the array → this tells us how many digits we need to process.
2. For each digit position:

   * Sort the array using **Counting Sort** based on that digit.
   * Increase digit position (units → tens → hundreds → ...).
3. Continue until all digit places have been processed.

Radix Sort is efficient for numbers with a fixed number of digits.

---

# 🧩 **Code Breakdown**

---

## ##️⃣ **`countingSort(arr, exp1)` — Counting Sort Based on One Digit**

```python
def countingSort(arr, exp1):
```

### 🔹 Purpose:

Sorts the array based on **one specific digit**, indicated by `exp1`:

| exp1 | Digit Position |
| ---- | -------------- |
| 1    | Units          |
| 10   | Tens           |
| 100  | Hundreds       |

---

### ### 1. Initialize variables

```python
n = len(arr)
output = [0] * n
count = [0] * 10
```

* `output`: stores sorted values for this pass.
* `count`: stores frequency of digits 0–9.

---

### ### 2. Count digit occurrences

```python
for i in range(0, n):
    index = arr[i] // exp1
    count[index % 10] += 1
```

For each number:

* Divide by `exp1` to extract the digit.
* `% 10` gives the digit at that position.
* Increment count.

Example (exp1 = 1 → units digit):

* 170 → 0
* 45 → 5
* 75 → 5
* 90 → 0
  etc.

---

### ### 3. Convert count array to cumulative positions

```python
for i in range(1, 10):
    count[i] += count[i - 1]
```

This turns frequency into **position indexes** for output.

---

### ### 4. Build the output array (stable sorting)

```python
i = n - 1
while i >= 0:
    index = arr[i] // exp1
    output[count[index % 10] - 1] = arr[i]
    count[index % 10] -= 1
    i -= 1
```

Processing from **right to left** keeps sorting *stable*.

---

### ### 5. Copy output back to original array

```python
for i in range(0, len(arr)):
    arr[i] = output[i]
```

---

# 🚀 **`radixSort(arr)` — Performs Radix Sort**

```python
def radixSort(arr):
```

### ### 1. Find the largest number

```python
max1 = max(arr)
```

This determines how many digits we need to sort.

---

### ### 2. Sort numbers digit-by-digit

```python
exp = 1
while max1 / exp >= 1:
    countingSort(arr, exp)
    exp *= 10
```

This loop runs:

* First for units place (`exp = 1`)
* Then tens (`exp = 10`)
* Then hundreds (`exp = 100`)
* …

Stops when `exp` exceeds the largest number.

---

# 🧪 **Driver Code**

```python
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(arr)
```

After sorting, output becomes:

```
2 24 45 66 75 90 170 802
```

---

# 📊 **Flow Summary**

### 1️⃣ Units place sort

→ `[170, 90, 802, 2, 24, 45, 75, 66]` (after first counting sort)

### 2️⃣ Tens place sort

→ `[802, 2, 24, 45, 66, 75, 170, 90]`

### 3️⃣ Hundreds place sort

→ `[2, 24, 45, 66, 75, 90, 170, 802]`

Final sorted list!

---

# 🎉 **Why Radix Sort Works Well?**

* Time Complexity: **O(d × (n + k))**

  * d = number of digits
  * n = number of elements
  * k = base (10 here)

* **Stable**, **non-comparative**, works great when range of numbers is known.

