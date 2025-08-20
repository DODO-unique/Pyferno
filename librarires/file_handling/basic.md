# 📝 Python File Handling (Raccoon Edition)

### 1. Modes (Text)

| Mode   | Meaning                  | Creates File? | Error if Missing? | Cursor Start | Cursor Rules                                              |
| ------ | ------------------------ | ------------- | ----------------- | ------------ | --------------------------------------------------------- |
| `"r"`  | Read only                | ❌ No          | ✅ Yes             | Start        | Can `seek()`                                              |
| `"w"`  | Write (overwrite)        | ✅ Yes         | ❌ No              | Start        | ⚠️ Always erases; `seek()` useless (file truncated first) |
| `"a"`  | Append                   | ✅ Yes         | ❌ No              | End          | Cursor forced to end, `seek()` ignored for writing        |
| `"x"`  | Create new (exclusive)   | ✅ Yes         | ✅ If exists       | Start        | Same as `w` (new only)                                    |
| `"r+"` | Read + Write             | ❌ No          | ✅ Yes             | Start        | Can `seek()`, overwrites from cursor                      |
| `"w+"` | Write + Read (overwrite) | ✅ Yes         | ❌ No              | Start        | ⚠️ Erases existing, then can read/seek                    |
| `"a+"` | Append + Read            | ✅ Yes         | ❌ No              | End          | Reads anywhere, but writes *always at end*                |

🔑 **Raccoon Notes:**

* `"w"` & `"w+"` are scorched earth: file is nuked **before** you touch it.
* `"a"` & `"a+"` will *always* shove the cursor to the end for writing (append is append).
* `"r"` & `"r+"` scream if the file isn’t there.

---

### 2. Reading

```python
f.read()       # entire file (string)
f.read(10)     # next 10 chars
f.readline()   # next line
f.readlines()  # list of all lines
```

**No, there’s no `.readwords()`.**
If you want words:

```python
words = f.read().split()
```

Iterating line by line:

```python
for line in f:
    for word in line.split():
        print(word)
```

---

### 3. Writing

```python
f.write("hello\n")                # single string
f.writelines(["a\n", "b\n"])      # list of strings
```

⚠️ `.write()` overwrites from cursor position — so watch your `seek()` in `r+`/`w+`.

---

### 4. Cursor (Pointer)

* `f.tell()` → current byte position
* `f.seek(offset, whence)` → move cursor

  * `whence=0`: from start (default)
  * `whence=1`: from current position
  * `whence=2`: from end

⚠️ With `"w"`: file is truncated immediately → `seek()` can’t “rescue” old data.
⚠️ With `"a"`: writing cursor always forced to end → `seek()` only affects reads.

---

### 5. Binary Modes

Add `"b"` to any mode: `"rb"`, `"wb"`, `"ab"`, etc.

* Works with raw **bytes**, not text.
* Example:

```python
with open("image.png", "rb") as f:
    data = f.read()  # bytes object

with open("copy.png", "wb") as f:
    f.write(data)
```

Use this for images, executables, `.db` files, etc.

---

### 6. Quick Reference Mantras 🦝

* **r** → read, complain if missing.
* **w** → wipe + overwrite.
* **a** → always stack at the end.
* **+** → do two things at once (read + write).
* **seek()** → useless in `"w"`, one-eyed in `"a"`.

---

Behind the Scenes w Virgil:

Victor: Yeah, like why one-eyed 🧍‍♂️
Virgil: Because it can see all the file but can't write anywhere else... so... like half-seeking = one-eyed 🧍‍♂️