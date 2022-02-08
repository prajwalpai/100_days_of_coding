import requests
import datetime

USERNAME = 'prajwalpai'
TOKEN= 'jibberswabberishingpish'

#1 Create your user account

pixela_endpoint = 'https://pixe.la/v1/users'
params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#Execute only onc
#response = requests.post(url = pixela_endpoint, json = params)

#2 : Create a graph definition
#curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{}'

json_data = {
    "id":"med-graph",
    "name":"My-Meditation",
    "unit":"mins",
    "type":"int",
    "color":"shibafu"
}

#Execute only once
#response = requests.post(url = pixela_endpoint + '/' + USERNAME + '/graphs', json = json_data, headers= {'X-USER-TOKEN': TOKEN})

#3. Get the graph!

#https://pixe.la/v1/users/prajwalpai/graphs/med-graph.html

#4. Post value to the graph

#$ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

date = datetime.datetime.now()
fdate = date.strftime("%Y%m%d")
response = requests.post(url=pixela_endpoint + '/' + USERNAME + '/graphs/med-graph', json = {'date': fdate, 'quantity':'10'}, headers = {'X-USER-TOKEN': TOKEN})

#5. Update the Graph
url=pixela_endpoint + '/' + USERNAME + '/graphs/med-graph/'+fdate
#response = requests.put(url = url, json = {'quantity':"15"},  headers = {'X-USER-TOKEN': TOKEN})


