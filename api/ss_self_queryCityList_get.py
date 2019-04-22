#coding=utf8

import requests
from read import url_post
from read import header

#获取所有可投保城市的信息
def ss_self_queryCityList_get():
    body = {
        "city":""
    }

    url = url_post() + 'self_queryCityList'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_self_queryCityList_get()