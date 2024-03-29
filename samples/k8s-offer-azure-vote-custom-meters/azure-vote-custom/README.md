# azure-vote-custom

The Azure Vote custom meters application is a simple sample to demonstrate custom meters usage in a Kubernetes application. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage. The application submits usage data to Azure Commerce Metering API for every vote casted in the last hour(s).

## Installing the Chart

Add the Azure Samples chart repository.

```
helm repo add azure-samples https://azure-samples.github.io/helm-charts/
```

Install the chart.

```
helm install azure-samples/azure-vote-custom
```


## Configuration

The following tables lists the configurable parameters of the azure-vote chart and the default values.

| Parameter | Description | Default |
|---|---|---|
| title | Azure vote app title. | Azure Vote App |
| value1 | Value for first vote control / value | Cats |
| value2 | Value for second vote control / value | Dogs |
| serviceName | Name for Kubernetes service. | aks-helloworld |
| serviceType | Type for Kubernetes service. | ClusterIP |

## Examples

```
helm install azure-samples/azure-vote-custom
```

![azure-vote cats and dogs](../images/vote1.png)

```
helm install azure-samples/azure-vote-custom --set title="Winter Sports" --set value1=Ski --set value2=Snowboard
```

![azure-vote ski and snowboard](../images/vote2.png)


