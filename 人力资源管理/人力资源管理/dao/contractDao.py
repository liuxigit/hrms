import pymysql


def select(index, row, name):
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
        sql = 'select t_staff.name,t_contract.* from t_contract,t_staff where t_contract.staff_id=t_staff.staff_id limit %s,%s'
        cur.execute(sql, (index, row))
    else:
        sql = 'select t_staff.name,t_contract.* from t_contract,t_staff where t_contract.staff_id=t_staff.staff_id and (t_staff.staff_id=%s or t_staff.name like %s) limit %s,%s'
        cur.execute(sql, (name, "%" + name + "%", index, row))
    rs = cur.fetchall()
    print(rs)
    connection.commit()
    cur.close()
    connection.close()
    return rs


def selectLenth(name):
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
        sql = 'select count(*) from t_contract,t_staff where t_contract.staff_id=t_staff.staff_id'
        cur.execute(sql)
    else:
        sql = 'select count(*) from t_contract,t_staff where t_contract.staff_id=t_staff.staff_id and (t_staff.staff_id=%s or t_staff.name like %s)'
        cur.execute(sql, (name, "%" + name + "%"))
    rs = cur.fetchall()
    print(rs[0][0])
    connection.commit()
    cur.close()
    connection.close()
    return rs[0][0]


def add(staff_id, start_day, end_day, duty, content, remark):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )

    cur = connection.cursor()  # 建立游标
    sql2 = 'select * from t_staff where staff_id=%s'
    cur.execute(sql2, (staff_id))
    rs2 = cur.rowcount
    if (rs2 == 0):
        return "员工不存在"

    sql = 'insert into t_contract (staff_id, start_day, end_day, duty, content, remark) values (%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, (staff_id, start_day, end_day, duty, content, remark))
    rs = cur.rowcount
    connection.commit()
    connection.close()
    print("开始ADD")
    if rs > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False


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
    sql = 'delete from t_contract where contract_id=%s '

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


def edit(contract_id, start_day, end_day, duty, content, remark):
    connection = pymysql.connect(
        host='localhost',  # 服务器ip地址
        port=3306,  # mysql默认端口号
        user="root",  # 用户名
        password="1234",  # 密码
        charset="utf8",  # 字符集
        db="hrms"  # 数据库
    )
    cur = connection.cursor()  # 建立游标
    sql = 'update t_contract set start_day=%s,end_day=%s,duty=%s,content=%s,remark=%s where contract_id=%s '

    cur.execute(sql, (start_day, end_day, duty, content, remark, contract_id))
    rs = cur.rowcount
    connection.commit()
    connection.close()
    if rs > 0:
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False
