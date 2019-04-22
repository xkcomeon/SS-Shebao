#coding:utf-8

import requests
import read


#获取账单详情
def ss_getBillInfo_get():
    body = {
        "ssId": "2b935ca9bfac4f0b908f008fe1e2bddb"      #账单的业务id
    }

    url = read.url_post() + 'getBillInfo'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getBillInfo_get()



