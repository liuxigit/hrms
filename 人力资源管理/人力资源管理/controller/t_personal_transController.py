# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.t_personal_transDao import *
# 导入math
import math


# 接受前端发送的查询人力资源调动列表的请求的函数
def tptListRequest(request):
    # 获取页码
    page = int(request.GET.get("page"))
    # 显示每页条数
    row = int(request.GET.get("row"))
    # 获取查询姓名
    message = request.GET.get("message")
    # 每一页查询的index的值
    index = row * (page - 1)

    # 查询结果，得到返回结果
    rs = select(index, row, message)
    # 查询总条数
    c = selectCount(message)
    # 计算总页数
    totalPage = math.ceil(c / row)
    # 创建一个空列表
    list = []
    for x in rs:
        # 创建一个字典
        dc = {"pertra_id": x[0], "staff_id": x[1], "name": x[2], "last_section": x[3], "next_section": x[4],
              "last_duty": x[5], "next_duty": x[6],
              "trans_time": x[7], "causee": x[8]}
        # 添加到空列表中
        list.append(dc)
    # 定义一个字典
    info = {"list": list, "total": c, "totalPage": totalPage}
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 修改人力调动信息
def tptUpdateRequest(request):
    staff_id = request.GET.get("staff_id")
    last_section = request.GET.get("last_section")
    next_section = request.GET.get("next_section")
    last_duty = request.GET.get("last_duty")
    next_duty = request.GET.get("next_duty")
    trans_time = request.GET.get("trans_time")
    causee = request.GET.get("causee")
    rs = update(last_section, next_section, last_duty, next_duty, trans_time, causee, staff_id)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 删除
def tptDelRequest(request):
    # 获取要删除的id
    pertra_id = request.GET.get("pertra_id")
    # 调用删除的方法
    rs = delete(pertra_id)
    # 定义字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "删除成功"
    else:
        info["info"] = "删除失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 新增
def tptAddRequest(request):
    # 获取用户名
    # 是前端定义的姓名等
    staff_id = request.GET.get("staff_id")
    last_section = request.GET.get("last_section")
    next_section = request.GET.get("next_section")
    last_duty = request.GET.get("last_duty")
    next_duty = request.GET.get("next_duty")
    trans_time = request.GET.get("trans_time")
    causee = request.GET.get("causee")
    # 调用selectid方法，并获取返回值
    rs = selectid(staff_id)
    # 调用add函数，获取返回值
    addd = add(staff_id, last_section, next_section, last_duty, next_duty, trans_time, causee)
    # 创建字典
    info = {"info": "", "name": "", "info2": ""}
    if rs == False:
        info["info"] = "无此员工"
    else:
        info["name"] = rs
        if addd == True:
            info["info2"] = "新增成功"
        else:
            info["info2"] = "新增失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")

# 自动根据填入的员工编号填写员工姓名
def tptAutoNameRequest(request):
    # 获取用户名
    # 是前端定义的员工编号
    staff_id = request.GET.get("staff_id")
    #调用selectid函数得到返回值
    rs = selectid(staff_id)
    # 创建字典
    info = {"info": "", "name": ""}
    if rs == False:
        info["info"] = "请输入正确的员工编号"
    else:
        info["name"] = rs
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")