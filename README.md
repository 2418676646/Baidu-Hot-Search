# Baidu-Hot-Search
获取百度热搜前30榜单，每天定时推送

### 介绍

本项目基于Python 3.11.1构建，你需要在https://www.pushdeer.com获取提送key，pushdeer是一个免费的推送服务，支持Mac iOS Android

### 开始

安装依赖

```python
pip install requests
pip install bs4 
pip install BeautifulSoup
```

替换代码38行的key

```python
push_key = 'your key'
```

### Run

#

### 定时推送

把baidu.py部署到服务器（服务器请自行安装python需要的依赖环境）

设置定时任务(每天早晚9.30运行一次)那么一天就会推送2次

编写定时任务

```
crontab -e
```

写入

```
30 9,21 * * * /usr/bin/python3 /path/baidu.py
```

重启服务

```
systemctl restart crond.service
```

