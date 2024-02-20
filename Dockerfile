# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# No need to install dependencies from requirements.txt for this script

# No need to expose ports since we're not starting a server

# Run app.py when the container launches
CMD ["python", "./main.py"]
