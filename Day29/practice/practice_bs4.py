from cgitb import text
from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

tbody = doc.tbody
trs = tbody.contents
prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    print(name, price)

prices[fixed_name] = fixed_price


print(prices)
