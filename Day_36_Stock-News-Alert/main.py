import os
import requests
from newsapi import NewsApiClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api = os.environ['STOCK_API_KEY']
news_api = os.environ['NEWS_API_KEY']

url = 'https://www.alphavantage.co/query?'
PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': stock_api
}
r = requests.get(url, params=PARAMS)
data = r.json()
date1 = list(data['Time Series (Daily)'])[0]
date2 = list(data['Time Series (Daily)'])[1]

date1_closing = data['Time Series (Daily)'][date1]['4. close']
date2_closing = data['Time Series (Daily)'][date2]['4. close']

change = float(date1_closing) - float(date2_closing)
percentage_change = round((100 * change) / (float(date2_closing)), 2)

print(f"Yesterday closing = {date1_closing}\nDay before Yesterday closing = {date2_closing}\n\
     change = {round(change, 2)}\
     \nPercentage Change = {percentage_change}")

if percentage_change > 5:
    newsapi = NewsApiClient(api_key=news_api)
    sources = newsapi.get_sources()
    source_list = []
    for item in sources['sources']:
        source_list.append(item['name'])

    source_list_string = ','.join([str(elem) for elem in source_list])
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME, sources=source_list_string)
    for newsitem in top_headlines['articles'][:3]:
        print(newsitem['title'])
