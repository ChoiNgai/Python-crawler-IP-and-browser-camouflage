import urllib.request
import requests
import time
import ssl
import random

def openUrl(ip, agent):
    headers = {'User-Agent': agent}
    proxies = {'http' : ip}
    requests.get("https://www.studydrive.club/2020/03/21/xue-xi-bi-ji-r-yu-yan/", headers=headers, proxies=proxies, verify=True)
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Access to success.")

#IP池
#IP来源：
# http://www.xicidaili.com/
# https://www.kuaidaili.com/free/
def randomIP():
    ip = random.choice(['101.23.0.102', '101.23.0.103', '101.23.0.125'])
    return ip

#User-Agent
#User-Agent来源：http://www.useragentstring.com/pages/useragentstring.php
def randomUserAgent():
    UserAgent = random.choice([
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
        'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
        'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
        'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'


    ])
    return UserAgent

if __name__ == '__main__':
    for i in range(10):
        ip = randomIP()
        agent = randomUserAgent()
        openUrl(ip, agent)
        time.sleep(10)
