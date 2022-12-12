#导入pymysql
import pymysql

def update(name,sex,birth,phone,email,time,id):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="hrms",
        charset="utf8"
    )
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    #3 定义一个sql语句
    sql ="update t_application set name=%s,sex=%s,birth=%s,phone=%s,email=%s,time=%s where applic_id = %s;"
    #4 运行sql
    cur.execute(sql,(name,sex,birth,phone,email,time,id))
    #5 提交事务
    con.commit()
    #获取受影响行数
  # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    num = cur.rowcount
    if num > 0:
        print("修改成功")
        return True
    else:
        print("修改失败")
        return False



#新增
def add(name,sex,birth,phone,email,time):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="hrms",
        charset="utf8"
    )
    #print(name,age)
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    #3 定义一个sql语句
    sql ="INSERT into t_application (name,sex,birth,phone,email,time) values (%s,%s,%s,%s,%s,%s);"
    #4 运行sql
    cur.execute(sql,(name,sex,birth,phone,email,time))
    #5 提交事务
    con.commit()
    #获取受影响行数
    num = cur.rowcount
    cur.close()
    con.close()
    if num > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False


def select(index,row,name):
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
        sql = "SELECT * from t_application limit %s,%s;"
        cur.execute(sql, (index, row))
    else:
        sql = "SELECT * from t_application where name like %s or sex = %s or birth like %s or  time like %s limit %s,%s;"
        cur.execute(sql, ("%"+name+"%",name,"%"+name+"%","%"+name+"%",index, row))
        # 4 运行sql

    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs


def delete(id):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        database="hrms",
        charset="utf8"
    )
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    #3 定义一个sql语句
    sql ="DELETE FROM t_application WHERE  applic_id=%s;"
    #4 运行sql
    cur.execute(sql,(id))
    #5 提交事务
    con.commit()
    #获取受影响行数
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
        sql = "select count(*) from t_application"
        # 4 运行sql
        cur.execute(sql)
    else:
        sql = "select count(*) from t_application where name like %s"
        cur.execute(sql,(name))
    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs[0][0]



def select(index,row,name):
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
        sql = "SELECT * from t_application limit %s,%s;"
        cur.execute(sql, (index, row))
    else:
        sql = "SELECT * from t_application where name like %s or sex = %s or birth like %s or  time like %s limit %s,%s;"
        cur.execute(sql, ("%"+name+"%",name,"%"+name+"%","%"+name+"%",index, row))
        # 4 运行sql

    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs
if __name__ == '__main__':
    update()