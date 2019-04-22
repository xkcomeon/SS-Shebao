#coding:utf-8

import requests
import read


#批量停保--确定停保
def ss_batchStopInsured_post():
    body = {
        "userId":"205703250039944248",
        "userName":"龙十一",
        "leavingDay":"null",
        "text":"",
        "ssInsureId":"null",
        "hfInsureId":"7fe985449cc843e0afa1f249dd1d0d6c",
        "ssStartDate":"null",
        "hfStartDate":"2018-11",
        "isStopSS":"false",
        "isStopHF":"true"
    }

    url = read.url_post() + 'batchStopInsured'
    r = requests.post(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_batchStopInsured_post()



