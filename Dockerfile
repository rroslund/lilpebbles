FROM ubergarm/sanic-alpine

COPY ./src /src
COPY ./lilpebbles.py /lilpebbles.py
COPY ./sw.js /sw.js
COPY ./workbox-sw.prod.v1.0.1.js /workbox-sw.prod.v1.0.1.js

ENTRYPOINT ["/usr/bin/python3"]

CMD ["lilpebbles.py"]
