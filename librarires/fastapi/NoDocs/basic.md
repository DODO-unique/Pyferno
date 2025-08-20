# Essence of FastAPI

FastAPI isn’t magic—it’s just Python telling the web: *“Here’s how you want me to talk to the outside world.”*
At its core, FastAPI does three things:

1. **Routing & Request Handling** – Define endpoints (URLs) and what happens when someone hits them. Example: GET `/users` → fetch users, POST `/login` → check credentials. FastAPI maps requests to your Python functions automatically.* 

2. **Validation & Serialization (Pydantic)** – FastAPI checks that incoming data matches the expected structure and types, then converts it into Python objects. Returning a Pydantic model automatically produces JSON for the client. No manual parsing or serialization needed.

3. **Asynchronous Support & Performance** – Built on Starlette + async Python. You can write async endpoints that handle many requests simultaneously without blocking, useful for high-traffic APIs.

**Extras:**

* **Auto docs:** `/docs` and `/redoc` endpoints appear automatically, describing your API.
* **Dependency Injection:** reusable chunks like DB connections or auth checks plug into endpoints automatically.

**In short:** FastAPI is a modern, Pythonic way to turn functions into network-accessible APIs, handling validation, serialization, and async stuff with minimal boilerplate.

> ***Note: You can have your own endpoints, clients get to pick what endpoints they are serving**
> Technically, the relevant logic resides under the relevant endpoints
---

## Frontend ↔ Backend Interaction

**1. Frontend (browser):**

* You open `index.html` (or serve it via FastAPI).
* JS/CSS handle display and interaction.
* User actions trigger requests via `fetch()` or `axios`.

**2. Backend (FastAPI/Python):**

* FastAPI endpoints like `/calculate`, `/users`, `/upload` receive requests.
* Input is validated with Pydantic, logic runs, DB access happens if needed, response is returned.
* JS receives the response and updates the DOM.

**Flow diagram:**

```
[Browser/JS] --> sends request --> [FastAPI Endpoint] 
            --> validates & executes Python logic 
            --> returns JSON response --> [Browser/JS] 
            --> updates HTML/CSS
```

---

## Pydantic: The Data Bouncer

Pydantic defines structured models for your data:

* You define a `BaseModel` with fields and types.
* Incoming JSON/dict is validated and turned into a Python object.
* Returning a Pydantic model serializes it to JSON automatically.

Think of it as **Python-side rules for data**, while SQLAlchemy is **DB-side rules**. Pydantic doesn’t touch the database.
Using Pydantic models consistently makes your backend modular, scalable, and easier to reason about.  

> In essence, this is similar to SQLalchemy models which also translates and maps ORM codes to SQL (recall that the Engine handles the actual dialect nuances- yeah, that's got nothing to do here, was just helping you recall 🧍‍♂️)

---
