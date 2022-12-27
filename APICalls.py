import requests
import APIKEY

url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers = {
  "apikey": ""
          }

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

print(result)
