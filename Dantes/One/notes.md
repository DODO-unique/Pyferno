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

### State, Context, Behavior

Imagine you're in a chemistry lab.
Now, before you panic—stay with me.

1. **State** is like a hydrogen atom. It knows its own stuff—electrons, energy levels, vibes.
2. **Context** is the environment around that atom. Is it floating inside a star? Chilling in water? Stuck in your high school exam?
3. **Behavior** is how the atom *acts* in that environment. In a star, maybe it fuses and releases energy. In water, maybe it chills with oxygen. You get the idea.

---

In code:

* **State** → The internal data of an object. What it *is* right now.
* **Context** → The surrounding environment during execution. Variables, scope, call stack, and mood.
* **Behavior** → The actions the object takes—what it *does*, especially when called or interacted with.

---

In short:

> **Behavior = f(State, Context)**

Or in raccoon terms:

> **How I act depends on what I carry and where I’m stuck.**

---