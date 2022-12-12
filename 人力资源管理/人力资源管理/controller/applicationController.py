# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.applicationDao import *
#导入math
import math


def applicationAddRequest(request):
    # 获取用户名
    # 是前端定义的键名
    name = request.GET.get("name")
    birth = request.GET.get("birth")
    sex = request.GET.get("sex")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    time = request.GET.get("time")

    # 打印姓名和年龄
    #print("name=", name)
   # print("age=", age)
    # 调用add方法，并获取返回值
    rs = add(name,sex,birth,phone,email,time)
    # 创建字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "新增成功"
    else:
        info["info"] = "新增失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的新增列表请求函数

def applicationListRequest(request):
    # 获取页码
    page = int(request.GET.get("page"))
    # 显示每页条数
    row = int(request.GET.get("row"))
    # 每一页查询的index的值
    index = row * (page - 1)
    name = request.GET.get("name")
    # 查询结果，得到返回结果
    rs = select(index,row,name)
    # 查询总条数
    c = selectCount(name)
    #计算总页数
    totalPage = math.ceil(c/row)
    # 创建一个空列表
    list = []
    for x in rs:
        # 创建一个字典
        dc = {"id": x[0], "name": x[1], "sex": x[2], "birth": x[3], "phone": x[4], "email": x[5], "time": x[6]}
        # 添加到空列表中
        list.append(dc)
    # 定义一个字典
    info = {"list": list, "total": c, "totalPage": totalPage}
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的查询老师列表的请求的函数

def applicationUpdateRequest(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    sex = request.GET.get("sex")
    birth = request.GET.get("birth")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    time = request.GET.get("time")
    rs = update(name,sex,birth,phone,email,time,id)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 修改老师传给前端数据


# 删除
def applicationDelRequest(request):
    # 获取要删除的id
    id = request.GET.get("id")
    # 调用删除的方法
    rs = delete(id)
    # 定义字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "删除成功"
    else:
        info["info"] = "删除失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 删除老师表传给前端数据

