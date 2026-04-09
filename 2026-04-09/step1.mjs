// Step 1: Just open a Google Images tab and print target ID
import http from 'node:http';
const q = process.argv[2] || 'Star Wars Maul Shadow Lord';
const url = `https://www.google.com/search?q=${encodeURIComponent(q)}&tbm=isch&tbs=isz:l`;
http.get(`http://localhost:3456/new?url=${encodeURIComponent(url)}`, res => {
  let d = ''; res.on('data', c => d += c);
  res.on('end', () => console.log(d));
}).on('error', e => console.error(e.message));
