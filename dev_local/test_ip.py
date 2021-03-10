def ip_test(ip):
    proxies = {
        'http': 'http://' + ip,
        'https': 'https://' + ip,
    }
    print(proxies)
    try:
        response = requests.get(ip_url,headers=headers,proxies=proxies,timeout=3)    #timeout 接收回应最大延时
        if response.status_code == 200:
            with open('ip_list.txt','a') as f:
                f.write(ip)
                f.write('\n')
            print('测试通过')
            print(proxies)
            print(response.text)
    except Exception as e:
        print(e)