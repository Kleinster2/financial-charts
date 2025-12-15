const http = require('http');
const fs = require('fs');
const path = require('path');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml; charset=utf-8',
};

function safeJoin(rootDir, requestedPath) {
  const normalized = requestedPath.replaceAll('\\', '/');
  const noQuery = normalized.split('?')[0];
  const noHash = noQuery.split('#')[0];
  const stripped = noHash.replace(/^\/+/, '');
  const resolved = path.resolve(rootDir, stripped);
  const resolvedRoot = path.resolve(rootDir);
  if (!resolved.startsWith(resolvedRoot + path.sep) && resolved !== resolvedRoot) {
    return null;
  }
  return resolved;
}

async function startStaticServer(rootDir) {
  const server = http.createServer((req, res) => {
    const urlPath = req.url || '/';

    if (urlPath === '/favicon.ico') {
      res.writeHead(204);
      res.end();
      return;
    }

    const effectivePath = urlPath === '/' ? '/index.html' : urlPath;
    const filePath = safeJoin(rootDir, effectivePath);
    if (!filePath) {
      res.writeHead(400);
      res.end('Bad request');
      return;
    }

    fs.stat(filePath, (err, stat) => {
      if (err || !stat.isFile()) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }

      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      fs.readFile(filePath, (readErr, data) => {
        if (readErr) {
          res.writeHead(500);
          res.end('Server error');
          return;
        }
        res.writeHead(200, {
          'Content-Type': contentType,
          'Cache-Control': 'no-store',
        });
        res.end(data);
      });
    });
  });

  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  const address = server.address();
  if (!address || typeof address === 'string') {
    throw new Error('Failed to determine server address');
  }

  return {
    server,
    baseURL: `http://127.0.0.1:${address.port}`,
  };
}

module.exports = { startStaticServer };
