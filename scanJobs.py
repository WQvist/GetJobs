import requests, os, json, datetime

now = datetime.datetime.now()
url = 'http://api.arbetsformedlingen.se/af/v0/platsannonser/matchning?kommunid=1480&nyckelord="mjukvaruutvecklare"OR"systemutvecklare"OR"programmerare"OR"it"OR"backend-utvecklare"&Sokdatum=%d-%d-%dT0000+0100&antalrader=200' %(now.year, now.month, now.day) # 2512 = Mjukvaru- och systemutvecklare m.fl., 1480 = Göteborg
res = requests.get(url, headers={'Accept-Language': 'sv'})
res.raise_for_status()	# Raise exception if there was an error
with open('C:\\Users\\William\\Desktop\\test.txt', 'w') as outfile:
    json.dump(res.json(), outfile)
data=json.loads(res.content)
output=data['matchningslista']
lista=output['matchningdata']	# Lista med alla annonser

# Printa alla annonsrubriker
for annonser in lista:
	print(annonser['publiceraddatum'])
