# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the boto3 module
RUN pip install boto3
RUN pip install mysql-connector-python

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "app.py"]
