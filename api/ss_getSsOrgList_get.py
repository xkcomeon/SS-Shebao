#coding:utf-8

import requests
import read


#获取年度和账户列表
def ss_getSsOrgList_get():
    body = {

    }

    url = read.url_post() + 'getSsOrgList'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getSsOrgList_get()



