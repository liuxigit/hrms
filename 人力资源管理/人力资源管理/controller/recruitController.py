# 导入django的包
import json

from django.shortcuts import HttpResponse
# 导入dao包
from 人力资源管理.dao.recruitDao import *
#导入math
import math


def recruitAddRequest(request):
	# 获取用户名
	# 是前端定义的键名
	applic_id = request.GET.get("applic_id")
	staff_id = request.GET.get("staff_id")
	state = request.GET.get("state")
	# 打印姓名和年龄
	#print("name=", name)
   # print("age=", age)
	# 调用add方法，并获取返回值
	rs = add(applic_id,staff_id,state)
	# 创建字典
	info = {"info": ""}
	if rs == True:
		info["info"] = "新增成功"
	else:
		info["info"] = "新增失败"
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")



def recruitListRequest(request):
	page = int(request.GET.get("page"))
	# 显示每页条数
	row = int(request.GET.get("row"))
	# 每一页查询的index的值
	index = row * (page - 1)
	name = request.GET.get("name")
	# 查询结果，得到返回结果
	list = selectlAll(index,row,name)
	# 查询总条数
	c = selectCount(name)
	#计算总页数
	totalPage = math.ceil(c/row)
	info = {"list": list, "total": c, "totalPage": totalPage}
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 接受前端发送的查询老师列表的请求的函数

def recruitUpdateRequest(request):
	applic_id = request.GET.get("applic_id")
	staff_id = request.GET.get("staff_id")
	state = request.GET.get("state")
	rs = update(applic_id,staff_id,state)
	info = {"info": ""}
	if rs == True:
		info["info"] = "修改成功"
	else:
		info["info"] = "修改失败"
	# 定义返回给前端的数据
	return HttpResponse(json.dumps(info), content_type="application/json")


# 修改老师传给前端数据


# 删除
def recruitDelRequest(request):
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
