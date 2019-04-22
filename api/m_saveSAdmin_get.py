#coding=utf8

import requests
from read import url_post
from read import header

#获取当前用户权限--手机端
def ss_m_saveSAdmin_get():
    body = {
        "userId":"$userId"
    }

    url = url_post() + 'm_saveSAdmin'
    r = requests.get(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_m_saveSAdmin_get()