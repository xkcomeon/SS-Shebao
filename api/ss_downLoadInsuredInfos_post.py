#coding:utf-8

import requests
import read


#获取所有导出字段(人力丁社保批量)
def ss_downLoadInsuredInfos_get():
    body = {
        "insuredInfosQuery": {

        },
        "itemKeys": [
            "userName",
            "realName",
            "deptName",
            "position"
        ]
    }

    url = read.url_post() + 'downLoadInsuredInfos'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_downLoadInsuredInfos_get()



