#coding:utf-8

import requests
from read import url_post
from read import header
import json


#getCities  获取城市列表
def ss_getCities_get():
    body = {

    }

    url = url_post() + 'getCities'
    r = requests.get(url,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getCities_get()




