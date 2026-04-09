import http from 'http';

function cdpGet(path) {
  return new Promise((resolve, reject) => {
    http.get('http://localhost:3456' + path, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try { resolve(JSON.parse(d)); }
        catch { resolve(d); }
      });
    }).on('error', reject);
  });
}

const result = await cdpGet('/health');
console.log(JSON.stringify(result));
