import pymysql


# 查询
def select(index, row, message):
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
        sql = "SELECT t_personal_trans.pertra_id,t_personal_trans.staff_id,t_staff.name,t_personal_trans.last_section,t_personal_trans.next_section,t_personal_trans.last_duty,t_personal_trans.next_duty,t_personal_trans.trans_time,t_personal_trans.causee FROM t_staff,t_personal_trans where (t_staff.staff_id=t_personal_trans.staff_id) order by t_personal_trans.trans_time limit %s,%s"
        # 4 运行sql
        cur.execute(sql, (index, row))
    else:
        sql = "SELECT t_personal_trans.pertra_id,t_personal_trans.staff_id,t_staff.name,t_personal_trans.last_section,t_personal_trans.next_section,t_personal_trans.last_duty,t_personal_trans.next_duty,t_personal_trans.trans_time,t_personal_trans.causee FROM t_staff,t_personal_trans where (t_staff.name  like %s or t_staff.staff_id like %s) and (t_staff.staff_id=t_personal_trans.staff_id) order by t_personal_trans.trans_time limit %s,%s"
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
def selectCount(message):
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
        sql = "select count(*) from t_personal_trans;"
        # 4 运行sql
        cur.execute(sql)
    else:
        sql = "SELECT count(*) FROM t_staff,t_personal_trans where (t_staff.name  like %s or t_staff.staff_id like %s) and (t_staff.staff_id=t_personal_trans.staff_id) order by t_personal_trans.trans_time"
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
def update(last_section, next_section, last_duty, next_duty, trans_time, causee, staff_id):
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
    sql = "update t_personal_trans set last_section=%s,next_section =%s,last_duty =%s,next_duty =%s,trans_time =%s,causee =%s   where staff_id = %s;"
    # 4 运行sql
    cur.execute(sql, (last_section, next_section, last_duty, next_duty, trans_time, causee, staff_id))
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
def delete(pertra_id):
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
    sql = "DELETE FROM t_personal_trans  WHERE  pertra_id=%s;"
    # 4 运行sql
    cur.execute(sql, pertra_id)
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
def selectid(staff_id):
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
def add(staff_id, last_section, next_section, last_duty, next_duty, trans_time, causee):
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
    sql = "INSERT into t_personal_trans (staff_id, last_section, next_section, last_duty, next_duty, trans_time, causee) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    # 运行sql语句
    cur.execute(sql, (staff_id, last_section, next_section, last_duty, next_duty, trans_time, causee))
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


if __name__ == '__main__':
    selectid(1)
