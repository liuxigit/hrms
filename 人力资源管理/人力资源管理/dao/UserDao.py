import pymysql


def login(username, password):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'select * from t_user where username=%s and password=%s'

    cur.execute(sql, (username, password))

    rs = cur.fetchall()
    print(rs)
    cur.close()
    connection.close()
    if len(rs) > 0:
        return True
    else:
        return False


#自动填入邮箱
def autoemail(username):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'select user_email from t_user where username=%s'

    cur.execute(sql, (username,))

    rs = cur.fetchall()
    print(rs)
    cur.close()
    connection.close()
    return rs



def selectUser(name, pwd, user_email):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'select * from t_user where username=%s'

    cur.execute(sql, (name,))
    rs = cur.fetchall()
    print(rs)
    sql2 = "select username from t_user where user_email=%s"
    cur.execute(sql2, (user_email,))
    rs2 = cur.fetchall()
    print(rs2)
    cur.close()
    connection.close()
    if len(rs) > 0:
        return True
    if len(rs2) > 0:
        return "该邮箱已绑定账号"
    if len(rs) == 0 and len(rs2) == 0:
        return False


def regist(name, pwd, user_email):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'insert into t_user (username,password,user_email) values(%s,%s,%s)'

    cur.execute(sql, (name, pwd, user_email))
    rs = cur.rowcount
    connection.commit()
    connection.close()
    if rs > 0:
        print("注册成功")
        return True
    else:
        print("注册失败")
        return False

# 重置密码
def change_pwd(newPwd, username):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor()
    # 3 定义一个sql语句
    sql = "update t_user set password=%s where username=%s;"
    # 4 运行sql
    cur.execute(sql, (newPwd, username))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    if num > 0:
        print("重置成功")
        return True
    else:
        print("重置失败")
        return False

# 忘记密码的重置密码
def change_pwd2(newPwd, email_2):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor()
    # 3 定义一个sql语句
    sql = "update t_user set password=%s where user_email=%s;"
    # 4 运行sql
    cur.execute(sql, (newPwd, email_2))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    if num > 0:
        print("重置成功")
        return True
    else:
        print("重置失败")
        return False

#定义忘记密码的函数
def repwd(usernameAndEmial):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'select * from t_user where user_email=%s'

    cur.execute(sql, (usernameAndEmial,))
    rs = cur.fetchall()
    print(rs)
    cur.close()
    connection.close()
    if len(rs) > 0:
        return True
    else:
        return False



def set_user_state(user_state, username):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="123456",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'update t_user set state=%s where username=%s'

    cur.execute(sql, (user_state, username))
    #受影响函数
    rs = cur.rowcount
    #提交事务
    connection.commit()
    connection.close()
    cur.close()
    if rs > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    login("lx", "lx")
    change_pwd("1234567", "sa")
