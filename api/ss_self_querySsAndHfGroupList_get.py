#coding=utf8

import requests
from read import url_post
from read import header

#查询对应城市下的方案信息
def ss_self_querySsAndHfGroupList_get():
    body = {
        "cityCode":"310100"
    }

    url = url_post() + 'self_querySsAndHfGroupList'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_self_querySsAndHfGroupList_get()