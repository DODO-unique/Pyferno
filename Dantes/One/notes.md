### Python Interpreter and compilers

Python uses an interpreter to execute it's sauce code.
Interpreter (like CPython, written in C) firs compiles the sauce code into **bytecode** then this bytecode is ran in the PVM (python virtual machine).
Note that the PVM is also the part of the interpreter.

Compiler in C, C++, or Go, don't do that, they directly compile the entire sauce code and convert it into an executable- the kernel then runs this.

In the case of Java, Java uses a compiler in a sense that the bytecode is first compiled then the JVM (which acts as an interpreter) runs the bytecode.
But java is faster with JIT (and it's fancy modifications) becuse it enables Just In Time compiling- The frequently occuring codes simply get compiled ito executables by JIT simultaneously, on the fly. Python could do that if it were not so dynamic, though JIT does suffer with updating to more advanced features like Tiered JITs.

JIT works with Java and not python because it is relatively more static- python being ultra-dynamic one (which we will get to after this)

Note that python, being python, can't help itself with the JIT, so it's interpreter has more alternatives:

PyPy: This is JIT compiled python
Numba: JIT for numerical functions using LLVM
Cython: Compile Python to C for performance

But CPython, the default, doesn’t do JIT—because it can't safely assume anything stays the same.

---

## Types:
### Primitive Types: Six of them, all immutables

1. `int` is whole numbers, immutable- can't change it, if changed, it creates a new instance. Integer interns from -5 to 256- cached
2. `float` follow IEEE 754, decimal pointers, too precise for humans sometimes because `0.1 + 0.2 != 0.3`
3. `str`; array of unicode, basically. Immutable, if altered creates new instance of string.
4. `bool` subclass of `int`, intuitive, simply 0 and 1 wrapped in True and False.
5. `None` nonthing, ille, nada, nope. Singleton, represents void, and all that, we will get into details
6. `bytes` raw data good for those DSA byte problems. Juicy af

### `int`

* we will talk about how int works behind the scenes:
    ```c
    typedef struct {
    PyObject_HEAD   // Macro: includes ref count, type info, etc.
    long ob_digit[]; // Flexible array member holding the digits of the number
    } PyLongObject;
    ```
* Here, basically, we are storing long integers as different elements of array, where each element is a `long`.
* Python simply adds them up later. It looks like this:
    ```c
    2176782336 * (2^0) +
    287445236  * (2^30) +
    2          * (2^60)
    = original big number
    ```
* Here, each number is added to create a bigger number

### `float`

* It is a IEEE 754 double (IEEE is electrical engineering peeps. yeah.)
* precision is ~15-17 decimals
* 0.smth does not have a clean binary, so ... suffer this: `0.1 + 0.2 != 0.3` (it is actually `0.30000000000000004`)
* special values: float('inf') or float('-inf'), and float('nan') and nan = not a number, and `nan != nan`. yeah, how would nothing be equal to nothing? Because you have nothing to compare it to.
* Safer Alternative: decimal.Decimal, fractions.Fraction

###  `str` 

* A `str` in Python is a **sequence of Unicode code points**.
* These code points are compiled and loaded as **immutable** string objects.
* Despite being immutable, strings are **highly optimized** — slicing and copies are cheap at the C level.

---

### Slicing

> refer slicing.md in Dantes/Zero/code/

### 🔄 TL;DR:

* Slicing returns a new string
* Python internally uses `slice(start, stop, step)`
* `slice().indices(len)` normalizes `None` and negative values
* It's all sugar over a surprisingly smart mechanism

