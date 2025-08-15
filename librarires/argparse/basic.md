Excellent. These two are foundational to any serious CLI script.

---

## 1. ⚔️ `argparse` Rundown

`argparse` helps you **define command-line arguments** and **parse them into Python objects**.

Basic setup:

```python
import argparse

parser = argparse.ArgumentParser(description="What your program does.")

# Positional argument (required)
parser.add_argument("path", help="The path to operate on")

# Optional argument
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

# Parse command line into `args`
args = parser.parse_args()

print(args.path)       # access positional arg
print(args.verbose)    # True if --verbose is passed
```

---

### 🪬 Notes:

* `add_argument("name", help="...")` → required positional argument
* `add_argument("--flag", ...)` → optional, usually boolean or with default
* `action="store_true"` → makes the flag behave like a switch (`True` if passed)
* `type=int` or `type=float` → convert automatically
* `default="value"` → fallback if not passed

You get back an `argparse.Namespace` object, basically a lightweight container with `.argname` attributes.

---
