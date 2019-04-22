#coding=utf8
import json
import requests
from read import url_post
from read import header

#首页待办事项
def ss_queryHPNotice_get():
    body ={

    }

    url = url_post() + 'queryHPNotice'
    r = requests.get(url,headers=header())

    #各个状态具体的员工数
    ON_WORK = json.loads(r.text).get('result')[0]['value']
    PRE_DIMISSION = json.loads(r.text).get('result')[1]['value']
    DIMISSION = json.loads(r.text).get('result')[2]['value']
    WAIT = json.loads(r.text).get('result')[3]['value']
    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_queryHPNotice_get()