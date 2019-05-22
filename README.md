# mecab-docker-api

Docker container with MeCab provided as api with flask.
(Plan to expand to do preprocessing Japanese text)

## Before you start

Install [docker desktop](https://www.docker.com/products/docker-desktop) and follow the installation guides provided. (You have to create docker hub account. Docker id is like a "user name" and you must also provide an email address to create the account.)

Install [postman](https://www.getpostman.com/). This is not mandatory, but it makes testing api very easy. Please read their [documentation](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/) or maybe check out their [training](https://training.getpostman.com/catalog) for more information.


## Docker Usage Basics

To start a container (option -d for starting the container in the background)
```
docker-compose up
docker-compose up -d
```

To stop container
```
docker-compose down
```

To check the list of running containers
```
docker ps
```

To kill (stop forcefully) container. Specify which service to kill.
```
docker kill [service]
```

... to be updated soon


