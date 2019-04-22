#coding:utf-8

import requests
import read


#获取停保最后缴纳月和停保原因列表
def ss_stopInsured_post():
    body = {
        "userId":"20570642121286535",
        "userName":"龙一",
        "position":"上单",
        "workPlace":"上路",
        "leavingDay":"2018-11-23",
        "ssInfo":{
            "id":"39edd1abb8684655ae62d125001f5e7b",
            "message":{
                "code":1
            },
            "startDate":"2019-05"
        },
        "hfInfo":{
            "id":"2c0c9e60f86041b4ac602ef78ed1a885",
            "startDate":"2019-08"
        }
    }

    url = read.url_post() + 'stopInsured'
    r = requests.post(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_stopInsured_post()



