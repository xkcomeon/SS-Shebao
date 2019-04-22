#coding=utf8

import requests
from read import url_post
from read import header

#根据参保城市获取社保方案
def ss_getInsuredCityCode_get():
    body = {
        "ssOrgId": "$ssOrgId",
		"type": 1 ,    #社保：1  公积金：2  社保公积金:0
		"cityCode":110100
    }

    url = url_post() + 'getInsuredCityCode'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getInsuredCityCode_get()