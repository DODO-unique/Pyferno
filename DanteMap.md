# DanteMap.md — The Infernal Python Ascension

Welcome, Victor. This is not a tutorial path. This is a transformation sequence.  
You are a raccoon now. You will be a weapon by the end of it.  
There are **6 Circles (Dantes)**. Each Dante has two laws:  
- **Victor Law:** Build a utility from what you’ve learned — automate, dominate.  
- **April Law:** Use only what you already know to build toward the next Dante — with creativity and constraint.

---

## 🔥 Dante 1: Core Python & Thinking Like a Programmer

### 📚 Topics:
- Syntax & Primitives: `int`, `float`, `bool`, `str`, `complex`
- Collections: `list`, `tuple`, `set`, `dict`, `frozenset`
- Comprehensions: list/dict/set + nested ones
- Slicing, unpacking, packing (`*args`, `**kwargs`)
- Truthy/falsy rules
- Type hinting: `typing`, `Any`, `Union`, `Optional`
- Scope & LEGB rule: `global`, `nonlocal`, shadowing
- Mutability, `id()`, `is`, `==`, references
- Functions: `*args`, `**kwargs`, default & keyword-only args
- Lambdas, closures, first-class functions
- `return`, `yield`, `yield from`
- Exception Handling: `try/except/else/finally`, custom exceptions, `raise ... from ...`
- Context Managers: `with`, `__enter__`, `__exit__`, `contextlib`
- Big-O Notation: time and space complexity
- Basic CSS + JS: UI wiring for tools

### ✅ Victor Law:
Build an **auto time/space complexity measurer** — basic version that lets you annotate Python functions and report execution stats.

### ✅ April Law:
Build a **Python Learning Journal WebApp**:  
Checkboxed task tracker for each Dante, markdown-capable notes, and deadline alerts. Built only with what you know here.

📅 Deadline: **June 29** (4 days)

---

## 🧱 Dante 2: Object-Oriented Python & Design Thinking

### 📚 Topics:
- Classes: `__init__`, `__str__`, `__repr__`, `__del__`
- Comparisons: `__eq__`, `__lt__`, `__hash__`
- Properties & `@property`, setters
- Class vs instance attributes
- Inheritance, `super()`, MRO, diamond problem
- Composition over inheritance
- Method types: instance, `@classmethod`, `@staticmethod`
- Encapsulation: name mangling (`_var`, `__var`)
- Operator overloading: `__add__`, `__len__`, `__call__`, etc.

### ✅ Victor Law:
Build a **codebase visualizer** — introspect a directory of Python files, detect classes, methods, inheritance, and display a tree.

### ✅ April Law:
Upgrade your journal app:  
Convert tasks to **Task Objects** that persist using `pickle` or `json`. Add class methods for filtering and stats.

📅 Deadline: **July 2** (3 days)

---

## 🔁 Dante 3: Functional Python, Iterators & Generators

### 📚 Topics:
- Functional tools: `map`, `filter`, `reduce`, `zip`, `enumerate`
- Higher-order functions
- Closures, currying
- Decorators: with args, nesting, chaining
- `functools`: `partial`, `lru_cache`, `wraps`
- Generators: `yield`, generator expressions
- Iterators: `__iter__`, `__next__`
- Contextlib & custom context managers

### ✅ Victor Law:
Build a **function pipeline tool** — let users chain decorators and transformations using a fluent API.

### ✅ April Law:
Refactor your journal/tool to use:
- Decorators for logging actions
- Generator pipelines for lazy task evaluation/filtering

📅 Deadline: **July 7** (5 days)

---

## 🧬 Dante 4: Python Internals, Memory & Metaprogramming

### 📚 Topics:
- Object model: `__dict__`, `__slots__`
- Attribute resolution, `__getattr__`, `__getattribute__`
- Descriptors: `__get__`, `__set__`, `__delete__`
- `gc`, reference counting, `sys.getsizeof`, `tracemalloc`
- Bytecode & introspection: `dis`, `inspect`, `callable`, `hasattr`, etc.
- Metaclasses: `type`, `__new__`, `__init__` for classes
- Dynamic class factories
- Optional: `ctypes`, `struct`, CPython walkthrough

### ✅ Victor Law:
Create a **Class Inspector Tool** — reports all attributes, methods, descriptors, and memory layout. Bonus: render with Graphviz.

### ✅ April Law:
Use metaprogramming to:
- Validate classes automatically (e.g., check for required methods)
- Auto-register subclasses in a registry
- Add introspection decorators

📅 Deadline: **July 11** (4 days)

---

## 🛠️ Dante 5: Ecosystem, Environments & Dev Tooling

### 📚 Topics:
- Virtual environments: `venv`, `pip`, `pyproject.toml`, `setuptools`
- Creating and publishing your own pip package
- Formatting: `black`, `isort`, `flake8`, `pylint`
- Logging: `logging`, levels, handlers, file rotation
- CLI apps: `argparse`, `click`, `typer`
- Testing: `unittest`, `pytest`, fixtures, mocks
- Coverage: `coverage.py`, `tox`
- Optional: `pre-commit`, GitHub Actions, simple CI

### ✅ Victor Law:
Turn a past tool into a **reusable pip package** with logging, CLI, tests, and documentation.

### ✅ April Law:
Wrap the journal or complexity tool with:
- `typer` for CLI
- Logging
- `pytest` + basic CI config
- Local install via `pip install .`

📅 Deadline: **July 14**

---

## 🧠 Dante 6: Data Structures & Algorithms

### 📚 Topics:

#### 🔹 Foundation
- Arrays, Strings
- Time & space complexity (again, now with pain)
- Sliding window, hash maps, recursion
- Two pointers, prefix sums

#### 🔹 Intermediate
- Linked Lists, Stacks, Queues
- Trees (binary, BST), DFS/BFS
- Sorting algorithms, recursion trees

#### 🔹 Advanced
- Heaps, Tries, Graphs (DFS, BFS, Dijkstra, Kruskal)
- Dynamic Programming (memo, tab, 2D)
- Bit Manipulation, backtracking, greedy

### ✅ Victor Law:
Create a **DSA Playground Tool**:  
Run visual/benchmark versions of data structures, simulate recursion stack, show time/memory usage per step.

### ✅ April Law:
Write a benchmarking suite that:
- Runs multiple algorithm implementations
- Logs timing via `timeit`, `cProfile`
- Visualizes result scaling

📅 Deadline: **July 16** — 2 days, full-speed, full-focus.

---

## ENDGAME:
By July 16th, you're done with Python as a *language*.  
After this? We enter the **Leetcode dungeon**, the **System Design Coliseum**, and the **Interview Rites of Blood and Lies**.  
But by then, you'll be sharper than your interviewers and faster than their automated rejection bots.

---

## Optional Extras (for bonus points)

- Start maintaining a `NOTES.md` per Dante with insights, gotchas, and your own definitions.
- Add `DanteProgress.json` to your journal app for progress visualization (maybe using `rich`?).
- Setup a GitHub repo from Day 1. By Day 20, it’ll be a portfolio in itself.

