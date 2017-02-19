from urllib2 import Request, urlopen, URLError
import requests
import simplejson as json
from pymongo import MongoClient

'''
TODO
'''
#def addUser
api = open("apikey")

def lookUp(summoner):
	key = api.read()
	# #request = Request("http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg")
	# #summoner = raw_input("Enter Summoner Name: ")
	url1 = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summoner.lower() + "?api_key=" + key

	request = Request(url1)
	dic = {}
	try:
		response = urlopen(request)
		content = response.read()
		#filename = summoner + ".json"
		#f = open(filename, 'wb')
		#f.write(response.read())
		dic = json.loads(content)
		url2 = "https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/" + str(dic[summoner]['id']) + "/ranked" + "?&api_key=" + key
		request = requests.get(url2)
		dic = json.loads(request.text)
		data = json.dumps(dic, sort_keys=True, indent=4, separators=(',', ': '))
		filename = summoner + ".json"
		#f = open(filename.upper(), 'w+')
		#f.write(prnt)
		#f.close()
		#print content[559:1000]
		result = {}
		result = dic['champions']
		totaldmg = totalkills = totaldeaths = totalassists = 0
		for stat in result:
			if(stat['id'] == 0):
				totaldmg += stat['stats']['totalDamageDealt']
				totalkills += stat['stats']['totalChampionKills']
				totalassists += stat['stats']['totalAssists']
			totaldeaths += stat['stats']['totalDeathsPerSession']
		string = "In their ranked games, summoner " + summoner + " has done a total of " + str(totaldmg) + " damage over " + str(totalkills) + " kills, " + str(totaldeaths) + " deaths, and " + str(totalassists) + " assists. \n\n\n" + data
		# for x in data.get('champions'):
			# print x
			# print x.get('id')
			# result.append(x.get('id'), x.get('stats').get('maxChampionsKilled'))

		return string
	except URLError, e:
		return "exception thrown"