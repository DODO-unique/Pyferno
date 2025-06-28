### 🧠 Chapter II: Introspection & Reflection (Dante Level 2: Identity & Metaprogramming)

---

### 🔹 What is Introspection?

> **Introspection** is the act of examining an object at runtime to learn about its type, attributes, methods, and structure.

#### 🔸 Core Tools:

| Tool                                       | Purpose                              |
| ------------------------------------------ | ------------------------------------ |
| `type(obj)`                                | Returns the class/type of `obj`      |
| `id(obj)`                                  | Returns the memory identity          |
| `obj.__class__`                            | Explicit class reference             |
| `obj.__dict__`                             | Instance's internal namespace        |
| `type(obj).__dict__`                       | Class-level namespace                |
| `dir(obj)`                                 | Lists all attributes (incl. dunders) |
| `hasattr`, `getattr`, `setattr`, `delattr` | Dynamic attr access                  |
| `callable(obj)`                            | Is this thing callable?              |
| `isinstance(obj, T)`                       | Is obj an instance of type T?        |
| `issubclass(A, B)`                         | Is A a subclass of B?                |

---

### 🔹 What is Reflection?

> **Reflection** allows **modifying** the object/class/program *at runtime*, not just inspecting.

#### 🔸 Reflection Tools:

| Tool                      | Purpose                              |
| ------------------------- | ------------------------------------ |
| `setattr(obj, name, val)` | Dynamically adds/modifies attribute  |
| `delattr(obj, name)`      | Removes attribute                    |
| `type(name, bases, dict)` | Dynamically creates a class          |
| `__import__('mod')`       | Dynamically imports a module         |
| `globals()` / `locals()`  | Access current namespaces            |
| `exec()`, `eval()`        | Execute strings as code (🧨 careful) |

---

### 🔹 Special Attributes to Know:

| Dunder       | Meaning/Usage                                   |
| ------------ | ----------------------------------------------- |
| `__doc__`    | Docstring of class/function/module              |
| `__module__` | Name of module where class/function was defined |
| `__class__`  | The object's class                              |
| `__dict__`   | Namespace dictionary of object/class            |
| `__name__`   | Often used on functions/modules                 |

---

### 🔹 Reflection in Action: Example

```python
class Foo:
    """Example class"""
    def greet(self): return "Hi"

f = Foo()
setattr(f, "sniffed", True)
print(getattr(f, "sniffed"))         # True
print(f.__class__.__module__)        # '__main__'
print(f.__doc__)                     # "Example class"
```

---

### 🔹 Why It Matters (FAANG Angle):

* You *can't* build frameworks, serializers, or decorators without introspection.
* Libraries like `dataclasses`, `pydantic`, `sqlalchemy`, `Django`, `Flask` all rely on this.
* Python metaprogramming = soft magic. Learn it, control it.

---

### 🔹 TL;DR Summary:

✅ Use `type`, `dir`, `__dict__`, `__module__`, and `__doc__` to **inspect**.
✅ Use `setattr`, `type()`, and dynamic class creation to **reflect**.
✅ You’re no longer using Python—you’re *bending* it.

---

### suggested tasks
    Please, for the love of god, create a extension of this md which will contain whatever new introspections/reflections you learn. I am too lazy to do it rn