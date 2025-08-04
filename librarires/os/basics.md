For reference purposes

---

# 🌌 Python’s `os` Module

> **`os` is Python’s interface to the operating system.**
> Access the filesystem, environment, users, and process layer — all with one import.

---

## 📁 1. Filesystem & Paths

### 🔹 Basic Ops

| Function              | Description                          |
| --------------------- | ------------------------------------ |
| `os.getcwd()`         | Get current working directory        |
| `os.chdir(path)`      | Change current working directory     |
| `os.listdir(path)`    | List contents of a directory         |
| `os.makedirs(path)`   | Recursively create directories       |
| `os.remove(file)`     | Delete a file (not folders)          |
| `os.rmdir(path)`      | Delete an **empty** directory        |
| `os.rename(src, dst)` | Rename or move file/folder           |
| `os.stat(path)`       | Get file metadata (size, mtime, etc) |

> 🔥 To delete folders with content, use:
> `shutil.rmtree(path)`

---

### 🔹 Path Handling (`os.path`)

| Function               | Description                                |
| ---------------------- | ------------------------------------------ |
| `exists(path)`         | Path exists?                               |
| `isfile(path)`         | Is it a file?                              |
| `isdir(path)`          | Is it a directory?                         |
| `abspath(path)`        | Absolute path                              |
| `relpath(path, start)` | Path relative to another                   |
| `realpath(path)`       | Resolve symbolic links                     |
| `normpath(path)`       | Normalize path (remove `..`, `.` etc.)     |
| `normcase(path)`       | Normalize case + separators (Windows only) |
| `join(*paths)`         | Safely join path components                |
| `basename(path)`       | Final component of path                    |
| `dirname(path)`        | Directory portion of path                  |
| `split(path)`          | Tuple: (`dirname`, `basename`)             |
| `splitext(path)`       | Tuple: (`filename`, `extension`)           |
| `commonpath(paths)`    | Longest shared subpath in a list           |
| `sep`                  | Path separator (`/` or `\\`)               |

> 🔧 Use `os.path.abspath(__file__)` to get the **full path to your current script**.
> Useful when navigating relative directories safely.

---

### 🔍 Special Mentions

* `os.walk(path)` — Recursively yield `(root, dirs, files)`
* `os.scandir(path)` — Like `listdir()`, but returns objects with `.stat()`, `.is_dir()`
* `os.path.islink(path)` — Is this a symbolic link?
* `os.readlink(path)` — Get target of a symlink
* `os.symlink(src, dst)` — Create symbolic link (Admin/root permission on Windows)

---

## 🌱 2. Environment Variables

```python
os.environ["MY_SECRET"] = "123"             # Set variable (temporary)
print(os.environ.get("HOME", "Not set"))    # Read variable safely
```

* `os.environ` behaves like a dict
* ⚠️ **Changes apply only to the current process**
* Use for config, secrets, flags, etc.

---

## 🧑‍💻 3. User & Platform Info

| Function        | Description                |
| --------------- | -------------------------- |
| `os.getlogin()` | Current logged-in user     |
| `os.getuid()`   | User ID (Unix only)        |
| `os.name`       | OS type: `'posix'`, `'nt'` |
| `os.uname()`    | System info (Unix only)    |
| `os.path.sep`   | Path separator (`/`, `\\`) |

> 💡 Use `platform.system()` / `platform.release()` for more readable info

---

## ⚙️ 4. Process Management

| Function            | Description                            |
| ------------------- | -------------------------------------- |
| `os.system(cmd)`    | Run shell command (basic, blocking)    |
| `os.getpid()`       | Get current process ID                 |
| `os.fork()`         | Fork the current process (Unix only)   |
| `os.execvp(...)`    | Replace current process with a new one |
| `os.kill(pid, sig)` | Send signal to another process         |

> 🛑 For modern scripting, prefer:

```python
import subprocess
subprocess.run(["ls", "-l"])
```

---

## 🧪 Test Snippet: `os_test.py`

```python
import os

print(f"Current dir: {os.getcwd()}")

print("\nDirectory contents:")
for entry in os.listdir():
    print(" -", entry)

print("\nAbsolute path of this file:")
print(os.path.abspath(__file__))

print("\nEnvironment HOME:")
print(os.environ.get("HOME", "Not Set"))

print("\nPlatform type:")
print("Windows" if os.name == "nt" else "Unix-like")
```

---

## 🧩 Bonus: When to Use What?

| Task                       | Prefer                      |
| -------------------------- | --------------------------- |
| Copy/delete entire folders | `shutil` module             |
| Safer shell execution      | `subprocess.run()`          |
| Cross-platform sys info    | `platform` module           |
| Path handling (modern)     | `pathlib.Path`              |
| Path joining (legacy)      | `os.path.join(...)`         |
| Script-relative paths      | `os.path.dirname(__file__)` |

---

## ✅ Summary

* `os` is your bridge to the shell, filesystem, and system-level metadata.
* `os.path` is essential for cross-platform path logic.
* `shutil`, `subprocess`, and `pathlib` are modern, high-level alternatives.
* Avoid raw string-based path hacks. Use proper functions — they're battle-tested.

---
---
