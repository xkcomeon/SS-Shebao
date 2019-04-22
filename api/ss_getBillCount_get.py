#coding=utf8

import requests
from read import url_post
from read import header

#获取首页账单成本分析
def ss_getBillCount_get():
    body = {

    }

    url = url_post() + 'getBillCount'
    r = requests.get(url,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getBillCount_get()