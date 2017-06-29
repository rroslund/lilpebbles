FROM node:alpine

RUN apk add --no-cache --virtual .build-deps \
                  ca-certificates \
                  wget \
                  tar \
                  python3 \
                  python3-dev \
                  build-base \
                  git && \
                  python3 -m ensurepip && \
                  rm -r /usr/lib/python*/ensurepip && \
                  pip3 install --upgrade pip setuptools && \
                  pip3 install git+git://github.com/channelcat/sanic.git@master && \
                  cd /usr/local/bin && \
                  wget https://yarnpkg.com/latest.tar.gz && \
                  tar zvxf latest.tar.gz && \
                  ln -s /usr/local/bin/dist/bin/yarn.js /usr/local/bin/yarn.js && \
                  apk del python3-dev .build-deps build-base &&\
                  rm -r /root/.cache

RUN npm install webpack -g
RUN apk add --no-cache python3
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt && npm install
RUN npm run build
