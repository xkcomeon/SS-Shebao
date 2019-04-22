#coding=utf8

import requests
from read import url_post
from read import header

#获取当前用户权限--手机端
def ss_saveSSubAdmin_post():
    body = {
        "userId":"$userId",
        "openAuth":"true"       #ture：设置权限  false：撸掉权限
    }

    url = url_post() + 'saveSSubAdmin'
    r = requests.post(url,json=body,headers=header())

    #获取返回值
    print(r.text)
    #获取返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_saveSSubAdmin_post()