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


# Docker Swarm

Docker Swarm is a native clustering and orchestration tool for Docker containers. It allows you to create and manage a cluster of Docker nodes, which can be either physical or virtual machines.

## Key Concepts:

<ul>
<li> <strong>Nodes:</strong> These are the individual machines that make up the Docker Swarm cluster. Each node runs the Docker engine and can run one or more containers.</li>

<li><strong>Services:</strong> These are the applications that run on the Docker Swarm cluster. A service is made up of one or more tasks, which are instances of a container running on a node.</li>

<li><strong>Tasks:</strong> These are the individual instances of a container that run as part of a service. A service can have multiple tasks, each running on a different node in the cluster.</li>

<li><strong>Managers:</strong> These are nodes that are responsible for managing the cluster state and orchestrating the deployment of services and tasks.</li>

<li><strong>Workers:</strong> These are nodes that run the tasks that make up the services.</li>
</ul>

## Setting up a Docker Swarm Cluster

To set up a Docker Swarm cluster, you first need to initialize it on one of the nodes using the `docker swarm init` command. This node becomes the first manager node in the cluster. You can then join additional nodes to the cluster using the `docker swarm join` command.

## Deploying Services

Once the cluster is set up, you can deploy services to it using the `docker service create` command. You can specify the number of replicas of the service that you want to run, as well as other parameters such as the image to use and any environment variables.

## Monitoring and Scaling Services

You can monitor the state of the cluster and the services running on it using the `docker node`, `docker service`, and `docker stack` commands. You can also scale up or down the number of replicas of a service using the docker service scale command.

Overall, Docker Swarm provides a powerful and flexible way to manage and orchestrate containerized applications at scale.

## Docker Swarm Tutorial with Flask

First we need to create and dockerize a flask based application. Let's say we build our flask based application using the command
```
docker build -t myflaskapp .
```


### Creating Docker Swarm Cluster

Create a Docker Swarm cluster by following these steps:

1. Initialize the Docker Swarm cluster on your local machine by running the following command:

```
docker swarm init
```
This initializes a single-node Swarm cluster on your local machine.

2. Create a new overlay network by running the following command:

```
docker network create --driver overlay mynetwork
```

This creates a new overlay network called mynetwork, which allows containers in the Swarm to communicate with each other.

### Deploy the Flask Application as a Service

Deploy the Flask application as a Docker service in the Swarm by following these steps:

1. Deploy the service by running the following command:
```bash
docker service create --name myflaskapp --replicas 3 --network mynetwork -p 5000:5000 myflaskapp
```
This creates a Docker service called myflaskapp with 3 replicas, running on the mynetwork overlay network and listening on port 5000. The service is created from the myflaskapp Docker image we built earlier.

2. Verify that the service is running by running the following command:
```
docker service ls
```
This lists all the Docker services running in the Swarm. You should see a service called myflaskapp with 3 replicas.

3. Access the Flask application by going to `http://localhost:5000` in your web browser. You should see the "Hello World!" message.

# Load Testing and Scaling

The idea is to increase load to test the clusters/pods.

## Linux
To increase the load on the Flask application and trigger the creation of new nodes to manage the traffic, you can use a simple script that sends HTTP requests to the application.

1. Install the httpie tool by running the following command:
```
sudo apt install httpie
```
2. Use the watch command to continuously send requests to the Flask application, like this:
```
watch -n 0.1 http GET http://localhost:5000
```
This sends a GET request to the Flask application every 0.1 seconds. You should see the output of the watch command updating continuously with the response from the Flask application.

3. Scale up the number of replicas of the myflaskapp service by running the following command:

```
docker service scale myflaskapp=6
```
This increases the number of replicas of the myflaskapp service to 6. You should see new nodes being created and added to the Swarm.

4. Verify that the new nodes are running by running the following command:
```
docker service ps myflaskapp
```

This lists all the tasks (i.e. container instances) of the myflaskapp service running in the Swarm. You should see 6 tasks running.

5. Verify that the Flask application is still accessible by going to `http://localhost:5000` in your web browser. You should still see the "Hello World!" message.

## Windows

We will be using `Apache Benchmarking` for testing load on our website. For that we need to install Apache HTTP Server and add them in environment variable.

1. Download the Apache HTTP Server for Windows from the following link: https://www.apachelounge.com/download/`
2. Choose the version of Apache that matches your version of Windows (32-bit or 64-bit).
3. Extract the downloaded ZIP file to a directory of your choice.
4. Add the bin directory of the extracted Apache HTTP Server to your system's PATH environment variable. You can do this by following these steps:
<ul>
<li>Open the Start menu and search for "Environment Variables".</li>
<li>Click on "Edit the system environment variables".</li>
<li>Click on the "Environment Variables" button.</li>
<li>Under "System Variables", find the "Path" variable and click "Edit".</li>
<li>Click "New" and add the path to the bin directory of the extracted Apache HTTP Server (e.g. C:\apache\bin).</li>
<li>Click "OK" to close all the windows.</li>
</ul>
Once you have installed ab, you can use the same command as before to perform load testing:

```
ab -n 100000 -c 100 http://localhost:5000/
```
This command will send 100,000 requests with a concurrency of 100 to the Flask application running on `http://localhost:5000/`.

`ab` stands for Apache Bench, which is a command-line tool provided by the Apache HTTP Server for benchmarking HTTP servers. It is commonly used to perform load testing on web applications, including Flask-based applications.

The `ab` command allows you to send a specified number of requests with a specified level of concurrency to a web server and measure the performance of the server under load. It generates a report that shows various statistics, such as the number of requests per second, the average response time, and the standard deviation of the response time.

## Auto Scaling in Docker Swarm

We can set up a service with a defined maximum and minimum number of replicas. When the average CPU usage or memory usage of the service exceeds a certain threshold, Docker Swarm can automatically increase the number of replicas to handle the increased load.

Here is a basic example of how to set up auto-scaling for a service in Docker Swarm:

1. Set up a Docker Swarm cluster with at least one manager and one worker node.

2. Deploy the service with the desired number of replicas and the resource limits (such as CPU and memory limits) using the docker service create command. For example:

```
docker service create --replicas 3 --name myflaskservice --limit-cpu 0.5 --limit-memory 512m myflaskapp:latest
```
This command creates a service named my-service with three replicas, with CPU usage limited to 50% and memory usage limited to 512 MB per replica.

3. Configure the auto-scaling options for the service using the docker service update command. For example:

```
docker service update --replicas-max 10 --replicas-min 3 --update-delay 10s --update-parallelism 2 myflaskservice
```

This command sets the maximum number of replicas to 10, the minimum number of replicas to 3, and the update delay to 10 seconds. The --update-parallelism option specifies the number of replicas that are updated at a time during scaling operations.

4. Set up the auto-scaling policy for the service using the docker service update command. For example:

```
docker service update --force --image myflaskapp:latest --args "--autoscale-cpu 80,60 --autoscale-memory 80,60" myflaskservice
```

This command sets the auto-scaling policy for the service. In this example, the service scales up if the average CPU or memory usage exceeds 80% for at least one minute, and scales down if the average usage falls below 60% for at least one minute.

5. Monitor the service and observe the auto-scaling behavior using the docker service ps and docker service inspect commands.
```
docker service ps myflaskservice
docker service inspect myflaskservice
```

These commands show the current state and configuration of the service and its replicas.

With these steps, Docker Swarm can automatically scale up or down the number of replicas of the service based on the CPU and memory usage of the containers. This can help optimize the performance of the service without requiring manual intervention.