# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.payDao import *
#导入math
import math


def payAddRequest(request):
	# 获取用户名
	# 是前端定义的键名
	staff_id = request.GET.get("staff_id")
	type = request.GET.get("type")
	money = request.GET.get("money")
	check_peo = request.GET.get("check_peo")
	# 打印姓名和年龄
	#print("name=", name)
   # print("age=", age)
	# 调用add方法，并获取返回值
	rs = add(staff_id,type,money,check_peo)

	info = {"info": ""}
	if rs == True:
		print("-----------")
		money1()
		info["info"] = "新增成功"
	else:
		info["info"] = "新增失败"
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的新增列表请求函数

def payListRequest(request):
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
	#money(index,row)
	totalPage = math.ceil(c/row)
	# 创建一个空列表
	list = []
	for x in rs:
		dc = {"id": x[0], "staff_id": x[1],"name": x[2] ,"type": x[3], "money": x[4], "check_peo": x[5]}
		list.append(dc)
	info = {"list": list, "total": c, "totalPage": totalPage}
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的查询老师列表的请求的函数

def payUpdateRequest(request):
	check_id = request.GET.get("check_id")
	staff_id = request.GET.get("staff_id")
	type = request.GET.get("type")
	money = request.GET.get("money")
	check_peo = request.GET.get("check_peo")
	rs = update(staff_id,type,money,check_peo,check_id)
	info = {"info": ""}
	if rs == True:
		money1()
		info["info"] = "修改成功"
	else:
		info["info"] = "修改失败"
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 修改老师传给前端数据


# 删除
def payDelRequest(request):
	# 获取要删除的id
	id = request.GET.get("id")
	# 调用删除的方法
	rs = delete(id)
	# 定义字典
	info = {"info": ""}
	if rs == True:
		money1()
		info["info"] = "删除成功"
	else:
		info["info"] = "删除失败"
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 删除老师表传给前端数据
