# IMP For uwsgi - nginx config see: https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
# For running jupyter see : https://jupyter-notebook.readthedocs.io/en/stable/public_server.html

FROM ubuntu:16.04

WORKDIR /opt

# Basic installation
RUN apt-get update \
  && apt-get install -y sudo \
  && apt-get install -y python3 \
  && apt-get install -y python3-pip \
  && apt-get install -y curl \
  && apt-get install -y git \
  && apt-get install -y make \
  && apt-get install -y cron \
  && apt-get install -y wget \
  && apt-get install -y xz-utils \
  && apt-get install -y file \
  && apt-get install -y mecab \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y swig \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

# Install NEologd Dictionary
WORKDIR /var/lib/mecab/dic
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /var/lib/mecab/dic/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y

COPY . /opt/api
WORKDIR /opt/api

# TODO fix issue with nltk install error
RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]
