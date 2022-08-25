import requests

url = "https://coinranking1.p.rapidapi.com/coins"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"1y","tiers":"1","orderBy":"marketCap","orderDirection":"desc","limit":"5","offset":"0"}

headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "your key"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open('data.json', 'w') as json:
    json.write(response.text)

import json
import matplotlib.pyplot as plt

with open('data.json', 'r') as dataFile:
    data = json.load(dataFile)

for a in range(len(data['data']['coins'])):
    y = []
    for b in data['data']['coins'][a]['sparkline']:
        if(b != None):
            y.append(float(b))

    x = range(len(y))
    
    plt.plot(x, y, label=data['data']['coins'][a]['name'])

plt.xlabel('data over 1 year')
plt.ylabel('price (USD)')
plt.title('crypto data')
plt.legend()
plt.show()
