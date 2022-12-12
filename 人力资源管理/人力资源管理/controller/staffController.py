from django.shortcuts import HttpResponse
from 人力资源管理.dao.staffDao import *
import json
import math


def staff_selectRequest(request):
    print("执行contro")
    page = int(request.GET.get("page"))
    name = request.GET.get("name")
    row = int(request.GET.get("row"))
    sex = str(request.GET.get("sex"))
    edu_back = str(request.GET.get("edu_back"))
    section = str(request.GET.get("section"))
    state = str(request.GET.get("state"))

    index = row * (page - 1)

    if sex == '' and edu_back == '' and section == '' and state == '':
        print("++1111")
        list = []
        rs = select_01(index, row, name)
        c = selectLenth_01(name)
        totalpage = math.ceil(c / row)
        for i in rs:
            dic = {"staff_id": i[0], "name": i[1], "sex": i[2], "birth": i[3], "phone": i[4], "email": i[5],
                   "edu_back": i[6], "section": i[7], "duty": i[8], "entry_time": i[9], "state": i[10]}
            list.append(dic)
        info = {"list": list, "total": c, "totalpage": totalpage}
        return HttpResponse(json.dumps(info), content_type="application/json")
    else:
        print("++2222")
        list = []
        rs = select_02(index, row, sex, edu_back, section, state)
        c = selectLenth_02(sex, edu_back, section, state)
        totalpage = math.ceil(c / row)
        for i in rs:
            dic = {"staff_id": i[0], "name": i[1], "sex": i[2], "birth": i[3], "phone": i[4], "email": i[5],
                   "edu_back": i[6], "section": i[7], "duty": i[8], "entry_time": i[9], "state": i[10]}
            list.append(dic)
        info = {"list": list, "total": c, "totalpage": totalpage}
        return HttpResponse(json.dumps(info), content_type="application/json")


def staff_deleteRequest(request):
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


def staff_UpdateRequest(request):
    # 获取id
    id = request.GET.get("id")

    # 姓名
    name = request.GET.get("name")
    sex = request.GET.get("sex")
    birth = request.GET.get("birth")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    edu_back = request.GET.get("edu_back")
    section = request.GET.get("section")
    duty = request.GET.get("duty")
    entry_time = request.GET.get("entry_time")
    state = request.GET.get("state")

    print(id, name, sex, birth, phone, email, edu_back, section, duty, entry_time, state)

    rs = update(id, name, sex, birth, phone, email, edu_back, section, duty, entry_time, state)

    info = {"info": ""}
    if rs == True:
        info["info"] = "修改成功"
    else:
        info["info"] = "修改失败"
    return HttpResponse(json.dumps(info), content_type="application/json")

def staff_AddRequest(request):


    # 姓名
    name = request.GET.get("name")
    sex = request.GET.get("sex")
    birth = request.GET.get("birth")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    edu_back = request.GET.get("edu_back")
    section = request.GET.get("section")
    duty = request.GET.get("duty")
    entry_time = request.GET.get("entry_time")
    state = request.GET.get("state")

    print(name, sex, birth, phone, email, edu_back, section, duty, entry_time, state)

    rs = add(name, sex, birth, phone, email, edu_back, section, duty, entry_time, state)

    info = {"info": ""}
    if rs == True:
        info["info"] = "新增成功"
    else:
        info["info"] = "新增失败"
    return HttpResponse(json.dumps(info), content_type="application/json")