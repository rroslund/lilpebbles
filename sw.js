const CACHE_NAME = 'lilpebbles-gallery-v01';
const expectedCaches = [CACHE_NAME];
const staticFiles = [
  './',
  './css/main.css',
  './dist/bundle.js',
];

/**
 * Performs install steps.
 */
self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(staticFiles))
  );
});

/**
 * Handles requests: responds with cache or else network.
 */
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});

/**
 * Cleans up static cache and activates the Service Worker.
 */
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.map((key) => {
        if (!expectedCaches.includes(key)) {
          return caches.delete(key);
        }
      })
    )).then(() => {
      console.log(`${CACHE_NAME} now ready to handle fetches!`);
      return clients.claim();
    }).then(() => {
      return self.clients.matchAll().then(clients =>
        Promise.all(clients.map(client =>
          client.postMessage('The service worker has activated and taken control. This application can now be used offline.')
        ))
      );
    })
  );
});

/**
 * Listens to messages from the client.
 */
self.addEventListener('message', (event) => {
  caches.open('custom').then((cache) => {
    switch (event.data.command) {
      /**
       * Requests asset and add it to the custom cache.
       */
      case 'addimg':{
        var formData = new FormData();
        formData.append('img', event.data.file);
        return fetch('/images', {
          method:'POST',
          body: formData
        })
        .then(response => response.json())
        .then(response => {
          return fetch(new Request(response.small, { mode: 'no-cors' }))
           .then(res => cache.put(response.small, res))
          .then(() => {
              event.ports[0].postMessage({
                error: null,
                data: response,
                count: cache.keys().length,
              });
            })
        });
      /**
       * Requests asset and add it to the custom cache.
       */
      }
      case 'add':
        return fetch(new Request(event.data.url, { mode: 'no-cors' }))
          .then(response => cache.put(event.data.url, response))
          .then(() => {
            event.ports[0].postMessage({
              error: null,
              data: event.data,
              count: cache.keys().length,
            });
          });

      /**
       * Removes an existing asset from the custom cache.
       */
      case 'delete':{
        return cache.delete(event.data.url).then((success) => {
          console.warn(success ? null : 'Item was not found in the cache.');
          event.ports[0].postMessage({
            count: cache.keys().length,
          });
        });
      }
      /**
       * Called event is unknown.
       */
      default:
        throw Error(`Unknown command: ${event.data.command}`);
    }
  });
});