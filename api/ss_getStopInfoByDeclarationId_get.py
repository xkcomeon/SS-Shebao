#coding:utf-8

import requests
import read


#获取停保最后缴纳月和停保原因列表
def ss_getStopInfoByDeclarationId_get():
    body = {
        "declarationId":read.declarationId()
    }

    url = read.url_post() + 'getStopInfoByDeclarationId'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getStopInfoByDeclarationId_get()



