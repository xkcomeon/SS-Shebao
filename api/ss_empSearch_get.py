#coding=utf8

import requests
from read import url_post
from read import header

#搜索接口
def ss_empSearch_get():
    body = {
        "deptId": -1,    #中单-部门Id
		"type": 3,	#1只查部门 2只查在职人员 3查部门和在职人员 0查离职人员
		"page": 1,
		"size": 30,
		"key": ''
    }

    url = url_post() + 'empSearch'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_empSearch_get()