# string methods: 47 of them

## The grand table:

| Method               | Description                                  |
| -------------------- | -------------------------------------------- |
| `capitalize()`       | First char uppercase, rest lowercase         |
| `casefold()`         | Aggressive lowercase (for caseless matching) |
| `center(width)`      | Center text in padded space (width=padding)  |
| `count(sub)`         | Count occurrences of `sub`                   |
| `encode()`           | Encode string to bytes                       |
| `endswith(suffix)`   | Check if string ends with `suffix`           |
| `expandtabs()`       | Replace `\t` with spaces                     |
| `find(sub)`          | Return first index of `sub`, or -1           |
| `format()`           | Format using `{}` placeholders               |
| `format_map()`       | Like `format()`, but uses a mapping/dict     |
| `index(sub)`         | Return index of `sub`, or raise `ValueError` |
| `isalnum()`          | True if all chars are alphanumeric           |
| `isalpha()`          | True if all chars are letters                |
| `isascii()`          | True if all chars are ASCII                  |
| `isdecimal()`        | True if all chars are decimal digits         |
| `isdigit()`          | True if all chars are digits                 |
| `isidentifier()`     | True if string is a valid Python identifier  |
| `islower()`          | True if all cased chars are lowercase        |
| `isnumeric()`        | True if all chars are numeric                |
| `isprintable()`      | True if all chars are printable              |
| `isspace()`          | True if all chars are whitespace             |
| `istitle()`          | True if each word starts with uppercase      |
| `isupper()`          | True if all cased chars are uppercase        |
| `join(iterable)`     | Join iterable with string as separator       |
| `ljust(width)`       | Left-align in padded space                   |
| `lower()`            | Convert to lowercase                         |
| `lstrip()`           | Remove leading whitespace (or chars)         |
| `maketrans()`        | Create translation table for `translate()`   |
| `partition(sep)`     | Split at first `sep` into 3-part tuple       |
| `removeprefix()`     | Remove a prefix if present (3.9+)            |
| `removesuffix()`     | Remove a suffix if present (3.9+)            |
| `replace(old, new)`  | Replace all `old` with `new`                 |
| `rfind(sub)`         | Find last index of `sub`, or -1              |
| `rindex(sub)`        | Like `index()`, but from the right           |
| `rjust(width)`       | Right-align in padded space                  |
| `rpartition(sep)`    | Split at last `sep` into 3-part tuple        |
| `rsplit(sep)`        | Split from right                             |
| `rstrip()`           | Remove trailing whitespace (or chars)        |
| `split(sep)`         | Split string into list by `sep`              |
| `splitlines()`       | Split at line breaks (`\n`, `\r\n`, etc.)    |
| `startswith(prefix)` | Check if string starts with `prefix`         |
| `strip()`            | Remove leading and trailing whitespace/chars |
| `swapcase()`         | Invert case of each character                |
| `title()`            | Capitalize first letter of each word         |
| `translate(table)`   | Replace chars using a translation table      |
| `upper()`            | Convert to uppercase                         |
| `zfill(width)`       | Pad with zeroes on the left to reach `width` |

## Some notable ones you prolly won't know:

1. maketrans() & translate()
2. partition(sep) & rpartition(sep)
3. rstrip and lstrip() - strip() itself has no arguments to strip only right or left
4. swapcase() - usecase
5. zfill()
6. removesuffix() and removeprefix()
7. startswith(prefix)
8. I feel lore in replace() there
9. casefold() vs. lowercase()
10. center(width) sounds like we can play with it, but isn't it like {value:^width}, note that there are two ways to center a line (good luck with div though lol)
11. find() vs. index()
12. format_map()
13. expandtabs() is so niche... I smell fishy here... like a big one
14. The `is` series has some good ones, like isdigit() vs. isdecimal(), also isprintable(), isidentifier() (The dynamic raccoon in me awakens), isspace(), let's like we needed that one

What else? Let us note that all methods are implemented in this format:

`"<string>".method(smth-if-anyth)` which will return list, or tuples, or strings- but always a new object, so we would note that.


### 1. maketrans() & translate()

maketrans():

syntax: `str.maketrans(x, y, z=None)`

    - `x`: string character to replace
    - `y`: string of replacement characters (should be same length as `x`)
    - `z`: characters to delete

This creates a map for translate to follow- so you create a translate object (a dictionary-like object; +1 space complexity) which is fed into translate()

translate():

syntax: `str.translate(trans_obj)` (gender reveal pending)

example: 

    ```python
    table = str.maketrans("abc", "123") # yeah, I don't blame you for thinking this is a extremist hashtag of rainbow
    # It replaces every occurrence of 'a', 'b', 'c' with '1', '2', '3' — position doesn't matter.
    translated = "abcabc".translate(table)
    print(translated) # output: 123123
    ```

You can also create a dictionary to make it more intuitive, just make know that `None` means delete and we are God.

    ```python
    table = str.maketrans({
        "a": "1",
        "b": "2",
        "c": None #deletes the c
    })
    s = "abcabc"
    print(s.translate(table)) #output: 1212
    ```
⚠️ Closing note: this only works with str, byte, and bytearrays
Talking about complexity:
for maketrans():
    
```python
table = str.maketrans("abc", "123")
```

* Takes two same-length strings
* Builds a **dict** mapping `ord(char) → ord(char)` (integers)
* Complexity:

* 🕒 Time: **O(k)** where `k = len(x)`
* 🧠 Space: **O(k)** (you store that mapping)

Tiny. Almost always negligible.

for translate():

```python
"abcabc".translate(table)
```

This is the real meat.

* Internally, it loops over **each character** in the input string
* For each char:

  * Looks up its Unicode codepoint in the table
  * Replaces, deletes, or copies

So:

* 🕒 Time: **O(n)** where `n = len(string)`
* 🧠 Space: **O(n)** because it builds a **new string**

> So yes — `translate()` is **O(n)**, both time and space.

### 2. partition(sep) & rpartition(sep)

partition(sep): creates a three-part tuple of the string, example:

```python
"hello=world".partition("=")
→ ('hello', '=', 'world')
```

rpartition(sep): creates three-part tuple but seperates at the last occurence of seperator

```python
"1+2+3".rpartition("+")
# gives ('1+2', '+', '3')
```

⚠️Note: rpartition() vs. rsplit: 

    - rpartition() is getting the last seperator and splitting from there
    - rsplit is completely different, it does not print the seperator itself, it does not only split once and it is controllable with maxsplit

    example:

```python
s = "a+b+c"
s.rpartition("+")
# → ('a+b', '+', 'c')

s.rsplit("+", 1)
# → ['a+b', 'c']
```

### 2.5 split(), rsplit() and the curious case of maxsplit

 `str.split(sep=None, maxsplit=-1)`
- Splits the string from **left to right**
- If `sep` is `None`, splits on **any whitespace**
- If `maxsplit` is provided, limits the **number of splits**, not parts
- Default `maxsplit = -1` means **no limit**

`str.rsplit(sep=None, maxsplit=-1)`
- Same as `split()`, but works from **right to left**
- Useful when you care about **suffixes**, **file extensions**, **trailing content**

What is `maxsplit`?
- It controls the **maximum number of times the string is split**, not the number of chunks
- Example:
    ```python
    "1+2+3+4".rsplit("+", 2)
    # → ['1+2', '3', '4']
    ```
    - Split twice from the right: 
      - First: at last `'+'` → `'4'`
      - Second: next `'+'` → `'3'`
      - What's left: `'1+2'`

⚠️ Edge Case: maxsplit = 0
- No splits happen:
    ```python
    "a+b+c".split("+", 0)
    → ['a+b+c']
    ```

Difference from `partition()`/`rpartition()`:
- `split()` and `rsplit()` return a **list**, separator is removed
- `partition()` and `rpartition()` return a **3-tuple**, separator is preserved

---

TL;DR

| Method         | Returns | Direction     | Keeps Separator | Maxsplit |
|----------------|---------|---------------|------------------|----------|
| `split()`      | list    | Left → Right  | ❌ No             | ✅ Yes   |
| `rsplit()`     | list    | Right → Left  | ❌ No             | ✅ Yes   |
| `partition()`  | tuple   | First Match   | ✅ Yes            | ❌ No    |
| `rpartition()` | tuple   | Last Match    | ✅ Yes            | ❌ No    |


### 3. `strip()`, `lstrip()`, `rstrip()` — The Whitespace Mafia

#### `str.strip([chars])`
- Removes leading & trailing characters (default: whitespace)
- if `chars` is not passed: removes all whitespaces, leading and trailing
- If `chars` is passed: removes **all matching characters** (leading and trailing), not substrings
- Returns a **new string**

#### `str.lstrip([chars])`
- Same as `strip()`, but only from **left**

#### `str.rstrip([chars])`
- Same as `strip()`, but only from **right**

#### Examples:
```python
"  hello  ".strip() → "hello"
"<<hello>>".strip("<>") → "hello"
"abcabc123abc".strip("abc") → "123"
"banana".strip("ab") → "nan"
```

🧠 Remember: `"abc"` is treated as a **set**, not a pattern or substring

### 4. swapcase()

Simply swap the case. that's it.

Like `"heLow".swapcase()` gives you HElOW

that's it. That's all it does.

internally, it is simply doing
`.islower()` -> `.upper()`
`.isupper()` -> `.lower()`

### 5. zfill(width)

Pads the string with zeroes on the **left**, until the **total string length is `width`.**

- Sign characters (`+` or `-`) are preserved and padding comes **after** them
- Returns a **new string**

#### Examples:
```python
"42".zfill(5)     → "00042"
"-42".zfill(5)    → "-0042"
"hello".zfill(8)  → "000hello"
```

### replace(old, new, count=-1)

returns a new string after replacing all (or some) old occurences with the new ones

`str.replace(old, new, count=-1)`

Here:
    - `old`: substring to be repaced
    - `new`: substring to be inserted
    - `count`: Number of replacements to make; default=-1 (replace all)

examples:
```python
"raccoon".repalce('co', '🦝')
-> "rac🦝on"

# so, yeah, just replacing it
```

Simply moves over the string and finds old, replaces it as it finds it. Stops when the strings end or `count` is exhausted
This is highly optimized in C so faster in general than a loop. So method > brute force.

### casefold()

This is just aggresive .lower(), unlike .lower() though, .casefold() is not engish biased and used for unicode universally.

So imagine this for other languages as well, for example:

```python
"Straße".casefold() == "strasse".casefold()  # → True
"Maße".casefold() → "masse"
"ß".lower() → 'ß'     |   "ß".casefold() → 'ss'
```

### center(width)

### 🔧 Syntax:

```python
str.center(width, fillchar=' ')
```

* Centers the string in a field of length `width`
* Pads with `fillchar` (must be **one character**)
* Default is space
* Returns a **new string**

---

### 🧪 Example:

```python
"hello".center(11)         → '   hello   '
"hello".center(11, "-")    → '---hello---'
"hi".center(6, "*")        → '**hi**'
```

If the padding is odd, **left gets more**:

```python
"hi".center(5, "-") → '-hi--'
```

---

### find() vs. index()

Both are the same, simply, find() gives -1 as a return when nothing is found, index() gives a ValueError

`string.index(substring, start, end)`
`string.find(substring, start, end)`

substring is for what you want to find, start/end are optional and define the range of search with relevant index

### format_map()

This is interesting, so the syntax goes like this:

syntax: `.format_map(mapping)`

now, mapping accepts the objects that implement __getiem__(). But it does not accept tuples or lists

#### 🔎 Why `format_map()` doesn't accept lists or tuples (despite supporting `__getitem__()`)

While lists and tuples do implement `__getitem__()`, they **don't behave like mappings**.

`format_map()` expects a **mapping-type object** — one where `__getitem__()` accepts **string keys**, as in:

```python
mapping["key"]
````

But:

```python
my_list["key"]  # ❌ TypeError: list indices must be integers or slices
```

So even though sequences are technically "gettable," they are **not key-based containers**. `format_map()` tries to access:

```python
mapping["some_placeholder_name"]
```

If your object can’t handle that, it crashes. So we use dict or defaultdicts or even custom objects are fine.

#### ✅ Works:

```python
data = {"name": "Victor"}
"{name}".format_map(data) # → "Victor"
```

#### ❌ Fails:

```python
values = ("Victor",)
"{0}".format_map(values)  # → ❌ TypeError
```