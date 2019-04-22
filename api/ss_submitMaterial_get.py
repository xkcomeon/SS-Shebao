#coding:utf-8

import requests
import read


#提交线上材料--手机端
def ss_submitMaterial_get():
    body = {
        "userId":read.userId()
    }

    url = read.url_post() + 'submitMaterial'
    r = requests.get(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_submitMaterial_get()



