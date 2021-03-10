import re
import requests
from requests import RequestException
import time
import random
import os


#读取txt文件里的ip地址存储为列表
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

def get_page(url,ip_list):
    try:
        ip = random.choice(ip_list)
        proxies = {'http': ip}
        headers = {
            'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
            'User-Agent' : random.choice([
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
            # 伪装成浏览器
        }
        response = requests.get(url, headers=headers,proxies=proxies)
        print(headers)
        print(proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求出错')
        return None


def parse_page(html):
    try:
        read_num = int(re.compile('<span.*?read-count.*?(\d+).*?</span>').search(html).group(1))
        return read_num
    except Exception:
        print('解析出错')
        return None


def main():
    ip_list = ReadTxtName('/root/WebBrush/ipadress.txt')       #读入有效ip储存为列表
    csdnBlogUrl = ReadTxtName('/root/WebBrush/csdnBlogUrl.txt')    #读入博客链接储存为列表
    now = time.strftime("%H")                       #获得当前小时
    if str(now) == str(23):                         #23：00之后退出程序
        os._exit(0)
    try:
        while 1:
            random.shuffle(csdnBlogUrl)         #打乱博客地址列表顺序
            for i in range(0,len(csdnBlogUrl)-6):   #每一轮后面的6篇文章不刷
                url = csdnBlogUrl[i]
                html = get_page(url,ip_list)
                if html:
                    read_num = parse_page(html)
                    if read_num:
                        print('当前阅读量：', read_num)
                time.sleep(random.randint(2, 4))    #每篇文章中间来点间隔
            # url = 'https://blog.csdn.net/qq_43337115/article/details/101056850'  # 简单曲线拟合
            # html = get_page(url,ip_list)
            # if html:
            #     read_num = parse_page(html)
            #     if read_num:
            #         print('当前阅读量：', read_num)

            sleep_time = random.randint(10, 300)
            print('please wait', sleep_time, 's')
            time.sleep(sleep_time)  # 设置访问频率，过于频繁的访问会触发反爬虫
    except Exception:
        print('出错啦！')


if __name__ == '__main__':
    main()

