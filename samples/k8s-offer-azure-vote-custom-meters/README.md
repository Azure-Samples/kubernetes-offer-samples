---
page_type: sample
languages:
- yaml
- json
products:
- azure-kubernetes-service
- azure-marketplace
---

# Custom Meters for Azure Marketplace Kubernetes Applications Sample

This sample demonstrates how to use custom meters in a Kubernetes application. The application consists of two pods, one running a flask web form, and the second a redis instance for temporary data storage. The application submits usage data to Azure Commerce Metering API for every vote casted per hour.

For more detail about custom meter and how it can be setup in the partner center, please refer to [documentation](https://learn.microsoft.com/en-us/partner-center/marketplace/azure-container-metered-billing#sample-custom-pricing-options)

# How it works

To submit usage data to Azure Commerce Metering API, you need to add the following information in the [values.yaml](./azure-vote-custom/values.yaml) file:

```yaml
global:
  azure:
    identity:
      # Application's Managed Service Identity (MSI) Client ID. ClientID can be used to generate authentication token to communicate to external services like Microsoft Marketplace Metering API
      clientId: "DONOTMODIFY" # Azure populates this value at deployment time
    marketplace:
      # id of the plan purchased for the Azure Marketplace Kubernetes application,to be used in usage event payload to metering api, for more information please refer: https://learn.microsoft.com/en-us/partner-center/marketplace/marketplace-metering-service-apis 
      planId: "DONOTMODIFY" # Azure populates this value at deployment time
    extension:
      # resource id of the Azure Marketplace Kubernetes application,to be used in usage event payload to metering api, for more information please refer: https://learn.microsoft.com/en-us/partner-center/marketplace/marketplace-metering-service-apis 
      resourceId: "DONOTMODIFY" # application's Azure Resource ID, Azure populates this value at deployment time
```


Inside your code, you can follow the difference between [main.py](./azure-vote-custom/src/main.py) and [original-main.py](../k8s-offer-azure-vote/azure-vote/src/main.py)

Here is a snippet on how to generate MSI based authentication token and send usage event to metering API:
```python
# getMsiToken gets the MSI identity based authentication token from IMDS service running on the AKS cluster (endpoint http://169.254.169.254)
def getMsiToken():
    # audience for the token to be generated 
    resource = '20e940b3-4c77-4b0b-9a53-9e16a1b010a7'
    client_id = os.environ['CLIENT_ID']
    url = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&client_id={0}&resource={1}".format(client_id,resource)
    headers = {'Metadata': 'true'}

    resp = requests.get(url)
    resp = requests.get(url, headers=headers)
    print("getMsiToken got response successfully")

    return resp.json()

# sendCustomUsageToMeteringAPI sends usage event to metering service 
def sendCustomUsageToMeteringAPI(quantity : str):
    # metering service production URL
    url = 'https://marketplaceapi.microsoft.com/api/usageEvent?api-version=2018-08-31'
    # get resourceId (application's Azure resource id) from environment variable
    resourceId = os.environ['EXTENSION_RESOURCE_ID']
    # get plan id from environment variable
    planId = os.environ['PLAN_ID']
    
    # generate a guid to be used as a correlation id which can be used for debugging purposes with metering service
    correlationId = uuid.uuid4()
    # get MSI identity based bearer token
    token = getMsiToken()
    accessToken = "Bearer {0}".format(token["access_token"])

    # add headers
    headers = {'authorization': accessToken, 'x-ms-correlationid': str(correlationId), 'content-type': 'application/json'}

    # create usage payload, or more information please refer: https://learn.microsoft.com/en-us/partner-center/marketplace/marketplace-metering-service-apis
    usage ={ 
                'resourceUri' : resourceId,
                'planId' : planId,
                'dimension' : 'pervote',
                'quantity' : int(quantity),
                'effectiveStartTime' : str(datetime.datetime.now())
            }
    print("sendCustomUsageToMeteringAPI sending usage: {0}".format(usage))
    print("sendCustomUsageToMeteringAPI using corretion id {0}".format(correlationId))
    resp = requests.post(url, data=json.dumps(usage), headers=headers)
    print("sendCustomUsageToMeteringAPI response from metering API, status: {0} resp : {1}".format(resp.status_code, resp.json()))
    return resp

def getCustomUsageFromMeteringAPI():
    # metering service production URL to get usage events already ingested, add appropriate duration
    url = 'https://marketplaceapi.microsoft.com/api/usageEvents?api-version=2018-08-31&usageStartDate={0}'.format(str(datetime.datetime.now() + datetime.timedelta(days=-1)))
    # generate a guid to be used as a correlation id which can be used for debugging purposes with metering service
    correlationId = uuid.uuid4()

    print("getCustomUsageFromMeteringAPI using corretion id {0}".format(correlationId))

    # get MSI identity based bearer token
    token = getMsiToken()
    accessToken = "Bearer {0}".format(token["access_token"])

    # add headers
    headers = {'authorization': accessToken, 'x-ms-correlationid': str(correlationId), 'content-type': 'application/json'}
    print("getCustomUsageFromMeteringAPI getting usage in last 1 days")
    resp = requests.get(url, headers=headers)
    print("getCustomUsageFromMeteringAPI response from metering API, status: {0} resp : {1}".format(resp.status_code, resp.json()))
    return resp
```