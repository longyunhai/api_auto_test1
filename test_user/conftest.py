import pytest
import requests
from tools import log_tool,os_tool
from config.base_config import BASE_URL,STR_REQUEST,STR_RESPONSE

@pytest.fixture(scope="module")
def d():
    # 用户登录
    json = {
        "pwd": "VzuT98XI",
        "userName": "pafef09020"
    }
    r = requests.request("POST",BASE_URL + "/login", json=json)
    token = r.json()["data"]["token"]
    log_tool.info("-------------------用户登录(请求)-------------------"
                  + STR_REQUEST.format(r.request.method, r.request.url, r.request.headers, r.request.body))
    log_tool.info("-------------------用户登录(响应)-------------------"
                  + STR_RESPONSE.format(r.status_code, r.headers, r.text))
    try:
        assert "2000" in r.text
    except:
        log_tool.error(r.text)
    print(r.text)
    return {"pwd": "VzuT98XI", "name": "pafef09020", "token": token}
