#coding:utf-8

import requests
import read


#获取参保日志
def ss_getSsOpFlowLogs_get():
    body = {
        "userId":read.userId(),
        "flag":"true"   #true:查所有  false:查最新3条
    }

    url = read.url_post() + 'getSsOpFlowLogs'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getSsOpFlowLogs_get()



