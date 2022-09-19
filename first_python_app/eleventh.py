import requests

global_test =  requests.get('https://api.coinlore.net/api/tickers/')
x = global_test.json()

# print(x['data'])


price_list = dict()
for i in x['data'][0:6]:
    price_list[i['symbol']]= i['price_usd']
 

print(price_list)