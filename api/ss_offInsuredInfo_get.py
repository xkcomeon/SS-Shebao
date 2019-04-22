#coding:utf-8

import requests
import read


#取消投保、停保
def ss_offInsuredInfo_get():
    body = {
        "insuerdInfoId":read.insuerdInfoId()
    }

    url = read.url_post() + 'offInsuredInfo'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_offInsuredInfo_get()



