#!/bin/bash

# Use an official Python runtime as a parent image
FROM python:3.7.2

# Set the working directory to /app
WORKDIR /app

# Add pip requirements
ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 1111 available to the world outside this container
EXPOSE 1111

# Run startup script
# enter env_vars on the CMD line
CMD ["python3", "run.py"]

# CMD /app/docker_entrypoint.sh
