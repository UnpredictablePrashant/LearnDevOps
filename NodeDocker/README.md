# Docker login
```
docker login
```

# Building the docker

```
docker build . -t prashantdey/node-hello-world
```

# Look for the build image

```
docker images
```


# Run the image

```
docker run -p 3000:3000 -d prashantdey/node-hello-world
```

# Get container ID

```
docker ps
```

# Print app output

```
docker logs <container id>
```

# Action
Running on http://localhost:3000