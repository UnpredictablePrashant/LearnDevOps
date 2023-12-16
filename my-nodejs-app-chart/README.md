# Executing HELM Chart

Create Cluster
```sh
eksctl create cluster --name node-micro-demo --region us-east-1 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --nodes-min 2 --nodes-max 2
```

Configure with eks:
```sh
aws eks --region us-east-1 update-kubeconfig --name node-micro-demo
```

Install Helm:
```sh
helm install my-nodejs-app-release -f values.yaml .
```

Checkout for the services:
```sh
kubectl get services --watch
```

Listing and uninstalling helm:
```sh
helm list
helm uninstall <chart-name>
```