Put this somewhere in the dictionaries or the sets to be sure. Or both, don't mind


This hashing is not cryptography hashing, remember that.

The key concept is to take a hashable object (an object that supports __hash__() method- so mutables are shown the middle finger) and convert it into a number (let's call it Shivali [dad suggested that name])
Shivali is then stored at an empty index.
When user needs Shivali's value, `hash % hastable size` is done, this gives the index of Shivali.
Shivali is a rare name, but not unique, just like in real world. How many girls have you met with that name, hm? That's right.

So, say when you are creating a hash, of 'cat' and it collides (is same as) 'act'.
    This is a case of collision. In this scenario, when storing the hash, the machine checks what index to give the hash, sees that there is already a value there with same hash.
    The machine then sighs and goes `i + 1**2` (where i is the index), so it checks the next place in index, if even that is full, it groans and goes `i + 2**2` and there it stores it's shit- if even that is not empty then ... god bless the python VM, it continues.

Later, when finding, the guy simply takes the object, hashes it, goes `hash % hashtable size`, gets the index, goes to the index and operates, or returns to the function. 
If, the value is not same (through __eq__()), then move on with `i + 1**2` and so on till you find it.

The `i + 1**2` ... thingy? That is called Quadratic Probing 

This table helped my understanding:

```sql
+-------+----------+----------+-------------+
| Index |   Hash   |   Key    |   Value     |
+-------+----------+----------+-------------+
|   0   | 80345312 |  "cat"   |   "meow"    |
|   1   | 18293591 |  "dog"   |   "bark"    |
|   2   |          |  EMPTY   |             |
|   3   | 80345312 | "act"    |   "verb"    |  ← collision with "cat"
|   4   |          |  EMPTY   |             |
|   5   | 45033482 |  "fox"   |   "sneaky"  |
+-------+----------+----------+-------------+
```

A quick fact about [Sets](link sets here), Sets are dictionaries but with values ignored.
For example, a set like:
```py
set1 = {1, 2, 3}
```
is nothing but:
```py
{1: True, 2:True, 3:True}
```

So, 

As mentioned in [tuples](..\..\Dantes\One\tuples\internals.md), tuples with mutable elements are not hashable.


Note that probing itself is a very complicated process mathematically, here is how perturbing helps make it sharper:

### **Raccoon Drama**

1. **You (Victor) hash to 3.**
   Bin 3 is empty. You dump your mango peels there. Easy.

2. **Shivali the raccoon hashes to 3 too.**
   Collision. Bin 3 is full. She sighs and starts **perturbed probing**:

   * Start with `i = 3`, `perturb = hash(Shivali)`.
   * New index: `j = (3 * 5 + 1 + perturb) & 15`.
   * She lands at, say, bin 10. Bin 10 is free, she dumps her rotten litchis there.

3. **Another raccoon, “Trashlord”, also hashes to 3.**
   Now he has to follow the same dance:

   * Start at 3, sees it full, then hops like a lunatic across bins (`i = (i * 5 + 1 + perturb) & 15`, shifting `perturb` each time) until he finds a free one.

bit of 15 is 1111, which means the next is just 10000, so technically 
