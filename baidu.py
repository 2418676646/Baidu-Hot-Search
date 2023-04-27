import requests
from bs4 import BeautifulSoup
# 请求热搜网站
url = 'https://top.baidu.com/board?tab=realtime'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'

}
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# 获取热搜列表
hot_list = soup.find_all(class_='category-wrap_iQLoo')

message = ''

## 对热搜列表进行排序，将第一条数据排在第二位，其他数据位置不变
hot_list = hot_list[1:2] + hot_list[:1] + hot_list[2:]

# 遍历热搜列表获取热搜信息
for index, hot in enumerate(hot_list[:31], start=1):
    # 获取热搜标题和链接
    title = hot.find(class_='c-single-text-ellipsis').get_text(strip=True)
    link = hot.find('a')['href']

    # 获取热搜指数
    index_num = hot.find(class_='hot-index_1Bl1a').get_text(strip=True)

    if index == 1:
      message += '置顶   \n'
    else:
      message += f'Top{index-1}: [{title}]({link})   \n'
# 打印31条热搜信息
print(message)

# 推送信息
push_url = 'https://api2.pushdeer.com/message/push'
push_key = 'key'

push_data = {
    'pushkey': push_key,
    'text': '百度热搜榜单',
    'desp': message,
    'type': 'markdown'
}

try:
    response = requests.post(push_url, data=push_data)
    response.raise_for_status()
    print('推送成功')
except requests.exceptions.HTTPError:
    print('推送失败')
