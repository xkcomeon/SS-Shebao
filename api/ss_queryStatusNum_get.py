#coding=utf8

import json
import requests
from read import url_post
from read import header

#获取各个状态的员工数量
def ss_queryStatusNum_get():
    body = {

    }

    url = url_post() + 'queryStatusNum'
    r = requests.get(url,headers=header())

    #返回的各个员工状态数量
    ON_WORK = json.loads(r.text).get('result')[0]['value']
    UPLOAD_MATERIAL = json.loads(r.text).get('result')[1]['value']
    MATERIAL_ERROR = json.loads(r.text).get('result')[2]['value']
    INSURED_ERROR = json.loads(r.text).get('result')[3]['value']
    DIMISSION_WORK = json.loads(r.text).get('result')[4]['value']

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_queryStatusNum_get()