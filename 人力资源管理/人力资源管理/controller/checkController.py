# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.checkDao import *
from 人力资源管理.dao.payDao import money1
#导入math
import math


def checkAddRequest(request):
    # 获取用户名
    # 是前端定义的键名
    staff_id = request.GET.get("staff_id")
    base_pay = request.GET.get("base_pay")
    merit_pay = request.GET.get("merit_pay")
    bonus = request.GET.get("bonus")
    fine = request.GET.get("fine")
    total = request.GET.get("total")
    get_time = request.GET.get("get_time")

    # 打印姓名和年龄
    #print("name=", name)
   # print("age=", age)
    # 调用add方法，并获取返回值
    rs = add(staff_id,base_pay,merit_pay,bonus,fine,total,get_time)
    # 创建字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "新增成功"
    else:
        info["info"] = "新增失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的新增列表请求函数

def checkListRequest(request):
    # 获取页码
    page = int(request.GET.get("page"))
    # 显示每页条数
    row = int(request.GET.get("row"))
    # 每一页查询的index的值
    index = row * (page - 1)
    name = request.GET.get("name")
    print(name)
    print(type(name))
    # 查询结果，得到返回结果
    rs = select(name,index,row)
    # 查询总条数
    c = selectCount(name)
    #计算总页数
    totalPage = math.ceil(c/row)
    #money(index,row)
    list = []
    for x in rs:
        dc = {"pay_id": x[0], "staff_id": x[1], "base_pay": x[2], "merit_pay": x[3], "bonus": x[4], "fine": x[5], "total": x[6], "get_time": x[7]}
        # 添加到空列表中
        list.append(dc)
    # 定义一个字典
    info = {"list": list, "total": c, "totalPage": totalPage}
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的查询老师列表的请求的函数

def checkUpdateRequest(request):
    pay_id = request.GET.get("pay_id")
    #staff_id = request.GET.get("staff_id")
    base_pay = request.GET.get("base_pay")
    merit_pay = request.GET.get("merit_pay")
    bonus = request.GET.get("bonus")
    fine = request.GET.get("fine")
    total = request.GET.get("total")
    get_time = request.GET.get("get_time")
    rs = update(pay_id,base_pay,merit_pay,bonus,fine,total,get_time)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 修改老师传给前端数据


# 删除
def checkDelRequest(request):
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
