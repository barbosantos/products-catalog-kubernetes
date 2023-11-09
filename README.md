# products-catalog
In this project, we will extract product information from different shop websites. The object is to create a price calculator for saving money spent on grocery shopping.

# Kubernetes resources

For saving our products in a database, we have chosen mongodb. MongoDB will be installed using kubernetes helm chart.
The chart we are using is from the community operator (https://artifacthub.io/packages/helm/mongodb-helm-charts/community-operator)

To install it, we can run the following commands:
```bash
# make sure docker is running and start minikube
$ minikube start
# add chart repo
$ helm repo add mongodb https://mongodb.github.io/helm-charts
$ helm install mdb-community-operator mongodb/community-operator --namespace storage
# apply the replica set
$ kubectl apply -f k8s/mongodb.yml [--namespace namespace-name] 


```

# Mongodb Connection

Locally access:
Port forwarded the service created (e.g. using OpenLens or kubectl commands). Then connect using the following connection string (replace the values with the actual ones):

mongodb://username:password@localhost:forwadedport/admin?ssl=false&directConnection=true
