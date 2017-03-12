import requests
import json
from lxml import html
 
# Perform request
q = 'timer'
url = 'http://www.MYDOMAIN.com/search?q='+q
r = requests.get(url)
# print r.headers
 
# Get page elements using xpath, and save to a list
itemList = []
tree = html.fromstring(r.content)
items = tree.xpath('//ELEMENT[contains(@class,"MY-CLASS-SELECTOR"]')
for a in items:
    li = {'url': a.get('href')}
    itemList.append(li)
 
 
# Save our result as JSON
with open('results.'+q+'.json', 'w') as outfile:
    json.dump(itemList, outfile)
