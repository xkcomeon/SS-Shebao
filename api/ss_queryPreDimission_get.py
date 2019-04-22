#coding=utf8

import requests
from read import url_post
from read import header

#获取首页待离职未停保
def ss_queryPreDimission_get():
    body = {
        "page": 1,
        "pageSize": 10
    }

    url = url_post() + 'queryPreDimission'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_queryPreDimission_get()