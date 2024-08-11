
# Kubernetes

## Architecture


## Setting up Kubernetes

## Configuration Files

1. Pod Configuration File:  Defines a pod, the smallest deployable unit in Kubernetes.
2. Deployment Configuration File: Manages the deployment and scaling of a set of pods.
3. Service Configuration File: Exposes a set of pods as a network service.
4. ConfigMap Configuration File: Provides configuration data in the form of key-value pairs.
5. Secret Configuration File: Stores sensitive information such as passwords, OAuth tokens, and SSH keys.
6. PersistentVolume (PV) Configuration File: Defines a storage resource in the cluster.
7. PersistentVolumeClaim (PVC) Configuration File: Requests storage resources defined by a PersistentVolume.
8. Ingress Configuration File: Manages external access to the services in a cluster, typically HTTP and HTTPS.
9. Namespace Configuration File: Creates a new namespace for isolating resources.
10. Role and RoleBinding Configuration Files: Defines access control policies within a namespace.
11. StatefulSet Configuration File: Manages stateful applications, providing guarantees about the ordering and uniqueness of pods.
12. DaemonSet Configuration File: Ensures that a copy of a pod runs on all or some of the nodes in the cluster.


## Types of Service

1. ClusterIP: <br>
Purpose: Exposes the service on an internal IP address within the cluster. This is the default type and is used for communication between services within the same Kubernetes cluster. <br>
Use Case: Internal communication between pods within the same cluster.

```yml
apiVersion: v1
kind: Service
metadata:
  name: my-clusterip-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

2. NodePort: <br>
Purpose: Exposes the service on each node's IP address at a static port (the NodePort). A ClusterIP service, to which the NodePort service routes, is automatically created.<br>
Use Case: External access to the service using the IP address of any node in the cluster.

```yml
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
      nodePort: 30007
  type: NodePort
```

3. LoadBalancer: <br>
Purpose: Exposes the service externally using a cloud provider's load balancer. This service automatically creates a NodePort and ClusterIP service and routes external traffic to the appropriate pods.<br>
Use Case: Exposing the service to the internet with a cloud provider-managed load balancer.

```yml
apiVersion: v1
kind: Service
metadata:
  name: my-loadbalancer-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: LoadBalancer
```

4. ExternalName: <br>
Purpose: Maps a service to the contents of the externalName field (e.g., a DNS name) by returning a CNAME record with the value specified in externalName. This service does not define any ports or selectors.<br>
Use Case: Alias a service running externally to a Kubernetes cluster using a DNS name.

```yml
apiVersion: v1
kind: Service
metadata:
  name: my-externalname-service
spec:
  type: ExternalName
  externalName: example.com
```

5. Headless Service: <br>
Purpose: Provides direct access to the individual pods without using a load balancer. No ClusterIP is assigned, and DNS records are created for each pod.<br>
Use Case: Stateful applications that require direct access to individual pods, such as databases.
```yml
apiVersion: v1
kind: Service
metadata:
  name: my-headless-service
spec:
  clusterIP: None
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

# Projects

## Simple Flask Project: Starting with K8s

1. Build the image 
2. Start the minikube cluster
```bash
minikube start
```
3. Deploy the k8s file into the cluster
```bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
```
4. Access it through the minikube ip.
```bash
minikube service flaskapp-service
```

And run the service specified in the port.

## Path Based Routing for Microservices in K8s
1. Build all the microservices from the project and push it into the dockerhub / ecr.<br>
`https://github.com/UnpredictablePrashant/MicroserviceNodeJs`<br>
Alternatively, you can fetch it from `https://hub.docker.com/r/prashantdey/microservicenode/tags`

2. Write the `deployment.yml` file for each microservices and similarly do it for the `service.yml`. Finally, write the `ingress.yml` to create path based routing. Code is already provided.

3. Start minikube and configure the minikube to enable the ingress.
```bash
minikube start
minikube addons enable ingress
minikube addons enable ingress-dns
```

4. My port 80 is already being used by other services, so I configured my ingress to use 3005 to use for the HTTP traffic.
```bash
kubectl edit svc nginx-ingress-ingress-nginx-controller -n kube-system
```

Change the port to 3005, then save the file and close the file:
```yml
spec:
  ports:
  - name: http
    port: 3005
    targetPort: 80
  - name: https
    port: 443
    targetPort: 443
```

5. Apply all the k8s file.

```bash
kubectl apply -f deployment-ms1.yml
kubectl apply -f deployment-ms2.yml
kubectl apply -f deployment-ms3.yml
kubectl apply -f service-ms1.yml
kubectl apply -f service-ms2.yml
kubectl apply -f service-ms3.yml
kubectl apply -f ingress.yml
```

6. Inorder to access content from minikube cluster over localhost, we need to create tunnel.
```bash
minikube tunnel
```

You can access the website by running it at `http://localhost:3005/ms1`