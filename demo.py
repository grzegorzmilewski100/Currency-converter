import json
import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = "INR"
currency_2 = "USD"
amount = "1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "7b5fc175bfmsh53ccb1d1aac6d66p1dabfbjsnd8128b0d81c7",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount= data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount,formatted)