## Async (client & fastapi)

> Where JS and FastAPI show their teeth

---

### 1. The problem: stacking requests

* Hundreds of endpoints, clients firing requests fast → the server gets flooded.
* In a **synchronous/blocking** model: each request waits for the previous one to finish before moving on. That’s why queues bloat.

---

### 2. Async on the server

FastAPI (and async Python in general) handles this differently:

* You declare an endpoint `async def` instead of `def`.
* When a request hits an `async` endpoint that’s waiting for some I/O (DB query, API call), the server doesn’t block.
* The server **temporarily suspends that request**, moves on to handle other requests.
* When the awaited task completes, it resumes that request and returns the response.

Diagrammatically:

```
Request 1 → awaits DB → temporarily yields
Request 2 → executes while R1 waits
DB response → R1 resumes
```

So you never “stop the client,” but the server can handle many in-flight requests efficiently.

---

### 3. Async on the client

* JS (browser side) is **single-threaded**, but designed for async via `Promise` / `await`.
* Your mental model is correct: you can fire multiple requests, mark some as `await`, and continue doing other things while some responses are pending.
* The order of completion can be different from the order of requests—so your client code often **manages sequence explicitly** if order matters.

---

### 4. Why JS is considered “made for async”

* JS was designed for browsers, which are **I/O heavy** (network, user input, timers).
* Async (via event loop + promises) lets JS **never block the UI thread**, so the page stays responsive.
* Its power is exactly in handling multiple simultaneous asynchronous tasks efficiently.

---

### 5. FastAPI + async synergy

* On the server: `async def endpoint` + `await` I/O → many requests handled concurrently.
* On the client: `await fetch()` → request doesn’t block UI, multiple requests can be in-flight.
* The result: **end-to-end async flow**, non-blocking, scalable, but requires careful handling if response order matters.

---
