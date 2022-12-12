# 导入django的包
from django.shortcuts import HttpResponse
# 导入teacherDao文件
from 人力资源管理.dao.admin_to_userDao import *
# 导入json
import json
# 导入math
import math


# 创建一个接受前端发送的函数
def addRequest(request):
    # 获取用户名
    # name 是前段定义的键名
    name = request.GET.get("name")
    # 获取职称
    pwd = request.GET.get("pwd")
    # 获取邮箱
    user_email = request.GET.get("user_email")
    # 打印姓名和年龄
    print("name=", name)
    print("pwd=", pwd)
    print("user_email=", user_email)
    # 验证用户名是否重名
    length = len(name)
    rs = valiDateName(name)
    # 创建字典
    info = {"info": ""}
    if rs == True:
        info["info"] = "用户名重名"
    elif length < 4 or length > 6:
        info["info"] = "用户名长度必须在4-6之间"
    else:
        # 调用add方法，并且获取返回值
        ps = add(name, pwd, user_email)
        if ps == True:
            info["info"] = "新增成功"
        else:
            info["info"] = "新增失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的查询学生列表的请求
def userListRequest(request):
    # 获取页码
    page = int(request.GET.get("page"))
    # 每页要显示的条数
    row = int(request.GET.get("row"))
    # 获取要查询的姓名
    position = request.GET.get("position")
    # 计算分页查询的值
    index = row * (page - 1)
    # 查询结果，得到返回结果
    rs = select(index, row, position)
    print(rs)
    # 查询总条数
    c = selectCount(position)
    # 计算总页数
    totalPage = math.ceil(c / row)
    # 创建一个空列表
    list = []
    for x in rs:
        # 创建一个字典
        dc = {"id": x[0], "name": x[1], "pwd": x[2], "user_email": x[3], "state": x[4]}
        # 添加到列表中
        list.append(dc)
        # 定义一个字典
    info = {"list": list, "total": c, "totalPage": totalPage}
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")

    # 修改


def userUpdateRequest(request):

    # 获取编号
    id = request.GET.get("id")
    # 获取姓名
    name = request.GET.get("name")

    # 获取职称
    pwd = request.GET.get("pwd")
    # 获取年龄
    user_email = request.GET.get("user_email")

    print(id,name,pwd,user_email)
    # 访问修改方法，获取返回值
    rs = update(id,name, pwd, user_email)

    # 创建字典
    info = {"info": ""}
    if rs:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")


# 删除
def userDelRequest(request):
    # 获取要删除的id
    id = request.GET.get("id")
    # 调用删除的方法
    rs = delete(id)
    # 创建字典
    info = {"info": ""}
    if rs:
        info["info"] = "删除成功"
    else:
        info["info"] = "删除失败"
    # 定义返回给前端的数据
    return HttpResponse(json.dumps(info), content_type="application/json")
