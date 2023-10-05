# Use an official Python runtime as the base image
FROM python:3.7.3-stretch

# Make working directories
RUN mkdir -p /calculator
WORKDIR /calculator

# Upgrade pip with no cache
RUN pip install --no-cache-dir -U pip

# Copy every file in the source folder to the created working directory
COPY . .

# Install Flask
RUN pip install Flask

# Expose a port for the Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]
