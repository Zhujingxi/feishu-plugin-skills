const { readFileSync } = require('node:fs');
const { join } = require('node:path');

module.exports = function handler(req, res) {
  const installer = readFileSync(join(process.cwd(), 'install.sh'), 'utf8');
  res.setHeader('Content-Type', 'text/x-shellscript; charset=utf-8');
  res.setHeader('Cache-Control', 'public, max-age=300');
  res.status(200).send(installer);
};
