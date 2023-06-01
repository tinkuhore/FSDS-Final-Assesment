# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install build-essential and gcc
RUN apt-get update && apt-get install -y build-essential gcc

# Create and activate a virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose a port (if needed) - replace <port_number> with the actual port number
EXPOSE 5000

# Set the command to run the application
CMD [ "python", "app.py" ]
