FROM ubergarm/sanic-alpine

RUN pip3 install AoikLiveReload

RUN mkdir /app
# COPY ./src /app/src
COPY ./lilpebbles.py /app/lilpebbles.py
COPY ./workbox-sw.prod.v1.0.1.js /app/workbox-sw.prod.v1.0.1.js
WORKDIR /app

ENTRYPOINT ["/usr/bin/python3"]

CMD ["lilpebbles.py"]
