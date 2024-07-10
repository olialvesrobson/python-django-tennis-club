# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenSSL for SSL support
RUN apt-get update && apt-get install -y openssl

# Copy the project
COPY . /app/

# Generate self-signed certificates (or you can copy existing ones if you have them)
RUN openssl req -x509 -newkey rsa:4096 -keyout /app/key.pem -out /app/cert.pem -days 365 -nodes -subj "/CN=localhost"

# Add a command to run the Django development server with SSL
CMD ["python", "manage.py", "runsslserver", "0.0.0.0:8000", "--certificate", "/app/cert.pem", "--key", "/app/key.pem"]
