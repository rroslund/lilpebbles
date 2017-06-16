FROM ubergarm/sanic-alpine

RUN mkdir /app
COPY ./src /app/src
COPY ./lilpebbles.py /app/lilpebbles.py
COPY ./sw.js /app/sw.js
COPY ./workbox-sw.prod.v1.0.1.js /app/workbox-sw.prod.v1.0.1.js
WORKDIR /app

ENTRYPOINT ["/usr/bin/python3"]

CMD ["lilpebbles.py"]
