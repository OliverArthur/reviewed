FROM python:3.4.5-onbuild

ENV IP='0.0.0.0'

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y curl expect sqlite3 dropbear sudo

RUN mkdir -p python/src/dred-backend

WORKDIR /python/src/dred-backend

COPY requirements.txt /python/src/dred-backend/requirements.txt

ADD ./requirements.txt /python/src/dred-backend/requirements.txt

COPY . /python/src/dred-backend

# Copy entrypoint script to the container
COPY docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/docker-entrypoint.sh"]
