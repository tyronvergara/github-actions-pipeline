# GitHub Actions Pipeline

A minimal FastAPI service used as a **vehicle to practice a real CI/CD pipeline** with GitHub Actions - linting, containerization, and automated publishing to a container registry.

> **The API itself is intentionally simple.** The point of this repository isn't the application code - it's the pipeline around it: what triggers it, what it validates, and what it ships.

---

## What the pipeline does

Every pull request and every push to `main` triggers [`.github/workflows/main.yml`](.github/workflows/main.yml), which runs three jobs:

| Job | Runs on | What it does |
|---|---|---|
| `dockerfile-linter` | PR + push | Lints the `Dockerfile` with [Hadolint](https://github.com/hadolint/hadolint) |
| `python-linter` | PR + push | Lints `main.py` with [Pylint](https://pylint.readthedocs.io/) |
| `build-and-push` | push to `main` only | Builds the Docker image and publishes it to [GHCR](https://ghcr.io) |

The `build-and-push` job only runs on `push` - not on pull requests - so images are only published once code has actually landed on `main`.

```
Pull Request  ->  dockerfile-linter
                   python-linter

Push to main   ->  dockerfile-linter
                    python-linter
                    build-and-push  ->  ghcr.io/tyronvergara/mini-api
```

---

## The application

A small FastAPI service with two endpoints:

- `GET /` - returns a hello-world message
- `GET /status` - healthcheck endpoint

That's it. The application layer is deliberately thin so the pipeline stays the focus of the repository.

---

## Stack

- **FastAPI** - web framework
- **Docker** - containerization
- **GitHub Actions** - CI/CD orchestration
- **Hadolint** - Dockerfile linting
- **Pylint** - Python linting
- **GHCR (GitHub Container Registry)** - image hosting

---

## Running locally

```bash
docker build -t mini-api .
docker run -p 8000:8000 mini-api
```

The API will be available at `http://localhost:8000`.

---

