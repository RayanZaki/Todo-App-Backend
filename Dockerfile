# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if needed for your project)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile /app/

# Install the dependencies specified in the Pipfile
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of your application code into the container
COPY . /app/

# Set the environment variable to indicate the app is running inside a Docker container
ENV PYTHONUNBUFFERED 1

# Expose the port that your application will run on (e.g., 8000)
EXPOSE 8000

# Set the command to run your application (e.g., Flask, Django, etc.)
# For a Flask app:
# CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
# Or for Django:
CMD ["pipenv", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
