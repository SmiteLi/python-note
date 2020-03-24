#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import logging
import requests
import xlrd
import json
from bs4 import BeautifulSoup
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# http://93.qiweioa.cn/myApplication/siteDetail?paasid=mongoexpress&siteId=mongoexpress&name=mongoexpress&status=2
RIOHOST = "93.qiweioa.cn"
RIOPROTOCOL = "http"
RIOURL = RIOPROTOCOL + "://" + RIOHOST
RIOACCOUNT = "admin"
RIOPASSWORD = "Do1admin@123"
RIOPASSID = "tifapi"
EXCELPATH = r'D:\work\002-RIO\tif.xlsx'


def read_excel(path):
    excelFile = xlrd.open_workbook(path)
    excelSheet = excelFile.sheet_by_index(0)
    data = []
    if excelSheet.nrows > 0:
        for i in range(excelSheet.nrows):
            print("total=>", i)
            row = []
            for j in range(excelSheet.ncols):
                print(",", j, end="")
                row.append(excelSheet.cell_value(i, j))
            data.append(row)
            print()

    return data


def do_release_api(session):
    headers = {"X-Requested-With": 'XMLHttpRequest',
               "Content-Type": 'application/json'}
    session.headers.update(headers)

    data = read_excel(EXCELPATH)
    for i in range(data.__len__()):
        row = data.__getitem__(i)
        print('row = ', i)
        do_create_api(session, row)


def do_create_api(session, row):
    """
    创建API服务
    """
    saveUrl = RIOURL + "/api/app/service/draft/save"
    publishUrl = RIOURL + "/api/app/service/publish"

    name = row[0]
    svcid = row[1]
    description = row[2]
    pubPath = row[3]
    targetHosts = row[4]
    targetPath = row[5]

    params = {"paasid": RIOPASSID, "svcid": svcid, "name": name, "description": description, "isPublic": True, "router": {"pubPath": pubPath, "targetPath": targetPath, "targetHosts": [targetHosts], "keepSession": False, "requestLimit": 1000, "timeout": 60000, "userAccessible": True, "needLogin": False}, "deployRegion": [
        {"id": "zwww", "name": "政务外网", "protocol": "http", "ignoreCertsError": False, "host": [RIOHOST]}], "pubRegion": [{"id": "zwww", "name": "政务外网", "protocol": RIOPROTOCOL, "ignoreCertsError": False, "host": [RIOHOST]}]}
    createResult = session.post(saveUrl, json=params).json()
    print(createResult)

    publishResult = session.post(publishUrl, json=params).json()
    print(publishResult)
    do_auth_api(session, svcid)


def do_auth_api(session, svcid):
    authUrl = RIOURL + "/api/app/service/approve"
    params = {"svcid": svcid}
    authResult = session.post(authUrl, json=params).json()
    print(authResult)


def get_app_list(session):
    appListUrl = RIOURL + "/api/app/my/list?status=0"
    print(appListUrl)
    appListResult = session.get(appListUrl).json()
    return appListResult


def has_app(applist):
    for i in applist["data"]["apps"]:
        if i["paasid"] == RIOPASSID:
            return True

    return False


def do_create_app(session):
    pass


def do_login(session):
    loginUrl = RIOURL + "/rio/atlas-account/login"

    def get_rio_index_html(session):
        '''
        获取登录页的html
        :param url: https://demo.rio.govcloud.qq.com
        :return: 登录页面的html
        '''
        response = session.get(RIOURL)
        return response.text

    def get_csrf(html):
        '''
        处理登录页面的html
        :param html
        :return: 获取首页的csrftoken
        '''
        soup = BeautifulSoup(html, 'lxml')
        res = soup.find("input", attrs={"name": "_csrf"})
        csrf = res["value"]
        return csrf

    def get_challenge(html):
        '''
        处理登录页面的html
        :param html:
        :return: 获取首页的challenge
        '''
        soup = BeautifulSoup(html, 'lxml')
        res = soup.find("input", attrs={"name": "challenge"})
        challenge = res["value"]
        return challenge

    def get_rsa_pk(html):
        '''
        处理登录页面的html
        :param html:
        :return: 获取首页的rsa_pk
        '''
        soup = BeautifulSoup(html, 'lxml')
        res = soup.find("input", attrs={"id": "rsa_pk"})
        rsa_pk = res["value"]
        return rsa_pk

    def do_encrypt(rsa, unencryptstr):
        '''
        使用rsa算法对用户名和密码加密
        :param rsapk,unencryptstr
        return: 加密后的字符串
        '''
        rsaKey = RSA.importKey(base64.b64decode(rsa).decode())
        cipher = Cipher_pkcs1_v1_5.new(rsaKey)
        encryptedStr = str(base64.b64encode(cipher.encrypt(
            unencryptstr.encode(encoding="utf-8"))), encoding="utf-8")
        return encryptedStr

    html = get_rio_index_html(session)

    csrf = get_csrf(html)
    challenge = get_challenge(html)

    account_name = RIOACCOUNT
    password = RIOPASSWORD
    params = {"_csrf": csrf, "challenge": challenge,
              "account_name": account_name, "password": password}
    session.post(loginUrl, data=params)


if __name__ == "__main__":
    session = requests.session()
    do_login(session)
    appListResult = get_app_list(session)

    if has_app(appListResult):
        do_release_api(session)
    else:
        do_create_app(session)
        do_release_api(session)
