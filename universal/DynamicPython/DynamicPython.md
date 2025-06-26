## 🧭 Index: The Dynamic Nature of Python

### **I. Variable & Typing Behavior**

1. Dynamic Typing: Variables are just labels
2. Mutability & Identity: `id()`, `is`, and object mutation
3. Rebinding vs Mutation: The nuance of `x =` vs `x.append()`

---

### **II. Object Introspection & Reflection**

4. `type()`, `id()`, `dir()`, `getattr()`, `hasattr()`, etc.
5. Inspecting callables: `__code__`, `__defaults__`, `__annotations__`
6. `locals()`, `globals()`, `vars()`: Contextual introspection

---

### **III. Execution of Code as Data**

7. `eval()`, `exec()`, `compile()`: Running strings as code
8. Dynamic imports: `__import__`, `importlib` and plugin patterns
9. Dynamic attribute access: `__getattr__`, `__setattr__`

---

### **IV. Class & Object Mutation**

10. Monkey Patching: Changing behavior at runtime
11. Class factories: Creating classes with `type()`
12. Metaclasses: Controlling class creation (`__new__`, `__init__`)
13. Dynamic inheritance: Changing MRO at runtime (yes, it's possible)

---

### **V. Callable Mutability**

14. Swapping function internals (`__code__`, `__closure__`)
15. Function and method decorators: Dynamic wrapping
16. Closures and runtime-defined functions

---

### **VI. Typing Implications & Chaos Control**

17. Duck Typing: Behavior over structure
18. Structural vs Nominal typing (preview of static contrasts)
19. Interface by convention vs enforcement (a.k.a. pray-and-code)

---

### **VII. Dangerous Powers**

20. Reflection hell: When too much knowledge kills
21. Dynamic code pitfalls: Security, performance, debugging
22. Dynamic vs Static: A head-to-head contrast
23. The road to Types: Gradual Typing and `typing` module (segue to Dante1)

---
