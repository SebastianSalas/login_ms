# Image for Python
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Select working directory
WORKDIR /app

# Update
RUN apt-get update

# Copy requirements.txt to working directory
COPY requirements.txt .

# Install requirements
RUN pip install -r requirements.txt

# Copy all files to working directory
COPY . .

# Expose the container port
EXPOSE 8000

# Execute the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]