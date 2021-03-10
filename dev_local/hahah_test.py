import urllib.request
import requests
import time
import ssl
import random


def openUrl(ip, agent):
    headers = {'User-Agent': agent}  # 伪装浏览器型号
    proxies = {'http': ip}  # 伪装ip地址
    requests.get("https://www.baidu.com/", headers=headers, proxies=proxies, verify=True)
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Access to success.")


# 读取txt文件里的ip地址存储为列表
def ReadTxtName(rootdir):
    lines = []
    with open(rootdir, 'r') as file_to_read:
        while True:
            line = file_to_read.readline()
            if not line:
                break
            line = line.strip('\n')
            lines.append(line)
    return lines


# 随机选取ip
def randomIP(ip_list):
    ip = random.choice(ip_list)
    return ip


# 随机选取浏览器型号
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
    ip_list = ReadTxtName('ping713.txt')  # 读入有效ip储存为列表
    ip = randomIP(ip_list)  # 随机选择ip
    agent = randomUserAgent()  # 随机选择浏览器型号
    openUrl(ip, agent)  # 打开网页
    time.sleep(10)
