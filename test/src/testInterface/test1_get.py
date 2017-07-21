# coding:utf-8
import requests
wd = {"wd": "你是谁"}
r = requests.get("https://www.baidu.com/", params=wd)


print(r.status_code)
print(r.text)
print(r.content)
