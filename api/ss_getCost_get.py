#coding=utf8

import requests
from read import url_post
from read import header

#获取工本费
def ss_getCost_get():
    #参保方案入参详情
    body = {
    "userId":"2134366216756994",
    "userName":"小朱",
    "position":"",
    "workPlace":"",
    "ssInfo":{
        "isOff":"false",
        "cityCode":"310100",
        "invoiceId":"invoiceb47c6f1915334d3ba6e003c6014984ad",
        "ssOrgId":"2f48d2135b2444ff92937bb673375cd6",
        "schemeId":"2f48d2135b2444ff92937bb673375cd6-e94d8548898411e8a13252540080f838",
        "baseNum":4279,
        "startDate":"2018-11",
        "firstInsuredType":2,
        "forcePaymentMonths":[

        ]
    },
    "hfInfo":{
        "isOff":"false",
        "cityCode":"310100",
        "invoiceId":"invoiceb47c6f1915334d3ba6e003c6014984ad",
        "ssOrgId":"2f48d2135b2444ff92937bb673375cd6",
        "schemeId":"2f48d2135b2444ff92937bb673375cd6-e94d8548898411e8a13252540080f839",
        "baseNum":2300,
        "startDate":"2018-11",
        "firstInsuredType":2,
        "forcePaymentMonths":[

        ]
    }
}
    url = url_post() + 'getCost'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getCost_get()