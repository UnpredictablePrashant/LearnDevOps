const serverless = require('serverless-http');
const app = require('./index');

module.exports.run = serverless(app);
