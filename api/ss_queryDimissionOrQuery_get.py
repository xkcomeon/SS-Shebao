#coding=utf8

import requests
from read import url_post
from read import header

#获取首页离职未停保员工
def ss_queryDimissionOrQuery_get():
    body = {
        "page": 1,
        "pageSize": 10
    }

    url = url_post() + 'queryDimissionOrQuery'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_queryDimissionOrQuery_get()