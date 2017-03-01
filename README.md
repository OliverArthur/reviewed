# reviewed

### Tool you must have installed
* Docker for Mac (https://docs.docker.com/docker-for-mac/)
* Docker for Windows (https://docs.docker.com/docker-for-windows/)
* Docker for Linux (https://docs.docker.com/engine/installation/linux/ubuntu/)


### The application was created with the following technologies: 
* Python (v3.x) for provider the backend
* Angular (v1.6) for provider the front and bussines logic, build using ES6 Classes
* Gulp for the pipeline
* Material design lite for provider the front and UI
* Docker for provider the DEV env and also can using for Prod env

1. Clone the repo:

```
git clone git@github.com:OliverArthur/reviewed.git
```
#### backend-End container
* To build the `dred-backend` container, do:
```
docker-compose build dred-backend
```

* To start the container, do:

```
docker-compose up dred-backend
```
   This will start the docker container for the `dred-backend` application.
   
   Front-end is exposed to port `5000`.
   
   url for the api: `http://0.0.0.0:5000`.


#### Front-End container
* To build the `dred-ui` container, do:
```
docker-compose build dred-ui
```

* To start the container, do:

```
docker-compose up dred-ui
```
   This will start the docker container for the `dred-ui` application.
   
   Front-end is exposed to port `3000`.
   
   You can browse the UI by navigating to `http://0.0.0.0:3000` on your favorite browser (i.e Chrome).

#### Docker command line:
* docker ps (log the container is running, With this you can see the id of the target container.)
* docker exec -it mycontainerid bash (loggin into the container replaces mycontainerid for the id of the target container.)

#### Project Info (For Dev)
* Project setup in Docker container
* Tools: gulp, and npm
* npm command line: npm run server
