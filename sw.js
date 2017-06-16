importScripts('workbox-sw.prod.v1.0.1.js');

/**
 * DO NOT EDIT THE FILE MANIFEST ENTRY
 *
 * The method precache() does the following:
 * 1. Cache URLs in the manifest to a local cache.
 * 2. When a network request is made for any of these URLs the response
 *    will ALWAYS comes from the cache, NEVER the network.
 * 3. When the service worker changes ONLY assets with a revision change are
 *    updated, old cache entries are left as is.
 *
 * By changing the file manifest manually, your users may end up not receiving
 * new versions of files because the revision hasn't changed.
 *
 * Please use workbox-build or some other tool / approach to generate the file
 * manifest which accounts for changes to local files and update the revision
 * accordingly.
 */
const fileManifest = [
  {
    "url": "/css/main.css",
    "revision": "f4eae9ed7c7725098b14017e609f4de4"
  },
  {
    "url": "/index.html",
    "revision": "d1e175801e45a5ba11a3e0ff56c4b855"
  },
  {
    "url": "/js/app.js",
    "revision": "749d3bcfaad86a7f9b2e9d0407c6798e"
  },
  {
    "url": "/workbox-sw.prod.v1.0.1.js",
    "revision": "3fbc93cd82283d7c3a2cb4dcaf36be91"
  }
];

const workboxSW = new self.WorkboxSW();
workboxSW.precache(fileManifest);
