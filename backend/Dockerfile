# Use the official Python image as base
FROM python:latest

# Set working directory in the container
WORKDIR /app

# Copy and install requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

