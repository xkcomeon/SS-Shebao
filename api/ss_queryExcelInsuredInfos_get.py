#coding:utf-8

import requests
import read


#获取可投保数据 (在线excel)
def ss_queryExcelInsuredInfos_get():
    body = {
        "userIds":"15477162885871504"
    }

    url = read.url_post() + 'queryExcelInsuredInfos'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_queryExcelInsuredInfos_get()



