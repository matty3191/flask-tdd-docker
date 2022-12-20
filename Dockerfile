#pull official base image
FROM python:3.10.9-slim-buster

#set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#set environment variables. 
#1st varaible prevents python writing pyc files to disc (equivalent to python -b)
#2nd variable prevents python from buffering stdout and stderr (equivalent to python -u)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

#add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#add app
COPY . . 

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

#run server
CMD python manage.py run -h 0.0.0.0