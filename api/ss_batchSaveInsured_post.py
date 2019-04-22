 #coding:utf-8

import requests
import read


#批量投保--确定投保
def ss_batchSaveInsured_post():
    body = [
    {
         "userName":"小杨",
        "userId":"2305574867757049",
        "hfBaseNum":"2300",
        "hfCityCode":"310100",
        "hfFirstInsuredType":2,
        "hfIsOff":"false",
        "hfSchemeId":"f94d8548898411e8a13252540080f839",
        "hfStartDate":"2019-04",
        "hfSupplementPayMonths":"",
        "ssBaseNum":"1000",
        "ssCityCode":"310100",
        "ssFirstInsuredType":2,
        "ssIsOff":"false",
        "ssSchemeId":"f767f5f94f48419998294823ede91a81",
        "ssStartDate":"2019-04",
        "ssSupplementPayMonths":"",
        "ssInvoiceId":"invoice3575c53acb4845d6925827afde15ba22",
        "hfInvoiceId":"invoice3575c53acb4845d6925827afde15ba22",
        "ssSSOrgId":"daku88888",
        "hfSSOrgId":"daku88888"
    }
]
    url = read.url_post() + 'batchSaveInsured'
    r = requests.post(url,json=body,headers=read.header())

    #检测返回值
    print(r.text)
    #检测返回状态
    print(r.status_code)


if __name__ == '__main__':
    ss_batchSaveInsured_post()



