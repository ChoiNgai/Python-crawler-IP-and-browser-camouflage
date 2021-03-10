ip = random.choice(['101.23.0.102', '101.23.0.103', '101.23.0.125'])
proxies = {'http': ip}
headers = { "User-agent":
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_5)"
		"AppleWebKit/537.36 (KHTML, like Gecko) "
		"Chrome/50.0.2454.85 Safari/537.36"}
url = 'https://www.baidu.com'
rep = requests.get(url,headers =headers,proxies=proxies,params={})