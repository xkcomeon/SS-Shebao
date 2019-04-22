#coding:utf-8

import requests
from read import url_post
from read import header
import Dingshebao_Read


#保存员工基本信息
def ss_saveBaseInfo_post():
    body = {
    "userId":read.userId(),
    "realName":"小猪猪",
    "mobile":"15114878782",
    "idCard":"610526199909097331"
}

    url = url_post() + 'saveBaseInfo'
    r = requests.post(url,json=body,headers=header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)
    print(read.userId())

if __name__ == '__main__':
    ss_saveBaseInfo_post()



