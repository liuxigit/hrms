# 导入django
from django.shortcuts import HttpResponse
from 人力资源管理.dao.adminDao import *
import json
import math


# 登陆请求
def admin_loginRequest(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    rs = login(username, password)
    info = {"info": ""}
    if rs == True:
        info["info"] = "登录成功"
    else:
        info["info"] = "用户名或密码错误"
    return HttpResponse(json.dumps(info), content_type="application/json")