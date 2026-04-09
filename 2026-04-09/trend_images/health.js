const http = require('http');
http.get('http://127.0.0.1:3456/health', r => {
  let d = '';
  r.on('data', c => d += c);
  r.on('end', () => console.log(d));
});
