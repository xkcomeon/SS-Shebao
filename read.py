#coding:utf-8

#接口IP地址
def url_post():
    #url = "http://dev-ss.renlijia.com/rest/api/v2.0/"  #钉钉日常社保服务器地址

    url = "https://test-ss.renlijia.com/rest/api/v1.0/"  #钉钉测试社保服务器地址

    #url = "https://pre-ss.renlijia.com/rest/api/v2.0/"  #钉钉预发社保服务器地址

    #url = "https://ss.renlijia.com/rest/api/v2.0/"  #钉钉线上社保服务器地址

    return url


    #测试cookie
def Cookie():
    Cookie = "N3=FC92F66C80E14C9B7730B9B5E17A858BE22F312277C50C67160756B03EBC3DB0C9ACB2928F2E5DE7F56D66A641E74C185F8223015EAA13FD80D150683547DDD4528357B8FC0CC0F41639E3281C81CB128F30E408DAE3B86D78C3BEDF3A6C976E20C649FDA0DAD29B; N2=D91722EBEA22719423D423D1BFBA008326346B5E35C3F4B35B713A060341BD743927E2FB5064D40435B1BE43B1FD4C85995F42A61B4B65CBC038019AF8966D847183DFFF7355553ED10F9DB5B2F80D99281CF9183315D16BCAAC6EE43D850B3928128F0C6F5257455B6981D9DB4BD13B313D18680CADB9E594B1030E5445EED18614B7D8DA127DF41F5DBA8342AB7ABF2E21E7798A962C67D129E10533FB56CA520584E75FB5871C95993C9AC7E2046D39BF35659942E7E881773DA3F80A597967B9D34ABB519E6245ECFA7734A6E4BFAC38FEA057ACD172D7C3DDC31C39ED9BA54BDF0BD6F6429E0FAF39833373DC414D3134DF548EFDE43BC2BE134B53B17AD864FC9974892A65B86E2A010AEDC066981FB96656EAED89EE3EAA59FEBC87C163F07610BF7EAD89C0A6F1449AADA7ECD4B00824921CC68023A63BF9C790A32D52FEC8C71D838760BF7A44B9FD9C54BFA0B0C8C1E6DAE7425EFECD4F6A375EF7AAC9A723099BC9BF; N1=694a1cc6fcb39de84"
    return Cookie

    #测试Token
def Token():
    Token = "0f7b832d3d944a3fafa8497d46bcafa7"
    return Token

def header():
    header = {
        "Cookie": Cookie(),
        "x-csrf-token": Token()
    }
    return header
# print(header())


def cityCode():
    cityCode = 310100
    return cityCode

def userId():
    userId = 15477162885871504      #贺强
    return userId

def ssOrgId():
    ssOrgId = 'daku88888'     #大库ID--元宝汤包
    return ssOrgId

def ss_schemeId():
    ss_schemeId = "f94d8548898411e8a13252540080f838"    #上海社保唯一标准
    return ss_schemeId

def hf_schemeId():
    hf_schemeId = "f94d8548898411e8a13252540080f839"    #上海公积金7+7
    return hf_schemeId

def insuerdInfoId():
    insuerdInfoId = "a82b44beb3c945fbaea69e0d4ceb2158"
    return insuerdInfoId

def declarationId():
    declarationId = "fe54432b878c478a9128b0a917568e5c"
    return declarationId