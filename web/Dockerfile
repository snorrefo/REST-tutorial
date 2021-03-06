# Use an official Python runtime as a parent image
FROM python:3.6


COPY  ./requirements.txt /code/

# Set the working directory to /code
WORKDIR /code/

# Install tools required to build the project
# We need to run `docker build --no-cache .` to update those dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn==19.8.1

# Copy the current directory contents into the container at /code
COPY  ./ /code/

# Remove __pycache__ folders
RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Make port 5000 available to the world outside this container
EXPOSE 5000


# Run app.py when the container launches
CMD ["python", "wsgi.py"]
