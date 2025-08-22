# Branching Recursion & Call Stack Notes

### 1. Call Stack Basics

* In Python, **a single thread has one call stack**.
* A single process has one call stack assigned.
* The call stack holds the **outer scope** (global or any scope).
* **Classes/methods are defined in the call stack**, but nothing executes until they are called.
* Calling something (function, method, etc.) **pushes a new stack frame**.
* If a program has no functions, **Python treats the top-level code as `main()`**, so even that runs in a call stack.

### 2. Stack Frames & Recursion

* Each function call creates a **stack frame**, storing local variables, parameters, and instruction pointer.
* **Recursion:** every recursive call adds a new stack frame.
* **Linear recursion:** stack frames keep stacking until the base case, then pop in reverse order.
* **Branching recursion (binary/nonlinear):**

  * Python doesn’t resolve branches simultaneously.
  * Picks one branch (e.g., left), fully resolves it linearly, then moves to the next branch (e.g., right).
  * Conceptually, this forms a **tree**, but actual execution is linear.
  * Each branch = a **linear stack**, waiting for its sub-stacks to resolve before returning.

### 3. Branching Example (Subsets)

* Each element: **include or exclude** → creates two branches.
* Each branch adds frames for recursive calls linearly.
* When base case is reached, frames start popping and results combine.

### 4. Multi-threading & GIL

* **GIL (Global Interpreter Lock)**: a mutex → only **one thread executes Python bytecode at a time** in a process.
* Prevents clashes on shared resources.
* **Threads**: each thread has its own **call stack**, but execution is one at a time due to GIL.
* **Processes** (multiprocessing):

  * Each process has its **own memory space, GIL, and call stack**.
  * True parallel execution possible.
* **Analogy:** running multiple Python files as separate processes is similar—each can execute truly concurrently.
* Other languages:

  * Rust → fearless concurrency, safe via ownership rules.
  * C++ → true multithreading, but you manage memory and synchronization.

### 5. Key Mental Models

* **Branching recursion:** a tree of logical branches, executed as **linear stacks one at a time**.
* **Stack frame = local context of function call.**
* **Threads vs processes:** threads share memory but GIL restricts Python bytecode execution; processes are independent.

---