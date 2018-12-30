import urllib.request

url = "https://api.pro.coinbase.com/products/BTC-USDC/candles/5m"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})


opened_req = urllib.request.urlopen(req)

html_bytes = opened_req.read()

html_str = html_bytes.decode('utf-8')
html = str(html_str)
data = eval(html)
print(data)

print(data[1])
print(data[1][0])