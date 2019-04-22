#coding:utf-8

import requests
import read


#批量获取用户ID （全选）
def ss_getAllBatchUserIds_get():
    body = {
        "ssStatus": "1",
        "ssStatus": "6",
        "ssStatus": "8",
        "ssStatus": "9",
        "ssStatus": "99",
        "hfStatus": "1",
        "hfStatus": "6",
        "hfStatus": "8",
        "hfStatus": "9",
        "hfStatus": "99",
        "orQueryBool": "true"
    }

    url = read.url_post() + 'getAllBatchUserIds'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getAllBatchUserIds_get()



