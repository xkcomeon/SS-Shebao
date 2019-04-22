#coding=utf8

import json
import requests
from read import url_post
from read import header

#获取当前用户状态（需不需要新手引导）
def ss_getRookieLeadStatus_get():
    body = {
        "type":1    #type：1/2
    }

    url = url_post() + 'getRookieLeadStatus'
    r = requests.get(url,json=body,headers=header())

    status = json.loads(r.text).get('result')

    #检测返回状态  true：新手引导  false：不需要新手引导
    print(status)
    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getRookieLeadStatus_get()