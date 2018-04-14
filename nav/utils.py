from __future__ import print_function
import requests
from requests import Session
from requests.auth import HTTPBasicAuth
import zeep
from zeep import Client
from zeep.wsse.username import UsernameToken
from zeep import xsd
from zeep.cache import SqliteCache
from zeep.transports import Transport
import collections
import time
from bs4 import BeautifulSoup

username = ''
password = ''

def init_flight_aware():
	global username
	global password

	with open('aware.txt') as f:
		username = f.readline().strip()
		password = f.readline().strip()

def get_gate(flightId):
	init_flight_aware()

	session = Session()
	session.auth = HTTPBasicAuth(username, password)


	transport = Transport(cache=SqliteCache(), session=session)
	client = Client('http://flightxml.flightaware.com/soap/FlightXML2/wsdl', transport = transport)

	response0 = zeep.helpers.serialize_object(client.service.FlightInfo(flightId, 15), target_cls=collections.OrderedDict)

	flight = 0

	while((flight < 14) and ((response0['flights'][flight + 1]['filed_departuretime'] - int(time.time())) > 0)):
	    flight += 1

	filed_departuretime = response0['flights'][flight]['filed_departuretime']

	faFlightID = zeep.helpers.serialize_object(client.service.GetFlightID(flightId, filed_departuretime), target_cls=collections.OrderedDict)

	response1 = client.service.AirlineFlightInfo(faFlightID)

	originGate = response1['gate_orig']

	return originGate

#returns a boolean representing if the flight is on-time or not
def get_on_time(flightId):
	init_flight_aware()

	session = Session()
	session.auth = HTTPBasicAuth(username, password)


	transport = Transport(cache=SqliteCache(), session=session)
	client = Client('http://flightxml.flightaware.com/soap/FlightXML2/wsdl', transport = transport)

	response0 = zeep.helpers.serialize_object(client.service.FlightInfo(flightId, 15), target_cls=collections.OrderedDict)

	flight = 0

	while((flight < 14) and ((response0['flights'][flight + 1]['filed_departuretime'] - int(time.time())) > 0)):
	    flight += 1

	filed_departuretime = response0['flights'][flight]['filed_departuretime']

	filed_ete = response0['flights'][flight]['filed_ete']

	filedFlightLength = int(filed_ete[0:2]) * 3600 + int(filed_ete[3:5]) * 60 + int(filed_ete[6:8])

	estimatedarrivaltime = response0['flights'][flight]['estimatedarrivaltime']

	return (((filed_departuretime + filedFlightLength) - estimatedarrivaltime) < 15*60)

#returns the filed departure time as an integer in Unix Epoch time.
#If presenting directly to users, it's necessary to convert this to normal human readable time.
#https://stackoverflow.com/questions/3682748
def get_filed_departure_time(flightId):
	init_flight_aware()

	session = Session()
	session.auth = HTTPBasicAuth(username, password)


	transport = Transport(cache=SqliteCache(), session=session)
	client = Client('http://flightxml.flightaware.com/soap/FlightXML2/wsdl', transport = transport)

	response0 = zeep.helpers.serialize_object(client.service.FlightInfo(flightId, 15), target_cls=collections.OrderedDict)

	flight = 0

	while((flight < 14) and ((response0['flights'][flight + 1]['filed_departuretime'] - int(time.time())) > 0)):
	    flight += 1

	filed_departuretime = response0['flights'][flight]['filed_departuretime']

	return filed_departuretime

#returns the estimated time of arrival as an integer in Unix Epoch time.
#If presenting directly to users, it's necessary to convert this to normal human readable time.
#https://stackoverflow.com/questions/3682748
def get_estimated_arrival_time(flightId):
	init_flight_aware()

	session = Session()
	session.auth = HTTPBasicAuth(username, password)


	transport = Transport(cache=SqliteCache(), session=session)
	client = Client('http://flightxml.flightaware.com/soap/FlightXML2/wsdl', transport = transport)

	response0 = zeep.helpers.serialize_object(client.service.FlightInfo(flightId, 15), target_cls=collections.OrderedDict)

	flight = 0

	while((flight < 14) and ((response0['flights'][flight + 1]['filed_departuretime'] - int(time.time())) > 0)):
	    flight += 1

	estimatedarrivaltime = response0['flights'][flight]['estimatedarrivaltime']

	return estimatedarrivaltime

def get_wait_times():
	page = requests.get("http://apps.atl.com/Passenger/FlightInfo/Default.aspx")
	waitTimes = []

	soup = BeautifulSoup(page.text, "html.parser")

	securityWaitTextList = soup.find(id="bodySection_wucSecurityWaitTimes_upnWaitTime").find_all("p")

	for checkpointText in securityWaitTextList:
		if ("closed" in str(checkpointText)):
			waitTimes.append(-1)
		elif ("less than 15 minutes" in str(checkpointText)):
			waitTimes.append(0)
		elif ("15 – 30 minutes" in str(checkpointText)):
			waitTimes.append(1)
		else:
			waitTimes.append(2)

	return waitTimes
