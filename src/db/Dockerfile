# pull official base image
FROM postgres:14-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

## Here, we extended the official Postgres image (an Alpine-based image) 
## by adding create.sql to the "docker-entrypoint-initdb.d" directory in the container. 
## This file will execute on init.