# use an official python image as the base image
FROM python:3.11-slim-buster

# set working directory
WORKDIR /stockapp

# copy contents of current dir into container
COPY . /stockapp

# upgrade pip
RUN pip install --upgrade pip

# install any needed packages
RUN pip install --no-cache-dir -r requirements.txt

# set the default commands to run when starting the container
CMD ["python", "main.py"]