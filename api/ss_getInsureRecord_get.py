#coding:utf-8

import requests
import read


#获取投保记录
def ss_getInsureRecord_get():
    body = {
        "userId":read.userId(),
        "page": 1,
        "pageSize": 10
    }

    url = read.url_post() + 'getInsureRecord'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getInsureRecord_get()



