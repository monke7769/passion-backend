# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8686 available to the world outside this container
EXPOSE 8686

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]