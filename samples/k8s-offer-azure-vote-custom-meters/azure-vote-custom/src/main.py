from flask import Flask, request, render_template
import os
import random
import redis
import socket
import sys
import requests
import datetime
import uuid
import json

app = Flask(__name__)

# Load configurations from environment or config file
app.config.from_pyfile('config_file.cfg')

if ("VOTE1VALUE" in os.environ and os.environ['VOTE1VALUE']):
    button1 = os.environ['VOTE1VALUE']
else:
    button1 = app.config['VOTE1VALUE']

if ("VOTE2VALUE" in os.environ and os.environ['VOTE2VALUE']):
    button2 = os.environ['VOTE2VALUE']
else:
    button2 = app.config['VOTE2VALUE']

if ("GETVALUE" in os.environ and os.environ['GETVALUE']):
    button4 = os.environ['GETVALUE']
else:
    button4 = app.config['GETVALUE']

if ("TITLE" in os.environ and os.environ['TITLE']):
    title = os.environ['TITLE']
else:
    title = app.config['TITLE']

# Redis configurations
redis_server = os.environ['REDIS']


# Redis Connection
try:
    if "REDIS_PWD" in os.environ:
        r = redis.StrictRedis(host=redis_server,
                        port=6379,
                        password=os.environ['REDIS_PWD'])
    else:
        r = redis.Redis(redis_server)
    r.ping()
except redis.ConnectionError:
    exit('Failed to connect to Redis, terminating.')

# Change title to host name to demo NLB
if app.config['SHOWHOST'] == "true":
    title = socket.gethostname()

# Init Redis
if not r.get(button1): r.set(button1,0)
if not r.get(button2): r.set(button2,0)
# store number of votes casted until synced with metering api using VOTES key
if not r.get('VOTES'): r.set('VOTES',0)
# store last sync time with metering api using LASTSYNC key
if not r.get('LASTSYNC'): r.set('LASTSYNC',str(datetime.datetime.now() + datetime.timedelta(days=-1)))

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        # Get current values
        vote1 = r.get(button1).decode('utf-8')
        vote2 = r.get(button2).decode('utf-8')

        # Return index with values
        return render_template("index.html", value1=int(vote1), value2=int(vote2), button1=button1, button2=button2, title=title, button4=button4, meteringResponse='')

    elif request.method == 'POST':

        if request.form['vote'] == 'reset':
            
            # Empty table and return results
            r.set(button1,0)
            r.set(button2,0)
            vote1 = r.get(button1).decode('utf-8')
            vote2 = r.get(button2).decode('utf-8')
            return render_template("index.html", value1=int(vote1), value2=int(vote2), button1=button1, button2=button2, title=title, button4=button4, meteringResponse='')
        
        elif request.form['vote'] == button4:
            
            vote1 = r.get(button1).decode('utf-8')
            vote2 = r.get(button2).decode('utf-8')
            resp = getCustomUsageFromMeteringAPI()
            pretty_json = json.loads(resp.text)

            meteringResponse = "Last day usage status: {0} response: {1}".format(resp.status_code, json.dumps(pretty_json, indent=2))

            return render_template("index.html", value1=int(vote1), value2=int(vote2), button1=button1, button2=button2, title=title, button4=button4, meteringResponse=meteringResponse)

        else:

            # Insert vote result into DB
            vote = request.form['vote']
            r.incr(vote,1)
            
            # Get current values
            vote1 = r.get(button1).decode('utf-8')
            vote2 = r.get(button2).decode('utf-8')  
            
            r.incr('VOTES',1)
            # get last sync time from cache and if the usage is sent within last hour, store the votes in cache
            lastSyncTime = datetime.datetime.strptime(r.get('LASTSYNC').decode('utf-8'), '%Y-%m-%d %H:%M:%S.%f')
            totalIngestableVotes = r.get('VOTES').decode('utf-8')
            if lastSyncTime < (datetime.datetime.now() + datetime.timedelta(hours=-1)):
                resp = sendCustomUsageToMeteringAPI(totalIngestableVotes)
                pretty_json = json.loads(resp.text)
                meteringResponse = "Metering API Response for the click usage for {0} votes in last hour(s), status: {1} response: {2}".format(totalIngestableVotes, resp.status_code, json.dumps(pretty_json, indent=2))

                if resp.status_code == 200:
                    # reset number of votes to be synced with metering api
                    r.set('VOTES',0)
                    # set last sync time with metering api
                    r.set('LASTSYNC', str(datetime.datetime.now()))

            else:
                meteringResponse = "Usage was sent to metering api recently, last sync time: {0}, total votes to be ingested: {1}".format(str(lastSyncTime), totalIngestableVotes)

            # Return results
            return render_template("index.html", value1=int(vote1), value2=int(vote2), button1=button1, button2=button2, title=title, button4=button4, meteringResponse=meteringResponse)

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

if __name__ == "__main__":
    app.run()
