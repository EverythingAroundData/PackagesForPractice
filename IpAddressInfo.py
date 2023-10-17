import requests

proxies = {
	'htps':'https://144.255.176.161:4153'
}

response = requests.get('https://ipinfo.io/json', proxies=proxies)
print(response.text)

