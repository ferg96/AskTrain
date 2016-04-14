from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import cPickle as pickle

stationList = pickle.load( open( "/home/ubuntu/data/stations.p", "rb" ) )
BaseStation = process.extract("paddington",stationList.keys(),limit=1)

#get only station name
res_list = [x for x,_ in BaseStation]
#res_list= listToStringWithoutBrackets(res_list)
#print res_list

#get CRS code
for i in res_list:
    BaseStationCRS = d[i]

from suds.client import Client

client = Client('https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-11-27')

client.set_options(soapheaders={'AccessToken': {'TokenValue': '1ca73af3-ce9a-43c6-a1d7-5b5b714fb7bf'}})

HelloWorld = client.service.GetArrivalBoard(numRows=5,crs=BaseStationCRS,filterCrs='',filterType='to',timeOffset=0,timeWindow=60)

#print HelloWorld

print HelloWorld.trainServices
