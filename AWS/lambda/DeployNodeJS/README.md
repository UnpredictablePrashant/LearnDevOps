# Hosting Nodejs in AWS Lambda

```sh
npm install express serverless-http
```

### Create a `index.js`

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send({message: "Hello from Express!"});
});

module.exports = app;
```

### Create `handler.js`

```js
const serverless = require('serverless-http');
const app = require('./index');

module.exports.run = serverless(app);
```

### Create `serverless.yml`

```yml
service: nodejsworkshop

provider:
  name: aws
  runtime: nodejs18.x
  stage: dev
  region: ap-south-1

functions:
  app:
    handler: handler.run
    events:
      - http: ANY /
      - http: 'ANY /{proxy+}'

plugins:
  - serverless-offline
```

### Deploying the application

```sh
npm install --save-dev serverless-offline
Set-Alias -Name sls -Value serverless
sls deploy
```
