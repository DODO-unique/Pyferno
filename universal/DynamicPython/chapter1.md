
### Python Variables, Types, and Identity

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

* these things use same  space, different identifiers point to them
* `int` from `-5 to 256`
* some strings, `None`, `True`, etc.

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

---

### Deepcopy vs Copy

* `copy.copy(x)` → shallow copy (references internals)
* `copy.deepcopy(x)` → full clone (new instances), unless immutable

```python
x = [1, 2]; y = copy.copy(x)     → y is not x, but y[0] is x[0]
x = (1, [2]); y = deepcopy(x)    → both tuple & list are new
```

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

