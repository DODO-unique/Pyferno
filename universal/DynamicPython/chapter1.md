
### I: Python Variables, Types, and Identity

Python uses **identifiers** (not variables) to bind names to objects in a namespace. All values are **instances of classes**. Even primitives like `int`, `str`, `None`.

**Assignment** is **binding**: `x = 5` binds `x` to an `int` object(5).  
**Rebinding** replaces that reference: `x = 'hello'` → now `x` points to a `str`.

---

### Identity, Equality, and Memory

- `==` → value equality (`__eq__`)
- `is` → identity (object in memory, `id()`)

```python
a = 257; b = 257 → a is b ❌  #(outside int cache range)
a = 10; b = 10   → a is b ✅  #(within cache)
```

Python **interns**:

*CPython optimizes memory by reusing immutable objects like small integers (-5 to 256) and some strings, so different identifiers may point to the same memory address

---

### Mutable vs Immutable

* **Immutable**: `int`, `str`, `tuple`, `float`, etc.
  Changing value → new instance created.

* **Mutable**: `list`, `dict`, `set`, etc.
  In-place modification affects all references.

```python
x = [1, 2]; y = x; x += [3] → y also changes
x = x + [4]                → new list, `x` rebinding only
```

⚠️ Note that `x = x + [4]` is rebinding a mutable list, and `x += [3]` is mutating it (so y changes too)

Here `x = x + [4]` triggers as `x.__add__([4])`, which adds the element in the arguments to the object- 
  - so you see, x (variable) is an instance of class `list` here and,
  - `.__add__([4])` is a dunder to that object.
  - `.__iadd__()` is a dunder that modifies mutables in place
  - `+=` triggers the `.__iadd__()` dunder, which mutates the list in place

---

### Deepcopy vs Copy

* `copy.copy(x)` → shallow copy (references internals)
* `copy.deepcopy(x)` → full clone (new instances), unless immutable (because why would you create a deepcopy of an immutable?)

```python
x = [1, 2]; y = copy.copy(x)     → y is not x, but y[0] is x[0]
x = (1, [2]); y = deepcopy(x)    → both tuple & list are new
```

## About immutable and deepcopy

* Immutables are... immutables, they can't be changed, no matter what you do- 
* Most primitive types (like int, str, etc.) are immutables
* If immutables can't be changed, identifiers with same immutables won't have to be different
* Thus, having some cache makes sense- thus interning comes into play

---

### Garbage Collection (CPython)

Python deletes objects when **refcount = 0**.
`x = 5; x = 'a'` → if no one else points to `5`, it is GC’d.

---

### Metaclass and `type`

`type(obj)` → class of obj
`type` itself is the **metaclass of all classes**.
Custom metaclasses inherit from `type`.

```python
class Meta(type): ...
class A(metaclass=Meta): ...
```

Metaclass defines class creation behavior (`__new__`, `__init__`).

---

### Function Default Pitfall

```python
def f(x=[]): x.append(1); return x
f(); f(); f() → [1, 1, 1]
```

Default mutable args persist between calls. Use `None`:

```python
def f(x=None): x = [] if x is None else x
```

⚠️ Note that this is happening because default values are evaluated **once** at function definition, not again. Well, that is the damn point of this section- why does this feel misplaced now, prolly add it in functions part in Dante 1 point 3 Funtions and Call Mechanics.

---

### TL;DR

* **Everything is an object**
* **Assignment binds**, doesn’t copy
* **Mutability defines behavior**
* `is` ≠ `==`
* Deepcopy = new instances (unless immutable)
* `type` = metaclass; everything comes from it
* CPython uses refcount GC, with interning for small ints/strings

> Know this, and no FAANG interviewer can shake your fur loose.

