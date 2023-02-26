# Learn DevOps
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FUnpredictablePrashant%2FLearnDevOps&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

This repository consist of documentation to learn DevOps.


# Traditional Deployment
We will try to deploy a nodejs application using the traditional method. You will understand the complexity involved in deploying the application.
Visit NoDockerNode to read for documentation on deploying Nodejs application without Docker.


# Docker Deployment

## Dockerizing a flask based application

### Creating a flask based application

Let's first write a simple flask based application which will print `Hello World`. We will start by creating a `app.py` file and put the following code inside it.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
```

In order to create flask based application, we need to install flask library as well. We can put them inside a `requirements.txt` file which is the ideal way to store the list of all the libraries which you will need for the functioning of the application.<br>
Create `requirements.txt` and put the following lines
```
flask
```

Now that we have all components to run a flask application. We can simply go ahead and run this by first installing flask and running this by following command
```bash
pip3 install -r requirements.txt
python3 app.py
```

You will notice that flask application is running on port `5000` and you can access it with by visiting `http://127.0.0.1:5000`.

### Dockerizing the application

First, stop the current server of flask, making sure port `5000` is free. Create a `Dockerfile` with the following content in the same folder where `app.py` is

```docker
FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]
```

Build this image by running the command
```bash
docker build -t flask-hello .
```

Run this built image from the following command which will create a container.
```
docker run -p 5000:5000 -d flask-hello
```

The application is running on port `5000` and can be accessed with `127.0.0.1:5000`. However, if you want it to run on port 3000 on your machine then just change the pointing port and your command to run will be `docker run -p 3000:5000 -d flask-hello`.

### Running the flask based application with gunicorn

Add `gunicorn` in your `requirements.txt` file. <br>
Create a bash file called as `build.sh` and put the command to run the server through gunicorn.

```bash
#!/bin/sh
gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:80
```
Change the Dockerfile to have the entry point from this `build.sh` file. The `Dockerfile` would look like:

```
FROM python
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT [ "./build.sh" ]
```

Finally build and run the application with the command specified above.
