# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 8815 available to the world outside this container
EXPOSE 8815

# Run app.py when the container launches
CMD ["python", "./chisquared.py"]
