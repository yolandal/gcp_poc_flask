# GCP POC Model Engine
This folder contains a Flask web app using Gunicorn HTTP Server.
A Flask app cluster has been created for the deployment: *Kubernetes Engine > Clusters > flask-app-cluster* 

#### Build the docker image on GCP
Image can be found in *Container Registry > Images*
>gcloud builds --project gcp-poc-bell-bi submit --tag gcr.io/gcp-poc-bell-bi/flask-app:v1.2

#### Deploy to GKE  
>kubectl apply -f app.yaml

May need to get authentication credentials for the cluster first
>gcloud container clusters get-credentials flask-app-cluster --zone=us-central1-b

Get deployed URL
>kubectl get services -l name=flask-app-test

##### Versions: 
- 1.0: Initial deployment with a simple welcome message 
- 1.1: Added a static LOB number <-> name look-up with POST and GET request methods, with endpoints /lob and /num
- 1.2: Takes a JSON payload and returns a JSON payload with message, timestamp and static sentiment values, via a POST request

##### Initial Set Up
Explosed as external load balancer
>kubectl expose deployment flask-app-test --type=LoadBalancer --port 80 --target-port 8080