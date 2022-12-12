from django.shortcuts import HttpResponse
from 人力资源管理.dao.contractDao import *
import json
import math


def contract_selectRequest(request):
    print("执行contro")
    page = int(request.GET.get("page"))
    name = request.GET.get("name")
    row = int(request.GET.get("row"))
    print("ffffffffffff")
    index = row * (page - 1)

    list = []
    rs = select(index, row, name)

    c = int(selectLenth(name))

    totalpage = math.ceil(c / row)

    for i in rs:
        dic = {"name": i[0], "contract_id": i[1], "staff_id": i[2], "start_day": i[3], "end_day": i[4], "duty": i[5],
               "content": i[6], "remark": i[7]}
        list.append(dic)
    info = {"list": list, "total": c, "totalpage": totalpage}
    return HttpResponse(json.dumps(info), content_type="application/json")



def contract_AddRequest(request):


    # 姓名

    staff_id = request.GET.get("staff_id")
    start_day = request.GET.get("start_day")
    end_day = request.GET.get("end_day")
    duty = request.GET.get("duty")
    content = request.GET.get("content")
    remark = request.GET.get("remark")


    print(staff_id, start_day, end_day, duty, content, remark)

    rs = add(staff_id, start_day, end_day, duty, content, remark)

    info = {"info": ""}
    if rs == True:
        info["info"] = "新增成功"
    elif rs=='员工不存在':
        info["info"] = "员工不存在"
    else:
        info["info"] = "新增失败"
    return HttpResponse(json.dumps(info), content_type="application/json")


def contract_deleteRequest(request):
    # 获取id
    id = request.GET.get("id")
    print(id)
    rs = delete(id)

    info = {"info": ""}
    if rs == True:
        info["info"] = "删除成功"
    else:
        info["info"] = "删除失败"
    return HttpResponse(json.dumps(info), content_type="application/json")


def contract_editRequest(request):
    # 获取id
    contract_id = request.GET.get("contract_id")
    start_day = request.GET.get("start_day")
    end_day = request.GET.get("end_day")
    duty = request.GET.get("duty")
    content = request.GET.get("content")
    remark = request.GET.get("remark")

    print(contract_id)
    rs = edit(contract_id,start_day,end_day,duty,content,remark)

    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    return HttpResponse(json.dumps(info), content_type="application/json")


