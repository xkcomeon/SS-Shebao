#coding=utf8

import requests
from read import url_post
from read import header

#根据参保城市获取开票抬头和单立户
def ss_getSSOrgIdAndInvoiceHead_get():
    body = {
        "cityCode":"$cityCode",     #参保城市code
        "type":0,   # 0：社保公积金、1：社保、2：公积金
        "userId":"$userId"       #参保员工ID
    }

    url = url_post() + 'getSSOrgIdAndInvoiceHead'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getSSOrgIdAndInvoiceHead_get()