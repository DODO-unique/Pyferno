### 🧵 Slicing in Python

**Slicing** is when you extract a part of an indexed sequence (like `str`, `list`, `tuple`) using your own custom range.

---

### ⏱️ Time and Space Complexity

* **Time: O(n)**
  Because slicing iterates through up to `n` elements to build the new slice.

* **Space: O(n)**
  Yes, two things are created:

  1. The new slice object
  2. The resulting sliced sequence
     But constants are ignored in Big-O, so it stays **O(n)**.

---

### 🧠 How Python Resolves Slice Syntax

The square bracket syntax:

```python
s[1:4:1]
```

...is syntactic sugar for:

```python
s.__getitem__(slice(1, 4, 1))
```

So slicing triggers the **`__getitem__`** method with a `slice` object.

---

### 🧮 Resolving the `slice`

```python
slice_obj = slice(start, stop, step)
resolved = slice_obj.indices(len(s))
```

`.indices(length)` returns a normalized **tuple of (start, stop, step)**:

* It fixes `None`
* Adjusts negatives
* Prevents out-of-range issues

---

### 🧪 Example: Reversing a String

```python
s = "abcd"
s[::-1]
# Under the hood:

slice_obj = slice(None, None, -1)
tup = slice_obj.indices(len(s))  # → (3, -1, -1)
```

Now Python can iterate cleanly:

```python
result = ''.join(s[i] for i in range(*tup))  # → 'dcba'
```

---

### 🔄 Lists and Tuples Do the Same Thing

* Lists → build with `.append()`
* Tuples → concatenate during iteration
* Slicing works identically because `__getitem__(slice(...))` is shared across all sequence types

---

### ⚠️ Notes

* `.indices()` doesn’t return `(0, 3, -1)` for `[::-1]` — it returns **(3, -1, -1)**
  (off-by-one clarification)
* Strings are immutable, so the result must be re-built from scratch

---

### ✅ Final TL;DR

Slicing =

* `__getitem__(slice(...))`
* `.indices(len(...))` to normalize
* `range(...)` to iterate
* Copy into a new object (string, list, etc.)

It’s **iteration** + **allocation** dressed as syntactic sugar.