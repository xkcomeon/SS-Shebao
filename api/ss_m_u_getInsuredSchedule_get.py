#coding:utf-8

import requests
import read


#获取参保进度--手机端
def ss_m_u_getInsuredSchedule_get():
    body = {
        "type":1    #1社保  2 公积金
    }

    url = read.url_post() + 'm_u_getInsuredSchedule'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_m_u_getInsuredSchedule_get()



