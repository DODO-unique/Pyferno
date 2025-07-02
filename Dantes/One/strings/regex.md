## 🧠 Regex Reference Guide (Sanity Edition)

Welcome to the Regex Sanctum — where symbols are explained, trauma is tamed, and `.*?` is finally understood.

---

### 🧱 Anchors

| Symbol | Meaning                                     |
| ------ | ------------------------------------------- |
| `^`    | Start of string (or line in multiline mode) |
| `$`    | End of string                               |

---

### 🔍 Character Classes

| Symbol | Matches                          |
| ------ | -------------------------------- |
| `.`    | Any character (except `\n`)      |
| `\w`   | Word char: `[a-zA-Z0-9_]`        |
| `\W`   | Non-word char: `[^\w]`           |
| `\d`   | Digit: `[0-9]`                   |
| `\D`   | Non-digit                        |
| `\s`   | Whitespace (space, tab, newline) |
| `\S`   | Non-whitespace                   |
| `\b`   | boundary between \w and \W       |

---

### 🎯 Quantifiers

| Symbol  | Meaning         |
| ------- | --------------- |
| `*`     | 0 or more       |
| `+`     | 1 or more       |
| `?`     | 0 or 1          |
| `{n}`   | Exactly n       |
| `{n,}`  | n or more       |
| `{n,m}` | Between n and m |

> ⚠️ Quantifiers are **greedy** by default — they match as much as possible.
> Use `*?`, `+?`, `??`, etc. for **non-greedy** (aka lazy) versions.

---

### 📦 Groups & Ranges

| Symbol          | Meaning                           |
| --------------- | --------------------------------- |
| `(...)`         | Capturing group                   |
| `(?:...)`       | Non-capturing group               |
| `(?P<name>...)` | Named group                       |
| `[...]`         | Character set                     |
| `[^...]`        | Negated character set (not these) |
| `[a-z]`         | Range: lowercase a–z              |

---

### 🔗 Logic & Lookarounds

| Symbol     | Meaning                           |                  |
| ---------- | --------------------------------- | ---------------- |
| \`         | \`                                | OR (alternation) |
| `(?=...)`  | Lookahead (assert what follows)   |                  |
| `(?!...)`  | Negative lookahead                |                  |
| `(?<=...)` | Lookbehind (assert what precedes) |                  |
| `(?<!...)` | Negative lookbehind               |                  |

---

### 🧪 Common Examples

* Match an email: `\b[\w.-]+@[\w.-]+\.\w+\b`
* Match a URL: `https?://[^\s]+`
* Match a number: `[-+]?\d*\.?\d+`
* Match a hashtag: `#\w+`
* Match a word with optional `'`: `\b\w+(?:'\w+)?\b`

---

### 🛠 Regex in Python

```python
import re
re.match(pattern, string)      # The start until it doesn't
re.fullmatch(pattern, string)  # entire match
re.search(pattern, string)     # First match
re.findall(pattern, string)    # All matches
re.sub(pattern, repl, string)  # Replace matches
re.compile(pattern)            # Compile for reuse
```

Use **raw strings**: `r'\d+'` to avoid hell with double escaping.

---

### ⚠️ Anti-Trauma Tips

* ❌ Don’t parse HTML with regex — use a parser (e.g. BeautifulSoup)
* ✅ Use `.compile()` when reusing patterns repeatedly
* ✅ Test patterns on [regex101.com](https://regex101.com/)
* 🔍 Anchor your regex with `^...$` if you want full-line validation

