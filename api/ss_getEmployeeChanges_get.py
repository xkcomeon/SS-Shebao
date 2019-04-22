#coding=utf8

import requests
from read import url_post
from read import header

#参保人员每月变动人员列表
def ss_getEmployeeChanges_get():
    body = {
        "employeeChangeKey": "SS_INSURING~ON_WORK",        #离职员工：SS_INSURING~DIMISSION
        "page": 1,
        "pageSize": 10
    }

    url = url_post() + 'getEmployeeChanges'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getEmployeeChanges_get()