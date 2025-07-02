exec=(statement_string, globals=None, locals=None)



# 🧾 Python Runtime Sorcery Notes: `eval`, `exec`, `compile`

---

## 🔮 `eval(expression, globals=None, locals=None)`

### ✅ Purpose:

* Evaluates a **single Python expression**
* Returns the **result**

### ✅ Syntax:

```python
eval("a + b", {"a": 1, "b": 2})  # → 3
```

### ✅ Use Cases:

* Calculators
* Dynamic expressions
* Safe scope-limited evaluations

### ⚠️ Restrictions:

* **Only expressions** (`3 + 4`, `"hello" * 2`, `lambda x: x`)
* No statements (`x = 5`, `def foo(): ...`)

### 🧠 Returns:

* Actual value (int, str, etc.)

### 🌐 Scoping:

* `globals`: Dict used as the **global scope**
* `locals`: Optional local override
* If omitted, uses current environment (`globals()` / `locals()`)

---

## 💣 `exec(code, globals=None, locals=None)`

### ✅ Purpose:

* Executes **any valid Python code**, including:

  * Assignments
  * Function/class definitions
  * Loops, conditionals, etc.

### ✅ Syntax:

```python
exec("x = 5\ny = x * 2", env)
print(env['y'])  # → 10
```

### ✅ Use Cases:

* Dynamic script execution
* Runtime function/class injection
* Code runners, REPLs

### ⚠️ Returns:

* **Always returns `None`**
* You must store state in `globals`/`locals` if needed

### 🌐 Scoping:

* `globals` dict is **required** to track variables (unless modifying real global scope)
* Without `env`, the created variables are lost unless declared at module level

---

## 🧪 `compile(source, filename, mode)`

### ✅ Purpose:

* Compiles **source string** to a Python **code object**
* Must be passed to `eval()` or `exec()` to run

### ✅ Syntax:

```python
code = compile("x + y", "<string>", "eval")
result = eval(code, {"x": 1, "y": 2})  # → 3
```

### ✅ Modes:

* `"eval"` → expects a single expression → for use with `eval()`
* `"exec"` → expects full code block → for use with `exec()`
* `"single"` → for REPL-style input (rare)

### ✅ Use Cases:

* Preprocessing code
* Dynamic code generation
* Function factories and interpreters

### ⚠️ Returns:

* A **code object**, not executed until passed to `eval()` or `exec()`

---

## 🔥 Summary Table

| Feature                       | `eval()`          | `exec()`            | `compile()`                  |
| ----------------------------- | ----------------- | ------------------- | ---------------------------- |
| Accepts                       | 1 expression      | Any code            | Any code (by mode)           |
| Returns                       | Expression result | `None`              | Code object                  |
| Can assign variables?         | ❌                 | ✅                   | ✴️ (with exec)               |
| Can define functions/classes? | ❌                 | ✅                   | ✴️                           |
| Needs `globals`/`locals`?     | Optional          | Often needed        | Always paired with exec/eval |
| Best for?                     | Quick evaluations | Full code execution | Runtime compilation          |

---

## 🧼 Best Practices

* Use `eval()` when you **need a result**
* Use `exec()` when you **need side effects** (variable defs, functions)
* Use `compile()` when you **want control** over delayed or analyzed execution
* Always **sandbox with `globals={'__builtins__': {}}`** if evaluating untrusted input
* Don’t use these unless you know why you're using them — **Python is giving you raw power**

---

## 🦝 Raccoon Wisdom

> `eval()` is the sniper — precise, single shot.
> `exec()` is the bomb — blows everything up.
> `compile()` is the forge — prepares weapons for later use.

---
## Extra Notes:
You're not misleading at all — in fact, **you’re 95% correct and articulating the core idea beautifully**, especially given how recent this knowledge is for you. That “dull” feeling is just your neurons **wiring runtime metaprogramming into long-term memory** — drink water, breathe, and let the brain reboot.

Let’s polish the final 5% so it’s *note-perfect* and won't backfire when revisiting:

---

## ✅ What You're Absolutely Right About:

### ✔️ When to use `globals` with `eval`

Your explanation:

> You only pass globals to eval when:
>
> * You want it to use variables not in the current real global scope
> * You want to mock or isolate the execution
> * You’re building tools where state is tracked externally

That’s **spot-on**.
Adding:

* `eval()` looks **only at globals**, unless you pass both `globals` and `locals`.
* If you pass just `globals`, it’s **used for both**.

---

## 🔧 Small Tweaks for Precision

### ❌ "`env` is kind of useless for `eval`"

Almost true, but here's the clean rewrite:

> `env` (custom dictionary) is **optional** for `eval`, and only useful when:
>
> * You want to evaluate in a **sandboxed or separate namespace**
> * You want to **inject custom values**
> * You don’t want the expression to access real global variables

So **it’s not useless**, just **not required** unless you're isolating or mocking the context.

---

## ✅ Why use a separate dictionary (`env`)?

You nailed it:

> 1. To assign a custom namespace
> 2. To avoid polluting real global scope
> 3. Because the function signatures accept them

Optional clarity boost:

> 4. To **capture what was created dynamically**, e.g., new variables or functions
> 5. To simulate **separate runtimes**, like an interpreter shell or REPL

---

## ✅ `exec(f"counter = {i}", env)` Logic Explanation

Perfect logic trail:

* `exec(...)` compiles and evaluates `"counter = i"`
* Python asks: “Where’s the global namespace?”
* You gave it `env`, so it mutates it: `env["counter"] = i`

Consider tightening this phrase just slightly for note clarity:

> It does **not** execute `env['counter'] = i` directly, but the effect is identical — it places `counter` into the dict you passed as `globals`.

---

## Extra Notes


### When should you pass globals to eval?

Use `globals` in `eval(expr, globals)` when:
- You want to run the expression in a separate scope (like a mock sandbox)
- You want to inject or control the variable context (e.g., `{"x": 5}`)
- You’re avoiding side effects in your real global namespace

So: `eval()` works fine without `env`, but it becomes powerful and safe **with** it in dynamic or external state tracking tools.

### Why create an external dictionary for exec/eval?

- To define a controlled namespace for your code
- To prevent polluting or overwriting real global variables
- To inspect, capture, or manipulate state programmatically
- Because `exec()` and `eval()` accept them as arguments

### How exec() affects the namespace:

```python
env = {}
for i in range(10):
    exec(f"counter = {i}", env)
    print(env['counter'], end=', ')
```

This works because:

* `"counter = {i}"` is first compiled into bytecode.
* PVM converts the bytecode into executable, and searches for a namesapce for `counter`
* given namespace is `env`, which is a dictionary
* `counter = {i}` is resolved as key-value pair in env

### Note:
- don't go smth = exec(smthelse), you'd look dumb with a NoneType
- answer = eval(smth) gives you legit answer though
- be careful how and where you use this. With great power comes...
- exec is not a function or an object
- eval is a object and a function
---

