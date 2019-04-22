# coding=utf8
import json
import random
import time
import datetime
import requests

# 环境变量
contentType = "application/json;charset=UTF-8"
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

# test环境
base_url = "https://test-ss.renlijia.com/rest/api/v1.0/"
cookie1 = "N2=D91722EBEA22719423D423D1BFBA008326346B5E35C3F4B35B713A060341BD743927E2FB5064D40435B1BE43B1FD4C85995F42A61B4B65CBC038019AF8966D847183DFFF7355553ED10F9DB5B2F80D99281CF9183315D16BCAAC6EE43D850B3928128F0C6F5257455B6981D9DB4BD13B313D18680CADB9E594B1030E5445EED18614B7D8DA127DF41F5DBA8342AB7ABF2E21E7798A962C67D129E10533FB56CA520584E75FB5871C95993C9AC7E2046D39BF35659942E7E881773DA3F80A597967B9D34ABB519E6245ECFA7734A6E4BFAC38FEA057ACD172D7C3DDC31C39ED9BA54BDF0BD6F6429E0FAF39833373DC414D3134DF548EFDE43BC2BE134B53B17AD864FC9974892A65B86E2A010AEDC066981FB96656EAED89EE3EAA59FEBC87C163F07610BF7EAD89C0A6F1449AADA7ECD4B00824921CC68023A63BF9C790A32D52FEC8C71D838760BF7A44B9FD9C54BFA0B0C8C1E6DAE7425EFECD4F6A375EF7AAC9A723099BC9BF; N1=694a1cc6fcb39de84; N3=FC92F66C80E14C9B7730B9B5E17A858BE22F312277C50C67160756B03EBC3DB0C9ACB2928F2E5DE7F56D66A641E74C185F8223015EAA13FD80D150683547DDD4528357B8FC0CC0F41639E3281C81CB128F30E408DAE3B86D78C3BEDF3A6C976E20C649FDA0DAD29B"
cookie2 = "_X_CSRF_TOKEN=ed41e8b17e7d4439b3a28c8ecd15719a; N2=027F06055F0A2C03BDF6F385E8FDECAED1B48AB02C2ABFA77E230A7B7AFBF08414274FD3DC2B416CB73BCAB082B1FD32995F42A61B4B65CB33ACC13268E348FD45CDF86BF06AB417EF90399B366093340867DA7707DFD8FA69CF061CC8E3596C14D5EA254B1EAD14F0B80AD3DF866CB3A543ED4E1EF11A1F2664DB2EAFF625679F0320419606D0B2CAAC6EE43D850B3928128F0C6F525745E49FB0552FDBA5DF0DFF9CC185C35ECE2019150C137CA6BE0E47BC4A24EC258A99543C0DC79E2CF631E655B2E9DAE571F278FD768226CEDFEA27DF04B23CC8762A9B4D2D571EE40A13E508F8EC8087A1794C98FC1373406B501D6E6C18D2F488D066C634CB9E1331D8B778F7200C35E387B62362AB0787C8D137D7FBF46EE27F10A4692FFA620D914325AD91757CD52DC5354BC14B24A219FEA830A218396DDC551EA37D68A94455; N1=88e2a50a61144b989"
token = "1ad28ae99bbc4953b3af876f8ab36d44"
TOKEN = "ed41e8b17e7d4439b3a28c8ecd15719a"
schemeId1 = "f94d8548898411e8a13252540080f827"  #北京社保城镇标准
#"f94d8548898411e8a13252540080f838" #(预发)上海社保唯一标准
schemeId2 = "f94d8548898411e8a13252540080f829"
#"f94d8548898411e8a13252540080f839"  #(预发)上海公积金7+7


def header():
    header = {
        "Cookie": cookie1,
        "Token": token
    }
    return header

# print(header())

# 获取当前日期函数
def timeToday():
    timeToday = time.strftime('%Y-%m-%d', time.localtime())
    return timeToday
def timeYear():
    timeYear = time.strftime('%Y',time.localtime())
    return timeYear


# print(timeToday())

'''
#获取这个月后三个月的时间
import arrow
def timeMonth():
    a = arrow.now()
    timeMonth = a.shift(months=+3).format("YYYY-MM")
    return timeMonth
print(timeMonth())
'''


# 接口请求后sleep时间
def teardown_hook_sleep_N_secs(response, n_secs):
    if response.status_code == 200:
        time.sleep(n_secs)
    else:
        time.sleep(10)


# 首页待办事项人数校验
def queryHPNotice_get():
    url = base_url + "queryHPNotice"

    r = requests.get(url, headers=header())
    # print(r.text)
    # print(r.status_code)

    ON_WORK = json.loads(r.text).get('result')[0]['value']
    PRE_DIMISSION = json.loads(r.text).get('result')[1]['value']
    DIMISSION = json.loads(r.text).get('result')[2]['value']
    WAIT = json.loads(r.text).get('result')[3]['value']

    return ON_WORK, PRE_DIMISSION, DIMISSION, WAIT


# 投保后首页在职未投保人数
a = queryHPNotice_get()[0] - 1
# 取消投保后首页在职未投保人数
b = queryHPNotice_get()[0]
# 投保后首页投保待处理
c = queryHPNotice_get()[3] + 1


# 首页参保人员记录校验
def queryHPChangeByMonth_get():
    url = base_url + "queryHPChangeByMonth"
    # print(url)
    r = requests.get(url, headers=header())

    # print(r.text)
    # print(r.status_code)

    SS_INCREASE = json.loads(r.text).get('result')[0]['value']
    HF_INCREASE = json.loads(r.text).get('result')[1]['value']
    SS_REDUCE = json.loads(r.text).get('result')[2]['value']
    HF_REDUCE = json.loads(r.text).get('result')[3]['value']
    SS_INSURING = json.loads(r.text).get('result')[4]['value']
    HF_INSURING = json.loads(r.text).get('result')[5]['value']

    return SS_INCREASE, HF_INCREASE, SS_REDUCE, HF_REDUCE, SS_INSURING, HF_INSURING
print(queryHPChangeByMonth_get())


# if __name__ == '__main__':
#     queryHPChangeByMonth_get()

# 投保后社保正常在缴人数
d = queryHPChangeByMonth_get()[4] + 1
# 投保后公积金正常在缴人数
e = queryHPChangeByMonth_get()[5] + 1


# print(a, b, c, d, e)


def BillCount():
    url = base_url + "getBillInfos"
    body = {
        "year": timeYear()
    }
    r = requests.get(url, json=body, headers=header())

    #result.billList下的集合
    d =  json.loads(r.text).get('result')['billList']
    e = len(d)
    # print(e)
    h = e - 1
    #result.billList.e.billInfo下的集合
    d1 =  json.loads(r.text).get('result')['billList'][h]['billInfo']
    e1 = len(d1)
    # print(e1)

    i = 0
    Amount =0

    for item in d:
        count = json.loads(r.text).get('result')['billList'][h]['billInfo'][i]['totalAmount']
        Amount = Amount + count
        i+=1

        if i == len(d1):
            return Amount
if __name__ == '__main__':
    BillCount()