FROM python:3.13-bullseye AS base

# Set environment variables for Python and Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PROJECT_DIR="/app"

# Add Poetry and project virtual environment to PATH
ENV PATH="$POETRY_HOME/bin:$PROJECT_DIR/.venv/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry (set version as needed)
ENV POETRY_VERSION=2.1.1
RUN curl -sSL https://install.python-poetry.org | python3 - && chmod a+x /opt/poetry/bin/poetry

# Set working directory
WORKDIR $PROJECT_DIR

# Copy all files from the repository into /app
# (Make sure your .dockerignore doesn't exclude the "api" folder)
COPY . .

# Install only the main dependencies using Poetry
RUN poetry install --only main

# Expose the port used by FastAPI
EXPOSE 8000

# Run the FastAPI app using gunicorn with uvicorn workers
CMD ["poetry", "run", "gunicorn", "api.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
