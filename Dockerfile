# Use an official Python runtime as a parent image
#FROM python:latest  
FROM python:3.6.9 

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
#RUN apt-get update -y 
#RUN  apt-get install python3-pip -y 

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt
#RUN pip3 install --upgrade mysql-connector-python


RUN apt-get update -y && apt-get install sshpass -y

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Define environment variable
#ENV NAME World

# Run the Flask app when the container launches
CMD ["python3", "index.py"]

