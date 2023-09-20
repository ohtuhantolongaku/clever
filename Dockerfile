# Use an official Python and Node.js runtime as the base image
FROM python:3.9-slim

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Install clever-tools globally during the build step
RUN npm install -g clever-tools

# Copy your Python application files into the container
COPY . /app

# Expose the port your Flask app will run on (adjust as needed)
EXPOSE 8080

# Install any Python dependencies (if needed)
# RUN pip install -r requirements.txt

# Define the command to start your Flask app
CMD ["python", "app.py"]
