## 🧠 The `random` module in Python

```python
import random
```

This imports the pseudo-random number generator. *Pseudo*, because nothing is truly random—Python uses a deterministic algorithm seeded from your system clock or entropy pool.

---

### 🎲 BASIC RANDOMNESS

#### 1. `random.random()`

Returns a float in the range `[0.0, 1.0)`.

```python
random.random()  # e.g. 0.732773
```

#### 2. `random.uniform(a, b)`

Returns a float between `a` and `b`.

```python
random.uniform(5, 10)  # e.g. 7.2841
```

#### 3. `random.randint(a, b)`

Returns an integer between `a` and `b`, **inclusive**.

```python
random.randint(1, 6)  # simulates a die roll
```

#### 4. `random.randrange(start, stop[, step])`

Like `range()`, but picks one value randomly.

```python
random.randrange(0, 10, 2)  # could return 0, 2, 4, 6, or 8
```

---

### 🎴 CHOICE, SHUFFLE, AND SAMPLE

#### 5. `random.choice(seq)`

Pick a single element from a non-empty sequence.

```python
random.choice(['apple', 'banana', 'cherry'])
```

#### 6. `random.choices(seq, k=n)`

Return a list of `n` elements *with replacement*. Can have duplicates.

```python
random.choices(['red', 'green', 'blue'], k=2)
```

#### 7. `random.sample(seq, k=n)`

Returns `n` unique elements. **No replacement**.

```python
random.sample(range(100), 5)  # 5 unique numbers
```

#### 8. `random.shuffle(seq)`

Shuffles a sequence **in-place**.

```python
deck = [1, 2, 3, 4]
random.shuffle(deck)  # modifies deck
```

---

### 🎰 CONTROLLING THE CHAOS

#### 9. `random.seed(x)`

Sets the seed for reproducibility.
Same seed = same random sequence.

```python
random.seed(42)
```

Use this when you're debugging or want deterministic output.

