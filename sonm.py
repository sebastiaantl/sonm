from pprint import pprint
from flask import render_template
#curl -s https://dwh.livenet.sonm.com:15022/DWHServer/GetDeals/ -d '{"status":1}' > text.json
import requests
import json
r = requests.get('https://dwh.livenet.sonm.com:15022/DWHServer/GetDeals/', data = '{"status":1}')
data = r.json()
with open('text.json', 'w') as f:
    json.dump(data, f)

with open('text.json') as f:
    data = json.load(f)
live_deals = len(data['deals'])

unit = 10**18.0
def price_converter(price):
    price = float (price)
    usd_hour = float (price / unit)
    usd_hour = usd_hour * 3600
    return usd_hour

def time_converter(time):
    hour_time = float(time/3600)
    return hour_time

live_deals_ids = []
consumers = []
suppliers = []
hourly_volume = 0
total_eth_hash = 0
for x in data['deals']:
    live_deals_ids.append(int(x['deal']['id']))
    consumers.append(x['deal']['consumerID'])
    suppliers.append(x['deal']['supplierID'])
    #if 'duration' in(x['deal'].keys()):
    prices = price_converter(price=x['deal']['price'])
    hourly_volume += prices
    total_eth_hash += x['deal']['benchmarks']['values'][9]


total_eth_hash = total_eth_hash /1000000
consumers = sorted(set(consumers))
suppliers = sorted(set(suppliers))
live_deals_ids = sorted(live_deals_ids)
total_deals = max(live_deals_ids)
unique_consumers_amount = len(consumers)
unique_suppliers_amount = len(suppliers)