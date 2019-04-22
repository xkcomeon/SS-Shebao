#coding:utf-8

import requests
import read


#获取员工基本信息和公积金社保缴纳状态----待定
def ss_getUserInsuerdInfo_get():   #m_u_GetUserInsuredInfo (Mobile 端  无入参)
    body = {
        "userId":read.userId()
    }

    url = read.url_post() + 'getUserInsuerdInfo'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_getUserInsuerdInfo_get()



