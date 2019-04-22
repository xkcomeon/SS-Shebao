#coding=utf8

import requests
from read import url_post
from read import header

#部门链接口
def ss_selectDeptChain_get():
    body = {
        "deptId": -1        #deptId:-2(通讯录) deptId:-1（公司名-总部门）
    }

    url = url_post() + 'selectDeptChain'
    r = requests.get(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_selectDeptChain_get()