#coding=utf8

import json
import requests
from read import url_post
from read import header

#获取首页参保人员记录
def ss_queryHPChangeByMonth_grt():
    body = {

    }

    url =url_post() + 'queryHPChangeByMonth'
    r = requests.get(url,headers=header())

    #各个参保记录人数统计结果
    SS_INCREASE = json.loads(r.text).get('result')[0]['value']
    HF_INCREASE = json.loads(r.text).get('result')[1]['value']
    SS_REDUCE = json.loads(r.text).get('result')[2]['value']
    HF_REDUCE = json.loads(r.text).get('result')[3]['value']
    SS_INSURING = json.loads(r.text).get('result')[4]['value']
    HF_INSURING = json.loads(r.text).get('result')[5]['value']

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_queryHPChangeByMonth_grt()