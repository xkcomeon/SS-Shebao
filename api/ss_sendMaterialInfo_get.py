#coding:utf-8

import requests
import read


#邀请员工完善材料
def ss_sendMaterialInfo_get():
    body = {
        "userId":read.userId()
    }

    url = read.url_post() + 'sendMaterialInfo'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_sendMaterialInfo_get()



