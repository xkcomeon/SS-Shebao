#coding:utf-8

import requests
import read


#获取账单管理列表
def ss_getBillInfos_get():
    body = {
        "year": "2018",     #首次访问账单页默认为当前年度
        "ssOrgId": "8888"   #首次访问账单页默认查询全部公司
    }

    url = read.url_post() + 'getBillInfos'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_getBillInfos_get()



