# FastAPI Production Starter 🚀

A production-ready FastAPI project template with:

* Clean folder structure
* Environment-based configuration (`pydantic-settings`)
* Async SQLAlchemy + Postgres (`asyncpg`)
* Alembic migrations
* Logging setup
* Testing with `pytest` + `httpx`
* Lint/format/type checks (Ruff + Black + MyPy)
* Docker + Gunicorn(Uvicorn workers) for production

---

## Project Structure

```
app/
  main.py
  api/v1/router.py
  core/config.py
  core/logging.py
  db/session.py
  db/base.py
  models/
  schemas/
  services/
tests/
alembic/
.env.example
```

---

## Requirements

* Python **3.11+**
* Postgres (local or Docker)
* (Optional) Docker / Docker Compose

---

## 1) Setup (Local)

### Create virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -U pip
```

**Mac/Linux**

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

### Install dependencies

```bash
pip install -r requirements.txt
```

> If you haven’t created `requirements.txt` yet:

```bash
pip freeze > requirements.txt
```

---

## 2) Environment Variables

Copy `.env.example` → `.env`

**Windows**

```bash
copy .env.example .env
```

**Mac/Linux**

```bash
cp .env.example .env
```

Example `.env.example`:

```env
APP_ENV=dev
PROJECT_NAME=FastAPI Prod
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/appdb
SECRET_KEY=change-me
CORS_ORIGINS=["http://localhost:5173"]
LOG_LEVEL=INFO
```

---

## 3) Run the App (Development)

```bash
uvicorn app.main:app --reload
```

API base:

* `GET http://localhost:8000/api/v1/health`

Docs (disabled in prod by default):

* `http://localhost:8000/docs`
* `http://localhost:8000/redoc`

---

## 4) Database + Migrations (Alembic)

### Initialize Alembic (only once)

```bash
alembic init alembic
```

### Create migration

```bash
alembic revision --autogenerate -m "init"
```

### Apply migrations

```bash
alembic upgrade head
```

---

## 5) Testing

```bash
pytest -q
```

---

## 6) Code Quality

### Lint

```bash
ruff check .
```

### Format

```bash
black .
```

### Type check

```bash
mypy app
```

---

## 7) Docker (Production)

### Build & run

```bash
docker build -t fastapi-prod .
docker run -p 8000:8000 --env-file .env fastapi-prod
```

### Production server (inside container / server)

Recommended command:

```bash
gunicorn -k uvicorn.workers.UvicornWorker app.main:app -w 2 -b 0.0.0.0:8000
```

> Tip: Put this behind Nginx/Caddy for TLS + compression + request limits.

---

## 8) Environment Behavior

* `APP_ENV=dev`
  ✅ docs enabled, easier debugging
* `APP_ENV=prod`
  ✅ docs disabled (recommended), tighter defaults

---

## 9) Common Commands (Quick)

```bash
# dev
uvicorn app.main:app --reload

# test
pytest -q

# migrations
alembic revision --autogenerate -m "change"
alembic upgrade head

# lint/format
ruff check .
black .
mypy app
```

---

## 10) Notes / Best Practices

* Never commit `.env` (keep `.env.example` in repo)
* Use strong `SECRET_KEY` in production
* Use proper CORS origins (don’t leave `"*"` in prod)
* Add Sentry / OpenTelemetry for monitoring in production
* Add rate-limiting if API is public
