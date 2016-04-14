import requests
import json
import time

inputString = 'show me the departures board for victoria'
httpString = 'https://api.wit.ai/message?v='
todaysDate = time.strftime("%Y%m%d")
prefixString  = '&q='
queryString = inputString.replace(' ', '%20')

requestString = httpString+todaysDate+prefixString+queryString

headers = {
    'Authorization': 'Bearer FPO6ZW3QKJIOC6BCO4KXT5EQCTZTX4UF',
}

r = requests.get(requestString, headers=headers)

tempdata = json.loads(r.text)

#first step is to determine intent
intentString = tempdata['outcomes'][0]['intent']

#list of intents
#BasicSearch
#DepBoard
#
#
#
#



if (intentString == 'DepBoard'):

	searchString = tempdata['outcomes'][0]['_text']
	fromStation = tempdata['outcomes'][0]['entities']['station'][0]['value']
	
	elif (intentString == 'BasicSearch'):
	
	searchString = tempdata['outcomes'][0]['_text']
	fromStation = tempdata['outcomes'][0]['entities']['fromStation'][0]['value']
	toStation = tempdata['outcomes'][0]['entities']['toStation'][0]['value']
	
