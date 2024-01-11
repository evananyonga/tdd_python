# base image
FROM python:3.8
# setup environment variable
ENV DockerHOME=/var/www
# ENV CHROMEDRIVER_VERSION 114

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy whole project to your docker home directory.
COPY . $DockerHOME

# install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# port where the Django app runs
EXPOSE 8000

# specify server directory
ENTRYPOINT ["python", "superlists/manage.py"]

# start server
CMD ["runserver", "0.0.0.0:8000"]