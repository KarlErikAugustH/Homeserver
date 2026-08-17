FROM python:3.12-slim

WORKDIR /app

COPY backend/ ./backend/
COPY frontend/ ./frontend/

RUN pip install fastapi uvicorn jinja2

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "9000"]