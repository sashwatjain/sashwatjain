# Problem url sheet

https://docs.google.com/spreadsheets/d/1V5dedwFYWzyuaZTgGfZbLmacq1ma0yjUIm-TvKEGSbc/edit?gid=0#gid=0

https://leetcode.com/problems/merge-two-sorted-lists/description/

https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1


---

# ✅ **Why these two are NOT the same**

### ✔️ Works:

```python
del_node.data = del_node.next.data
del_node.next = del_node.next.next
```

### ❌ Does NOT work:

```python
del_node = del_node.next
```

---

# ⭐ **Reason: Assignment changes ONLY the local variable, not the linked list**

When you write:

```python
del_node = del_node.next
```

You are **only changing the local variable del_node** inside the function.
You are **NOT modifying the actual node in the linked list**.

Meaning:

* The original linked list still has the old node.
* Only the *pointer inside this function* moved.
* The outside linked list remains unchanged.

This is because in Python:

> **Rebinding a variable does NOT mutate the object.
> It only points the variable to a new object.**

So the linked list stays the same — nothing is deleted.

---

# ⭐ **But these lines DO modify the linked list**

```python
del_node.data = del_node.next.data
del_node.next = del_node.next.next
```

Here you are **changing the actual node’s fields (.data and .next)**.

This modifies the linked list structure itself.

This actually “deletes” the node by copying the next node’s value & skipping it.

---

# 📌 Example to understand

Suppose you have the list:

```
4 → 5 → 1 → 9
```

You want to delete node `5`.

### ✔️ What works:

```python
del_node.data = 1
del_node.next = node(9)
```

Linked list becomes:

```
4 → 1 → 9
```

### ❌ What doesn’t work:

```python
del_node = del_node.next
```

Inside the function:

```
del_node → 1
```

But outside:

```
4 → 5 → 1 → 9
```

The 5 is still there.
You only changed the *local variable*, not the list.

---

# 🔥 Final Summary

| Operation                            | Affects Linked List? | Why                                |
| ------------------------------------ | -------------------- | ---------------------------------- |
| `del_node = del_node.next`           | ❌ No                 | Just reassigns local variable      |
| `del_node.next = del_node.next.next` | ✔️ Yes               | Changes pointer inside actual node |
| `del_node.data = ...`                | ✔️ Yes               | Mutates node data                  |

---