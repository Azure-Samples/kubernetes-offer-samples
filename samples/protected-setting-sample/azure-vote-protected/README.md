# azure-vote

The Azure Vote application is a simple sample used throughout the Azure Container Service (AKS) documentation. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage.

## Installing the Chart

Add the Azure Samples chart repository.

```
helm repo add azure-samples https://azure-samples.github.io/helm-charts/
```

Install the chart.

```
helm install azure-samples/azure-vote-protected
```


## Configuration

The following tables lists the configurable parameters of the azure-vote chart and the default values.

| Parameter | Description | Default |
|---|---|---|
| title | Azure vote app title. | Azure Vote App |
| value1 | Value for first vote control / value | Cats |
| value2 | Value for second vote control / value | Dogs |
| password | Password for azure vote app | mysecret | 
| serviceName | Name for Kubernetes service. | aks-helloworld |
| serviceType | Type for Kubernetes service. | ClusterIP |

Note: For more complex values for password, such as data structures (a.b[0].c), use a similar structure as below to install the helm chart, but replace "password" with the data structure, i.e. "--set a.b[0].c=passwordValue".


## Examples

```
helm install azure-samples/azure-vote-protected
```

![azure-vote cats and dogs](../images/vote1.png)

```
helm install azure-samples/azure-vote-protected --set title="Winter Sports" --set value1=Ski --set value2=Snowboard --set password=mysecret
```

![azure-vote ski and snowboard](../images/vote2.png)


