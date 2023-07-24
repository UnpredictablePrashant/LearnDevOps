const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send({message: "Hello from Express!"});
});

module.exports = app;
