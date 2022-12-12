# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.t_recordDao import *
# 导入math
import math


# 接受前端发送的查询人员档案列表的请求的函数
def trListRequest(request):
    # 获取页码
    page = int(request.GET.get("page"))
    # 显示每页条数
    row = int(request.GET.get("row"))
    # 获取查询姓名
    message = request.GET.get("message")
    # 每一页查询的index的值
    index = row * (page - 1)

    # 查询结果，得到返回结果
    rs = select_tr(index, row, message)
    # 查询总条数
    c = selectCount_tr(message)
    # 计算总页数
    totalPage = math.ceil(c / row)
    # 创建一个空列表
    list = []
    for x in rs:
        # 创建一个字典
        dc = {"record_id": x[0], "staff_id": x[1], "record_name": x[2], "digest": x[3], "remark": x[4]}
        # 添加到空列表中
        list.append(dc)
    # 定义一个字典
    info = {"list": list, "total": c, "totalPage": totalPage}
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 修改人力调动信息
def trUpdateRequest(request):
    record_id = request.GET.get("record_id")
    record_name = request.GET.get("record_name")
    digest = request.GET.get("digest")
    remark = request.GET.get("remark")
    rs = update_tr(record_name, digest, remark,  record_id)
    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 删除
def trDelRequest(request):
    # 获取要删除的id
    record_id = request.GET.get("record_id")
    # 调用删除的方法
    rs = delete_tr(record_id)
    # 定义字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "删除成功"
    else:
        info["info"] = "删除失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 新增
def trAddRequest(request):
    # 获取用户名
    # 是前端定义的姓名等
    record_id = request.GET.get("record_id")
    staff_id = request.GET.get("staff_id")
    record_name = request.GET.get("record_name")
    digest = request.GET.get("digest")
    remark = request.GET.get("remark")
    # 调用selectid方法，并获取返回值
    rs = select_tr_id(staff_id)
    # 调用add函数，获取返回值
    addd = add_tr(staff_id, record_name, digest, remark)
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

#自动判断员工id是否正确
def trAutoIdRequest(request):
    # 获取用户名
    # 是前端定义的员工编号
    staff_id = request.GET.get("staff_id")
    #调用selectid函数得到返回值
    rs = select_tr_id(staff_id)
    # 创建字典
    info = {"info": "", "name": ""}
    if rs == False:
        info["info"] = "请输入正确的员工编号"
    else:
        info["name"] = rs
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")