# 导入pymysql
import pymysql


# 新增
def add(name, pwd, user_email):
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
    print("--------------------------")
    print(name, pwd, user_email)
    sql = "INSERT into t_user (username,password,user_email) values (%s,%s,%s);"
    # 4 运行sql
    cur.execute(sql, (name, pwd,user_email))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    if num > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False


# 查询
def select(index, row, name):
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
    cur = con.cursor();
    if name == "":
        # 3 定义一个sql语句
        sql = "SELECT * from t_user limit %s,%s;"
        # 4 运行sql
        cur.execute(sql, (index, row))
    else:
        sql = "SELECT * from t_user where username like %s limit %s,%s"
        cur.execute(sql, ("%" + name + "%", index, row))
    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs


def update(id,name, pwd, user_email):
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
    cur = con.cursor();
    # 3 定义一个sql语句
    sql = "update t_user set username=%s,password=%s,user_email=%s where user_id = %s;"
    # 4 运行sql
    cur.execute(sql, (name, pwd, user_email,id))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    if num > 0:
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False


def delete(id):
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
    sql = "delete from t_user where user_id = %s"
    # 4 运行sql
    cur.execute(sql, (id))
    # 5 提交事务
    con.commit()
    # 获取受影响行数
    num = cur.rowcount
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    if num > 0:
        print("删除成功")
        return True
    else:
        print("删除失败")
        return False


# 查询总条数
def selectCount(name):
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
    cur = con.cursor();
    if name == "":
        # 3 定义一个sql语句
        sql = "SELECT count(*) from t_user;"
        # 4 运行sql
        cur.execute(sql)
    else:
        # 3 定义一个sql语句
        sql = "SELECT count(*) from t_user where username like %s;"
        # 4 运行sql
        cur.execute(sql, ("%" + name + "%"))
    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs[0][0])
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs[0][0]


# 验证用户名重名
def valiDateName(name):
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
    # 定义sql
    sql = "select * from t_user where username=%s"
    # 运行sql
    cur.execute(sql, name)
    # 获取查询结果
    rs = cur.fetchall()
    print(rs)
    cur.close()
    con.close()
    # 根据元组的长度判断用户名是否重名
    if len(rs) > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    selectCount()
