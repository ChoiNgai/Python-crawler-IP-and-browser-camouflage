'''
使用代理访问
'''
import urllib.request
import random

url = 'https://www.studydrive.club/2019/10/15/xue-xi-bi-ji-ji-suan-ji-wang-luo/'

# 创建一个ｉｐｌｉｓｔ，随机使用ｉｐ
iplist = ['101.23.0.102','101.23.0.103', '101.23.0.125']
# 创建一个代理opener
proxy_support = urllib.request.ProxyHandler({'http': iplist[random.randint(0, len(iplist))]})
opener = urllib.request.build_opener(proxy_support)

# 添加浏览器的伪装头部
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0')]
for i in range(1,10):
  # 使用代理ｏｐｅｎｅｒ访问url
  response = opener.open(url)

  html = response.read().decode('utf-8')
print(html)