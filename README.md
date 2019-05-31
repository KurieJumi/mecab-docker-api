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

To [ssh into docker container](http://phase2.github.io/devtools/common-tasks/ssh-into-a-container/)
```
docker exec -it <container id> /bin/bash
```

To clean up cache after running docker containers
```
docker system prune -a
```

## Jupyter Basics

To open jupyter after you docker-compose up and everything is running look for the token and copy and paste http://localhost:8888/?token=<TOKEN YOU SEE ON SERVER SIMILAR TO CODE BELOW> to your browser
```
To access the notebook, open this file in a browser:
jupyter_1  |         file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
jupyter_1  |     Or copy and paste one of these URLs:
jupyter_1  |         http://(b27090dc995f or 127.0.0.1):8888/?token=c1a351b12a03a8ee0ddc7a87ae3a4d7dadeb1648d78b5b88
```

