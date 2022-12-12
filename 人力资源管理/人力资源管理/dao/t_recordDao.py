import pymysql

import pymysql


# 查询
def select_tr(index, row, message):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor()
    if message == "":

        # 3 定义一个sql语句
        sql = "SELECT * FROM t_record  limit %s,%s"
        # 4 运行sql
        cur.execute(sql, (index, row))
    else:
        sql = "SELECT * FROM t_record where (record_name  like %s or record_id like %s) limit %s,%s"
        #  运行sql
        cur.execute(sql, ("%" + message + "%", "%" + message, index, row))
    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs


# 查询总条数count
def selectCount_tr(message):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor()
    if message == "":
        # 3 定义一个sql语句
        sql = "select count(*) from t_record;"
        # 4 运行sql
        cur.execute(sql)
    else:
        sql = "SELECT count(*) FROM t_record where (record_name  like %s or record_id like %s)"
        # 4 运行sql
        cur.execute(sql, ("%" + message + "%", "%" + message))

    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs[0][0])
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs[0][0]


# 修改
def update_tr(record_name, digest, remark, record_id):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor()
    # 3 定义一个sql语句
    sql = "update t_record set record_name=%s,digest =%s,remark =%s  where record_id = %s;"
    # 4 运行sql
    cur.execute(sql, (record_name, digest, remark, record_id,))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    if num > 0:
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False


# 删除
def delete_tr(record_id):
    # 1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    # 3 定义一个sql语句
    sql = "DELETE FROM t_record  WHERE  record_id=%s;"
    # 4 运行sql
    cur.execute(sql, record_id)
    # 5 提交事务
    con.commit()
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    # 获取受影响行数
    num = cur.rowcount
    if num > 0:
        print("删除成功")
        return True
    else:
        print("删除失败")
        return False


# 根据id查询名字是否存在, last_section, next_section, last_duty, next_duty, trans_time, causee
def select_tr_id(staff_id):
    # 创建mysql的数据库连接
    con = pymysql.connect(host="localhost",
                          port=3306,
                          user="root",
                          password="1234",
                          database="hrms",
                          charset="utf8")
    # 创建数据库表增删改查操作对象
    cur = con.cursor()
    # 查询员工表中staff_id列的sql
    sql1 = "select name from t_staff where staff_id=%s"
    cur.execute(sql1, (staff_id,))
    rs = cur.fetchall()
    print(rs)
    # 判断人力调动员工id是否存在
    if rs == "":
        return False
    else:
        return rs

#新增
def add_tr(staff_id, record_name, digest, remark):
    # 创建mysql的数据库连接
    con = pymysql.connect(host="localhost",
                          port=3306,
                          user="root",
                          password="1234",
                          database="hrms",
                          charset="utf8")
    # 创建数据库表增删改查操作对象
    cur = con.cursor()
    # 定义一个sql语句
    sql = "INSERT into t_record (staff_id, record_name, digest, remark) VALUES (%s,%s,%s,%s);"
    # 运行sql语句
    cur.execute(sql, (staff_id, record_name, digest, remark))
    # 提交事务
    con.commit()
    # 关闭游标
    cur.close()
    # 关闭数据库对象
    con.close()

    # 获取受影响行数
    num = cur.rowcount
    if num > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False


