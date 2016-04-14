
import cPickle as pickle

stationList = pickle.load( open( "/home/ubuntu/data/stations.p", "rb" ) )

print stationList['Waterloo']
#stationList['Victoria']