#coding:utf-8

import requests
import read


#编辑材料上传图片
def ss_upload_post():
    body = {
        "file": "(binary)"
    }

    url = read.url_post() + 'upload'
    r = requests.post(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)

if __name__ == '__main__':
    ss_upload_post()



