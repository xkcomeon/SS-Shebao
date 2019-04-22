#coding=utf8

import requests
from read import url_post
from read import header

#获取子管理员列表
def ss_getDSubAdmins_get():
    body = {

    }

    url = url_post() + 'getDSubAdmins'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getDSubAdmins_get()