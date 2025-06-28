# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install websockets
RUN pip install python-dotenv 
RUN pip install mysql-connector-python


ENV IP=${IP}
ENV PORT=${PORT}
ENV HOST=${HOST}
ENV DB=${DB}
ENV USER=${USER}
ENV PASSWORD=${PASSWORD}

EXPOSE 4000

CMD [ "python", "./Server.py" ]