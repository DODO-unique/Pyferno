# Formatting in Python: Three Styles, One Bait

Formatting is one of Python's most deceptively rich features. It looks like a convenience, but hides power, speed, and subtle traps. Here we will talk about the three major formatting styles, from modern to ancient.

---

## 1. F-Strings (Python 3.6+)

F-strings are the most modern, fastest, and readable way to format strings.

```python
name = "Victor"
print(f"Welcome, {name}!")  # → Welcome, Victor
````

F-strings support **expressions**, not just variables:

```python
f"{3 * 7}"         # → '21'
f"{name.upper()}"  # → 'VICTOR'
```

⚠️ Mind how you handle expressions. No major expressions should be handled here.

### 📌 The `value:` Format Specifier

An f-string like `f"{value:10}"` is made of:

* `value` → The expression to be formatted
* `:` → Introduces the **format specifier block**
* `10` → Width, alignment, precision, type, etc.

Full syntax:

```
{value:[fill][align][sign][#][0][width][,][.precision][type]}
```

### 📐 Padding & Alignment

```python
f"{'cat':10}"     # 'cat       '   (default: right-align)
f"{'cat':<10}"    # 'cat       '   (left-align)
f"{'cat':>10}"    # '       cat'   (right-align)
f"{'cat':^10}"    # '   cat    '   (center-align)
```

With fill characters:

```python
f"{'cat':_>10}"   # '_______cat'
f"{'cat':.<10}"   # 'cat.......'
f"{'cat':-^10}"   # '---cat----'
```

### 💰 Numeric Padding

```python
f"{42:05}"        # '00042'
f"{1234567:,.2f}" # '1,234,567.00'
```

### 🧠 Nested Formatting

```python
value = 123
width = 10
print(f"{value:{width}}")  # → '       123'
```

### 🧪 Debug Print (3.8+)

```python
foo = 42
print(f"{foo=}")  # → foo=42
```

---

## 2. `.format()` Method

The older, verbose method, still widely used.

```python
"Hello, {}".format("world")  # → 'Hello, world'
"{1} then {0}".format("first", "second")  # → 'second then first'
"{name} is cool".format(name="Victor")   # → 'Victor is cool'
```

Supports the same specifiers:

```python
"{:.2f}".format(3.14159)  # '3.14'
"{:0>6}".format(42)       # '000042'
```

---

## 3. `%` Formatting (C-Style)

The legacy style, mostly seen in older codebases and low-level formatting.

```python
"%s is %d years old" % ("Victor", 5)  # → 'Victor is 5 years old'
```

Specifiers:

* `%s` → string
* `%d` → integer
* `%f` → float
* `%04d` → pad with zeroes: `'0042'`

Note: `%`-style does not support named parameters cleanly, and is not recommended for new code.

---

## 🧠 Internals / Memory Notes

* All formatting produces **new string objects**

  ```python
  f"{x}" is not x  # True
  ```
* F-strings compile to `BUILD_STRING` in bytecode
* `__format__()` is called under the hood on each value
* Formatting doesn’t use interning (unless you force it with `sys.intern()`)

f-string internals:

* 🔹 The f-string expressions get **evaluated at runtime** (as is, not replaced)
* 🔹 The **evaluated expression values** are **pushed on the stack**
* 🔹 The full formatted string is **built on the heap** (new object)
* 🔹 No "direct replacement" — Python constructs the result using runtime ops

---

## 🔚 Summary

| Style     | Fast | Readable | Supports Expressions | Recommended |
| --------- | ---- | -------- | -------------------- | ----------- |
| F-strings | ✅    | ✅        | ✅                    | ✅✅✅         |
| `.format` | 🟡   | ✅        | ❌                    | 🟡          |
| `%`       | ❌    | ❌        | ❌                    | ❌ (legacy)  |

---

> 💬 Pro Tip: Format strings are for humans. Keep them clean, keep them readable. No one ever got hired for `"%-08.2f"` alone.


