# -*- coding: UTF-8 -*-
import requests
from config.base_config import BASE_URL,STR_REQUEST,STR_RESPONSE
from tools import log_tool,random_tool


# 增加商品
def test__product_addProd(d):
    brand = random_tool.random_numbers()
    colors = random_tool.random_color()
    json = {
        "brand": "huawei"+brand,
        "colors": colors,
        "price": 0,
        "productCode": "string",
        "productName": "string",
        "sizes": ["string"],
        "type": "string"
}
    token = {"token":d["token"]}
    r = requests.request("POST",BASE_URL + "/product/addProd",json = json,headers = token)
    print(r.request.body)
    log_tool.info("-------------------增加商品test__product_addProd(请求)-------------------"
                  + STR_REQUEST.format(r.request.method, r.request.url, r.request.headers, r.request.body))
    log_tool.info("-------------------增加商品test__product_addProd(响应)-------------------"
                  + STR_RESPONSE.format(r.status_code, r.headers, r.text))
    print(r.text)
    try:
        assert "2000" in r.text
    except:
        log_tool.error(r.text)