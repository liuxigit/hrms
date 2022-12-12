# 导入django的包
import json
from random import *

from django.shortcuts import HttpResponse
# 导入json包
import json
# 导入邮箱发送库
import smtplib
# 导入信封库
from email.mime.text import MIMEText
from 人力资源管理.dao.UserDao import *


# 定义发送验证码
def sendCodeRequest(request):
    info = {"info": "", "code": ""}

    try:
        # 接受邮箱
        email_1 = request.GET.get("email_1")
        rs2 = repwd(email_1)
        if rs2==True:
            # 随机生成四位数
            num = str(randrange(1000, 10000))
            # 定义邮件内容
            content = "xxx公司发送的验证码是：" + num
            # 创建一个信封
            msg = MIMEText(content)
            # 定义收件人
            msg["To"] = email_1
            # 定义发件人
            msg["From"] = "2825033020@qq.com"
            # 定义邮件标题
            msg["Subject"] = "xx公司验证码"
            # 登陆邮件服务器,SMTP邮件服务器
            rs = smtplib.SMTP_SSL("smtp.qq.com", 465)
            rs.login("2825033020@qq.com", "uiawodxihddtdcfg")
            # 发送邮件
            rs.sendmail("2825033020@qq.com", email_1, msg.as_string())
            info["info"] = "邮件发送成功"
            info["code"] = num
        if rs2==False:
            info["info"] = "该邮箱未注册"
    except Exception as e:
        info["info"] = "邮件发送失败 "
        print(e)

    return HttpResponse(json.dumps(info), content_type="application/json")


# 定义发送忘记密码的验证码要求
def sendCode_repwdRequest(request):
    info = {"info": "", "code": ""}

    try:
        # 接受邮箱
        email_2 = request.GET.get("email_2")
        rs2 = repwd(email_2)
        if rs2 == True:
            # 随机生成四位数
            num = str(randrange(1000, 10000))
            # 定义邮件内容
            content = "xxx公司发送的验证码是：" + num
            # 创建一个信封
            msg = MIMEText(content)
            # 定义收件人
            msg["To"] = email_2
            # 定义发件人
            msg["From"] = "2825033020@qq.com"
            # 定义邮件标题
            msg["Subject"] = "xx公司验证码"
            # 登陆邮件服务器,SMTP邮件服务器
            rs = smtplib.SMTP_SSL("smtp.qq.com", 465)
            rs.login("2825033020@qq.com", "uiawodxihddtdcfg")
            # 发送邮件
            rs.sendmail("2825033020@qq.com", email_2, msg.as_string())
            info["info"] = "邮件发送成功"
            info["code"] = num
        if rs2 == False:
            info["info"] = "该邮箱地址未绑定账号"
    except Exception as e:
        info["info"] = "邮件发送失败 "
        print(e)

    return HttpResponse(json.dumps(info), content_type="application/json")
