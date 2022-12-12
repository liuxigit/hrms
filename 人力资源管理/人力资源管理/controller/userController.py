# 导入django
from django.shortcuts import HttpResponse
from 人力资源管理.dao.UserDao import *
import json
import math


# 登陆请求
def loginRequest(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    rs = login(username, password)
    info = {"info": ""}
    if rs == True:
        info["info"] = "登录成功"
        set_user_state("在线", username)
    else:
        info["info"] = "用户名或密码错误"
    return HttpResponse(json.dumps(info), content_type="application/json")


# 修改密码时自动填入邮箱的请求
def autoEmailRequest(request):
    username = request.GET.get("username")
    rs = autoemail(username)
    info = {"info": ""}
    info["info"] = rs
    return HttpResponse(json.dumps(info), content_type="application/json")


def registRequest(request):
    name = request.GET.get("name")
    print(name)

    pwd = request.GET.get("pwd")

    user_email = request.GET.get("user_email")

    rs = selectUser(name, pwd, user_email)
    info = {"info": ""}
    if rs == True:
        info["info"] = "用户已存在"
    if rs == "该邮箱已绑定账号":
        info["info"] = "该邮箱已绑定账号"
    if rs == False:
        rs2 = regist(name, pwd, user_email)
        if (rs2 == True):
            info["info"] = "注册成功"
        else:
            info["info"] = "注册失败"
    return HttpResponse(json.dumps(info), content_type="application/json")


# 重置密码请求
def changePwdRequest(request):
    newPwd = request.GET.get("newPwd")
    username = request.GET.get("username")
    rs = change_pwd(newPwd, username)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"

    return HttpResponse(json.dumps(info), content_type="application/json")


# 忘记密码的重置密码请求
def rePwdRequest(request):
    newPwd = request.GET.get("newPwd")
    email_2 = request.GET.get("email_2")
    rs = change_pwd2(newPwd, email_2)
    info = {"info": ""}
    if rs == True:
        info["info"] = "重置成功"
    else:
        info["info"] = "重置失败"

    return HttpResponse(json.dumps(info), content_type="application/json")



# 退出时将状态改为离线
def exitStateRequest(request):
    username = request.GET.get("username")
    rs = set_user_state("离线", username)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改状态成功"
    else:
        info["info"] = "修改状态失败"
    return HttpResponse(json.dumps(info), content_type="application/json")