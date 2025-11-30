# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0

https://www.geeksforgeeks.org/problems/remove-invalid-parentheses/1

---

# ✅ **High-Level Idea**

Given a string like:

```
"(a)())()"
```

We want to remove **minimum number of invalid parentheses** so the result becomes valid.

Valid outputs may be:

```
["(a())()", "(a)()()"]
```

We must:

1. Find **how many left '(' and right ')' parentheses must be removed**
   (minimum removals)
2. Try removing them in all possible combinations
3. When both counts reach zero → check if string is valid
4. Use a **set to avoid duplicates**

---

# 🔥 STEP 1 — Find how many parentheses to remove

### Function:

```python
def get_right_left_remove_count(self, s)
```

### Goal:

Calculate **how many '(' and ')' we need to remove** to make the string valid.

### Logic:

We scan left to right:

* Every `'('` increases `left`
* Every `')'` increases `right`

But if we have extra `')'` (like `")("` or `"())"`), we must remove them.

Algorithm:

```
if char == '(':
    left++

if char == ')':
    right++
    if left > 0:
        # found a pair -> match them
        left--  
        right-- 
```

So:

* `left` = unmatched `(` that we must remove
* `right` = unmatched `)` that we must remove

Example:

```
"(a)())()"
left = 1
right = 1
```

Meaning:

* We must remove **1 '('**
* We must remove **1 ')'**

---

# 🔥 STEP 2 — Recursively remove parentheses

### Function:

```python
def get_valid_parentheses(self, s, left, right, results, cache)
```

Inputs:

* `s` → current string
* `left` → how many '(' must still be removed
* `right` → how many ')' must still be removed
* `results` → final answers
* `cache` → seen strings (to avoid duplicates)

---

# 🎯 When do we check validity?

When both counts reach zero:

```python
if left == 0 and right == 0:
    if self.is_valid_parentheses(s):
        results.add(s)
```

No more removals needed → check if valid → store.

---

# 🧠 STEP 3 — Try removing a character at every position

We loop:

```python
for idx, c in enumerate(s):
    temp = s[:idx] + s[idx + 1:]  # string after removal
```

We try removing each char one by one.

BUT we only remove valid targets:

* if `c == '('` and `left > 0` → allowed to remove a left
* if `c == ')'` and `right > 0` → allowed to remove a right

This ensures we remove *exactly the required minimum number* of parentheses.

---

# 🛑 Avoid Duplicate Work Using Cache

```python
if temp in cache:
    continue
cache.add(temp)
```

Without this, many strings would repeat because removing from different sides often produces identical strings.

Example:

```
(()))
 remove index 3
 remove index 4
```

Both may produce same string `"(()))"` again.

Cache prevents infinite recursion and duplicate results.

---

# 🔥 STEP 4 — Valid parentheses check

### Function:

```python
def is_valid_parentheses(self, s)
```

Uses a simple counter:

* `'('` increases count
* `')'` decreases count
* count must never go negative
* must return to 0 at end

This verifies string validity.

---

# 📌 **Putting It All Together (Flow)**

### Example: Input

```
s = "(a)())()"
```

### Step 1: Count removals

```
left = 1
right = 1
```

### Step 2: Try all removals

Try removing one `(` and one `)` in various combinations:

```
"(a)())()" → remove char at i → new string → recurse
```

Eventually it finds:

```
"(a())()"
"(a)()()"
```

Both are valid.

---

# 🎉 Final Output

`results = ["(a())()", "(a)()()"]`

---

⭐ RULE 1: Never use two pointers in recursion unless you absolutely must

Dynamic substring expansion should be done with a loop, not recursion.

⭐ RULE 2: Your base case should always be the "goal state"

Goal: index reached end of string → success.

Not some pointer hitting a boundary.

⭐ RULE 3: Never mutate a recursive variable

Always pass a new version:

❌ sentance += " " + word
✔ new_sentence = sentence + " " + word

⭐ RULE 4: Always ask before coding:
“What is my recursion representing?”

In correct code:

i = current position in the string

sentence = words chosen so far

In your code:

unclear meaning of i

unclear meaning of j

unclear meaning of sentence state

If you can’t clearly define recursion variables, the logic will collapse.