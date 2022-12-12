import pymysql


def select_01(index, row, name):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    cur = connection.cursor()  # 建立游标
    print("select")
    if name == "":
        sql = 'select * from t_staff limit %s,%s'
        cur.execute(sql, (index, row))
    else:
        sql = 'select * from t_staff where name like %s limit %s,%s'
        cur.execute(sql, ("%" + name + "%", index, row))
    rs = cur.fetchall()
    print(rs)
    connection.commit()
    cur.close()
    connection.close()
    return rs


def select_02(index, row, sex, edu_back, section, state):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    cur = connection.cursor()  # 建立游标
    print("select")
    sql = 'select * from t_staff where sex = %s or edu_back=%s or section=%s or state=%s limit %s,%s'
    cur.execute(sql, (sex, edu_back, section, state, index, row))
    rs = cur.fetchall()
    print(rs)
    connection.commit()
    cur.close()
    connection.close()
    return rs


def selectLenth_01(name):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    print("selectlenth")
    cur = connection.cursor()  # 建立游标
    if name == "":
        sql = 'select count(*) from t_staff'
        cur.execute(sql)
    else:
        print("zheer")
        sql = 'select count(*) from t_staff where name like %s'
        cur.execute(sql, "%" + name + "%")
    rs = cur.fetchall()
    print(rs)
    connection.commit()
    cur.close()
    connection.close()
    return rs[0][0]


def selectLenth_02(sex, edu_back, section, state):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    print("selectlenth")
    cur = connection.cursor()  # 建立游标

    print("zheer")
    sql = 'select count(*) from t_staff where sex = %s or edu_back=%s or section=%s or state=%s'
    cur.execute(sql, (sex, edu_back, section, state))
    rs = cur.fetchall()
    print(rs)
    connection.commit()
    cur.close()
    connection.close()
    return rs[0][0]


def delete(id):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    cur = connection.cursor()  # 建立游标
    sql = 'delete from t_staff where staff_id=%s '

    cur.execute(sql, id)
    rs = cur.rowcount
    connection.commit()
    connection.close()
    if rs > 0:
        print("删除成功")
        return True
    else:
        print("删除失败")
        return False


def update(id, name, sex, birth, phone, email, edu_back, section, duty, entry_time, state):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'update t_staff set name=%s, sex=%s, birth=%s, phone=%s, email=%s, edu_back=%s, section=%s, duty=%s, entry_time=%s, state=%s where staff_id=%s '
    cur.execute(sql, (name, sex, birth, phone, email, edu_back, section, duty, entry_time, state, id))
    rs = cur.rowcount
    connection.commit()
    connection.close()
    if rs > 0:
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False


def add(name, sex, birth, phone, email, edu_back, section, duty, entry_time, state):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标

    sql = 'insert into t_staff (name,sex, birth, phone, email, edu_back, section, duty, entry_time, state) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (name, sex, birth, phone, email, edu_back, section, duty, entry_time, state))
    rs = cur.rowcount
    connection.commit()
    connection.close()
    if rs > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False