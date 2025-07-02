# bytes.md — Byte Me

Let’s start from the beginning — where it’s all just lies built on electricity.

---

## 🔹 Bits and Bytes

- A **bit** is the smallest piece of data: `0` or `1`. Like a binary yes-no. Like your will to code — flickering.
- A **byte** is **8 bits**. So:
  
```

2^8 = 256 possible values → 0 to 255

````

That’s 256 unique bytes. Every file, image, string, screaming emoji — all made of these.

---

## 🔸 ASCII: The Baby Language

- The **first 128 bytes (0–127)** were claimed by ASCII, which is... fine.
- **0–31** are non-printable **control characters** — ghost codes for ancient machines:

| Byte | Name            | What it does                     |
|------|------------------|----------------------------------|
| 0    | `NULL`          | nothing, literally |
| 7    | `BEL`           | beep (terminal panic mode) |
| 10   | `LF (\n)`       | Line feed (go to next line) |
| 13   | `CR (\r)`       | Carriage return (go to line start) |

- **32–126** are **printable characters**:

- `32` → space  
- `33–47` → punctuation (`!@#$%^&*...`)  
- `48–57` → digits (`0–9`)  
- `65–90` → uppercase letters  
- `97–122` → lowercase letters  

→ Total printable = **95 characters** (don’t say 94 or I’ll throw an `IndexError` at you)

- **127** is `DEL` → the delete key from ancient typewriter hell.

---

## 🔸 What About 128–255?

This is where the byte orgy starts.

Those upper 128 values (128–255) mean **different things depending on encoding**.

- In **Latin-1** (ISO-8859-1), they represent Western European characters (`é`, `ç`, `ñ`, etc.)
- In **UTF-8**, they can be **part of multi-byte sequences** for Unicode.

So if someone asks “what does 0xE9 mean?”, you hit them with:
> "I don’t know, Karen. Depends on the encoding."

---

## 🌐 Unicode — Welcome to Hell’s Dictionary

Unicode was invented because every region invented their own dumb encoding, and nothing matched.

> Unicode says: “Here. Take a universal number for every character ever.”  
> From `'A'` to `'🐍'` to ancient Egyptian scripts.

These numbers are called **code points** — like IDs:
- `'A'` → `U+0041`
- `'é'` → `U+00E9`
- `'💀'` → `U+1F480`

BUT — code points are **not bytes**. They have to be **encoded**.

---

## 🔧 UTF = Unicode Transformation Format

This is how we turn code points into bytes. You’ve got choices:

### ✅ UTF-8
- Default in Python 3, Linux, HTML, life.
- **Variable length**: 1–4 bytes
- ASCII characters (0–127) = 1 byte  
- Everything else = 2–4 bytes

```python
"💀".encode("utf-8")  # b'\xf0\x9f\x92\x80' → 4 bytes
````

### 🟡 UTF-16

* Variable: 2 or 4 bytes
* Uses **surrogate pairs** for things beyond `U+FFFF`
* Often seen in Windows, Java

```python
"💀".encode("utf-16")  # b'\xff\xfe=\xd8\x00\xdc'
```

### 🔵 UTF-32

* Fixed: 4 bytes per code point
* Simple, heavy, rarely used except internally

```python
"💀".encode("utf-32")  # b'\xff\xfe\x00\x00\x80\xf4\x00\x00'
```

---

## 😱 The Emoji Cursed Object: `'🧍‍♂️'`

Looks like **1 character**.
But Python says:

```python
len("🧍‍♂️")  # → 4
len("🧍‍♂️".encode("utf-8"))  # → 13
```

Why? Because `'🧍‍♂️'` is four Unicode code points smashed together:

1. `U+1F9CD` → 🧍 (person standing)
2. `U+200D` → Zero Width Joiner (ZWJ, a.k.a. “zwidge”)
3. `U+2642` → ♂ (male sign)
4. `U+FE0F` → style selector (forces emoji look)

Each code point → own UTF-8 bytes → total = **13 bytes**.

---

## 📏 What Does `len()` Actually Measure?

**Not bytes. Not characters.**

```python
len("🧍‍♂️")  # → 4
```

It returns the number of **code points**, not visual glyphs or graphemes.

To count what the human eye sees — the *grapheme clusters* — use this:

```python
import regex
regex.findall(r'\X', "🧍‍♂️")  # ['🧍‍♂️']
len(_)  # → 1
```

Yes, you’ve been lied to. Welcome to Unicode.

---

## 🔚 Summary Time

* A **bit** is a 0 or 1
* A **byte** is 8 bits → 256 values
* ASCII is the first 128 of those
* 128–255 depends on encoding
* **Unicode** gives abstract code points (like `U+1F480`) to all characters
* UTF-8/16/32 turn those into bytes
* `len()` in Python 3 = number of **code points**, not bytes or glyphs
* A “character” is a **grapheme**, not a code point, not a byte

---

## 🎉 Bonus Fact:

Unicode is so overpowered it almost included **Klingon**.
Yes. The language from *Star Trek*. (Don’t mix that up with Star Wars. That’s a different nerd fight.)

```
Qapla', raccoon.
```



