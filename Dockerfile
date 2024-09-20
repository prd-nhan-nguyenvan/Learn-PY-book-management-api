# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster

# Create a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install requirements
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY . .
