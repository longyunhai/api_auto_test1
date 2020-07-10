import random
import re
import requests
import json
from tools import random_tool,log_tool,os_tool
from config.base_config import BASE_URL,STR_REQUEST,STR_RESPONSE
import pytest


# 随机生成手机号码和名字
class random_pn():

    def phone(self):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

    def name(self):
        xing='abcdefjhijklmnopqrst'
        ming='01234567879'
        X="".join(random.choice(xing) for i in range(5))
        M="".join(random.choice(ming) for i in range(5))
        return X+M






# 用户注册
# def test_signup_t(d):
#     d["phone"] = random_pn().phone()
#     d["name"] = random_pn().name()
#     d["pwd"] = random_tool.random_pwd()
#     json = {
#           "phone": d["phone"],
#           "pwd": d["pwd"],
#           "rePwd": d["pwd"],
#           "userName": d["name"]
#     }
#     r = requests.request("POST",BASE_URL + "/signup",json = json)
#     log_tool.info("-------------------用户注册test_signup_t(请求)-------------------"
#                   +STR_REQUEST.format(r.request.method, r.request.url, r.request.headers, r.request.body))
#     log_tool.info("-------------------用户注册test_signup_t(请求)-------------------"
#                   +STR_RESPONSE.format(r.status_code, r.headers, r.text))
#     print(r.text)
#     try:
#         assert "2000" in r.text
#     except:
#         log_tool.error(r.text)




# 修改密码
def test_changepwd_t(d):
    json = {
          "newPwd": d["pwd"],
          "oldPwd": d["pwd"],
          "reNewPwd": d["pwd"],
          "userName": d["name"]
}
    token = {"token":d["token"]}
    r = requests.request("POST",BASE_URL + "/user/changepwd",json = json,headers = token)
    log_tool.info("-------------------修改密码test_changepwd_t(请求)-------------------"
                  +STR_REQUEST.format(r.request.method,r.request.url,r.request.headers,r.request.body))
    log_tool.info("-------------------修改密码test_changepwd_t(响应)-------------------"
                  +STR_RESPONSE.format(r.status_code,r.headers,r.text))
    print(r.text)
    try:
        assert "2000" in r.text
    except:
        log_tool.error(r.text)
# 冻结用户
def test_lock_t(d):
    data = {
        "userName":d["name"]
    }
    token = {"token": d["token"]}
    r = requests.request("POST", BASE_URL + "/user/lock",data = data,headers=token)
    log_tool.info("-------------------冻结用户test_lock_t(请求)-------------------"
                  +STR_REQUEST.format(r.request.method, r.request.url, r.request.headers, r.request.body))
    log_tool.info("-------------------冻结用户test_lock_t(响应)-------------------"
                  +STR_RESPONSE.format(r.status_code, r.headers, r.text))
    print(r.text)
    try:
        assert "2000" in r.text
    except:
        log_tool.error(r.text)
# 解冻
def test_unLock_t(d):
    data = {
        "userName":d["name"]
    }
    token = {"token": d["token"]}
    r = requests.request("POST", BASE_URL + "/user/unLock",data = data,headers=token)
    log_tool.info("-------------------解冻用户test_unLock_t(请求)-------------------"
                  +STR_REQUEST.format(r.request.method, r.request.url, r.request.headers, r.request.body))
    log_tool.info("-------------------解冻用户test_unLock_t(响应)-------------------"
                  +STR_RESPONSE.format(r.status_code, r.headers, r.text))
    print(r.text)
    try:
        assert "2000" in r.text
    except:
        log_tool.error(r.text)

