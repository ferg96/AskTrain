

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import cPickle as pickle
from suds.client import Client



def(intentString, fromStation, toStation):

	client = Client('https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-11-27')
	client.set_options(soapheaders={'AccessToken': {'TokenValue': '1ca73af3-ce9a-43c6-a1d7-5b5b714fb7bf'}})
	
	stationList = pickle.load( open( "/home/ubuntu/data/stations.p", "rb" ) )
	StationFrom = process.extract(fromStation,stationList.keys(),limit=1)
	#get only station name
	resultListFrom = [x for x,_ in StationFrom]
	#get CRS code
	for i in resultListFrom:
		StationFromCRS = d[i]
	
	if (intentString == 'BasicSearch'):
	
		StationTo = process.extract(toStation,stationList.keys(),limit=1)
		resultListTo = [x for x,_ in StationTo]
		#get CRS code
		for i in resultListTo:
			StationToCRS = d[i]
			
		ResultData = client.service.GetDepartureBoard(numRows=5,crs=StationToCRS,filterCrs='',filterType='to',timeOffset=0,timeWindow=60)
			
		elif:
		
		ResultData = client.service.GetDepartureBoard(numRows=5,crs=StationFromCRS,filterCrs='',filterType='from',timeOffset=0,timeWindow=60)
	


	return ResultData