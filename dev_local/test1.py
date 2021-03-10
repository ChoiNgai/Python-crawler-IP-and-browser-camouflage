import urllib.request
import time

# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


# 专刷某个页面
print('开始刷了哦：')
tempUrl = 'https://www.studydrive.club/2019/10/15/xue-xi-bi-ji-ji-suan-ji-wang-luo/'



for j in range(100):
    try:
     opener.open(tempUrl)
     time.sleep(7)
     print('%d %s' % (j, tempUrl))
    except urllib.error.HTTPError:
     print('urllib.error.HTTPError')
     time.sleep(1)
    except urllib.error.URLError:
     print('urllib.error.URLError')
     time.sleep(1)