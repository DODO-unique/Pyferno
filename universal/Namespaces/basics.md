### NameSpace

NameSpace is a semi-isolated space withtin a code where actions take place.

There are four major NameSpaces:
    1. Global
    2. Local 
    3. Enclosing
    4. Built-in

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