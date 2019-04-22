#coding=utf8

import requests
from read import url_post
from read import header

#查询方案下的险种详情
def ss_self_querySsAndHfItemList_get():
    body = {
        "groupCode":"f94d8548898411e8a13252540080f839"    #方案ID--schemeId
    }

    url = url_post() + 'self_querySsAndHfItemList'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_self_querySsAndHfItemList_get()