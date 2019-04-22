#coding=utf8

import requests
from read import url_post
from read import header

#获取工作地点
def ss_getWorkplaces_get():
    body = {

    }

    url = url_post() + 'getWorkplaces'
    r = requests.get(url,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getWorkplaces_get()