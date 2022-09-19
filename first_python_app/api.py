import requests

global_test =  requests.get('https://api.coinlore.net/api/tickers/')
x = global_test.json()


symbol = dict()
for i in x['data']:
    symbol[i['symbol']]= i['price_usd']
    
# print(symbol)


usdt = requests.get('http://api.navasan.tech/latest/?api_key=freeH1njcMsLTHCJFd9haMcGI1ZdNK3g&item=usdt')
usdt = usdt.json()
usdt = usdt['usdt']['value']
print(usdt)