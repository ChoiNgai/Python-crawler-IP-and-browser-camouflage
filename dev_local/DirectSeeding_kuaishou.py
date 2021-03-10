import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}

def first_get_request(first_request):
    first_data = json.loads(first_request.text)
    print(first_data)
    #进入第二层
    first_two_data = first_data['data']['videoFeeds']['list']
    for num in first_two_data:
        two_url = 'https://live.kuaishou.com/u/' + num['user']['id'] + '/' + num['photoId']
        # print(two_url)
        two_get_request(two_url)


def two_get_request(two_url):
    two_data = requests.get(url=two_url,headers=headers,verify=False)
    soup = BeautifulSoup(two_data.text,'lxml')
    #头像
    name_photo = soup.select('.profile-user img')[0]['src']
    #名字
    name = soup.select('.video-card-footer-user-name')[0].text
    #点赞量
    number = soup.select('.profile-user-count-info > .watching-count')[0].text
    #点心量
    num = soup.select('.profile-user-count-info > .like-count')[0].text
    #内容
    text = soup.select('.profile-user > .profile-user-desc > span')[0].text
    item = {
        '头像':name_photo,
        '名字':name,
        '内容':text,
        '点赞量':number,
        '点心量':num
    }
    with open('爬取的信息.txt','a',encoding='utf8') as f:
        f.write(str(item) + '\n')

        time.sleep(3)

def main():
    first_url = 'https://live.kuaishou.com/graphql'
    formdata = {
        "operationName": "videoFeedsQuery", "variables": {"count": 50, "pcursor": "50"},
        "query": "fragment VideoMainInfo on VideoFeed {\n  photoId\n  caption\n  thumbnailUrl\n  poster\n  viewCount\n  likeCount\n  commentCount\n  timestamp\n  workType\n  type\n  useVideoPlayer\n  imgUrls\n  imgSizes\n  magicFace\n  musicName\n  location\n  liked\n  onlyFollowerCanComment\n  width\n  height\n  expTag\n  __typename\n}\n\nquery videoFeedsQuery($pcursor: String, $count: Int) {\n  videoFeeds(pcursor: $pcursor, count: $count) {\n    list {\n      user {\n        id\n        eid\n        profile\n        name\n        __typename\n      }\n      ...VideoMainInfo\n      __typename\n    }\n    pcursor\n    __typename\n  }\n}\n"
    }
    #访问快手界面
    first_request = requests.post(url=first_url,headers=headers,data=formdata,verify=False)
    #分析首页链接
    first_get_request(first_request)

if __name__ == '__main__':
    main()
