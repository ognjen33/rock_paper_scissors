#!/bin/bash
set -e

# Run migrations
alembic upgrade head

# Start FastAPI server
exec uvicorn main:app --host 0.0.0.0 --port 8000

