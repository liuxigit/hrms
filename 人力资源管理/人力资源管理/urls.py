"""人力资源管理 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from 人力资源管理.controller.staffController import *
from 人力资源管理.controller.contractController import *
from 人力资源管理.controller.userController import *
from 人力资源管理.controller.adminController import *
from 人力资源管理.controller.t_personal_transController import *
from 人力资源管理.controller.t_recordController import *
from 人力资源管理.controller.sendcodeController import *
from 人力资源管理.controller.admin_to_userController import *

#马椿淋模块
from 人力资源管理.controller.applicationController import *
from 人力资源管理.controller.payController import *
from 人力资源管理.controller.checkController import *
from 人力资源管理.controller.recruitController import *


urlpatterns = [
    path('admin/', admin.site.urls),

    # 配置staff_selectRequest url
    path('staff_select/', staff_selectRequest),

    # 配置staff_deleteRequest url
    path('staffDel/', staff_deleteRequest),

    # 配置staff_UpdateRequest url
    path('staffUpdate/', staff_UpdateRequest),

    # 配置staff_AddRequest url
    path('staffAdd/', staff_AddRequest),

    # 配置contract_selectRequest url
    path('contract_select/', contract_selectRequest),

    # 配置contract_AddRequest url
    path('contract_add/', contract_AddRequest),

    # 配置contract_deleteRequest url
    path('contract_del/', contract_deleteRequest),

    # 配置contract_editRequest url
    path('contract_edit/', contract_editRequest),


    #邹鑫阳部分

    path('login/', loginRequest),
    path('regist/', registRequest),
    path('autoEmail/', autoEmailRequest),
    path('changePwd/', changePwdRequest),
    path('sendCode/', sendCodeRequest),
    path('sendCode_repwd/', sendCode_repwdRequest),
    path('repwd/', rePwdRequest),
    path('tptList/', tptListRequest),
    path('tptUpdata/', tptUpdateRequest),
    path('tptDel/', tptDelRequest),
    path('tptAdd/', tptAddRequest),
    path('tptAutoName/', tptAutoNameRequest),
    path('trList/', trListRequest),
    path('trUpdata/', trUpdateRequest),
    path('trDel/', trDelRequest),
    path('trAdd/', trAddRequest),
    path('trAutoId/', trAutoIdRequest),
    path('admin_login/', admin_loginRequest),
    path('exit_set_state/', exitStateRequest),


    #刘杰部分
    # 配置addRequest函数的映射地址
    path('userAdd/', addRequest),
    # 配置stuListRequest函数的映射地址
    path('userList/', userListRequest),
    # 配置teacherUpdateRequest函数的映射地址
    path('userUpdate/', userUpdateRequest),
    # 配置teacherUpdateRequest函数的映射地址
    path('userDel/', userDelRequest),


    #马椿淋
    path('applicationAdd/', applicationAddRequest),
    path('applicationList/', applicationListRequest),
    path('applicationUpdate/', applicationUpdateRequest),
    path('applicationDel/', applicationDelRequest),
    path('recruitList/', recruitListRequest),
    path('recruitAdd/', recruitAddRequest),
    path('recruitDel/', recruitDelRequest),
    path('recruitUpdate/', recruitUpdateRequest),
    path('payList/', payListRequest),
    path('payAdd/', payAddRequest),
    path('payDel/', payDelRequest),
    path('payUpdate/', payUpdateRequest),
    path('checkList/', checkListRequest),
    path('checkAdd/', checkAddRequest),
    path('checkDel/', checkDelRequest),
    path('checkUpdate/', checkUpdateRequest)

]
