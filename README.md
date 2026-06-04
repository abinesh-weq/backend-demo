# backend-demo

This is a minimal FastAPI demo project with a Hello API, Docker support, and a GitHub Actions workflow for CI/CD.

## Files

- `app/main.py`: FastAPI application with `/` and `/health` endpoints
- `requirements.txt`: Python dependencies
- `Dockerfile`: Builds the app container
- `docker-compose.yml`: Starts the app locally via Docker Compose
- `.github/workflows/deploy.yml`: CI/CD workflow that installs dependencies, runs tests, and builds the Docker image
- `tests/test_main.py`: Basic API tests

## Local run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   uvicorn app.main:app --reload
   ```
3. Open http://127.0.0.1:8000

## Docker run

1. Build the image:
   ```bash
   docker build . -t backend-demo
   ```
2. Run the container:
   ```bash
   docker run --rm -p 8000:8000 backend-demo
   ```

## Docker Compose

```bash
docker compose up --build
```
