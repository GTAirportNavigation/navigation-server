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
