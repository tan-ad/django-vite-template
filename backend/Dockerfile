FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies if any (e.g., for Pillow or postgres client)
# RUN apt-get update && apt-get install -y --no-install-recommends some-package

# Install Python dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Default command (can be overridden in docker-compose)
# Use 0.0.0.0 to allow connections from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
