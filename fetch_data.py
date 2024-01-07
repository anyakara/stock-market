import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAWW&outputsize=compact&apikey=3BR7HYUPN64UVULS'
r = requests.get(url)
data = r.json()

#print(data)
# my API keyyy: 3BR7HYUPN64UVULS


time_series_retrieval = data['Time Series (Daily)']#['2022-03-23']

#print(time_series_retrieval)

#should I make a dictionary of every date in the year and set it equal to its day equivalent -- then encode and decode?

print('start of fetching open')
for i in time_series_retrieval:
    print(time_series_retrieval[i]['1. open'])
print('end of fetching close')


'''

{'Meta Data': 
{'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'IBM', '3. Last Refreshed': '2022-03-23 16:00:01', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 
'Time Series (Daily)': 
{'2022-03-23': {'1. open': '129.0800', '2. high': '129.3200', '3. low': '128.2500', '4. close': '128.3000', '5. volume': '2923232'}, 
'2022-03-22': {'1. open': '128.5000', '2. high': '129.3000', '3. low': '127.8500', '4. close': '129.0600', '5. volume': '2649026'}, 
'2022-03-21': {'1. open': '129.0000', '2. high': '129.7400', '3. low': '127.4000', '4. close': '128.1000', '5. volume': '3379393'}, 
'2022-03-18': {'1. open': '127.3800', '2. high': '128.9300', '3. low': '126.3700', '4. close': '128.7600', '5. volume': '7400216'},


'''




