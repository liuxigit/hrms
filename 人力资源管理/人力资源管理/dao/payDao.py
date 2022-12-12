#导入pymysql
import pymysql

def update(staff_id,type,money,check_peo,check_id):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    sql = "update t_check set staff_id =%s, type=%s,money=%s,check_peo=%s where check_id = %s;"
    cur.execute(sql, (staff_id,type,money,check_peo,check_id))
    con.commit()
    rs = cur.fetchall()
    con.commit()
    num = cur.rowcount
    cur.close()
    con.close()
    if num > 0:
        print("新增成功")
        return True
    else:
        print("新增失败")
        return False



#新增
def add(staff_id,type,money,check_peo):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    #print(name,age)
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    re = PanDuanId(staff_id)
    if re == True:

        sql = "INSERT into t_check (staff_id,type,money,check_peo) values (%s,%s,%s,%s);"
        cur.execute(sql,(staff_id,type,money,check_peo))
        con.commit()
        rs = cur.fetchall()
        num = cur.rowcount
        cur.close()
        con.close()
        if num > 0:
            print("新增成功")
            return True
        else:
            print("新增失败")
            return False

    else:
        rs = "id错误"
        return rs



def delete(id):
  #1 创建mysql的数据库链接
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    #2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    #3 定义一个sql语句
    sql ="DELETE FROM t_check WHERE check_id =%s;"
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
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    # 2 创建操作数据库表的增删改查的对象 ,游标对象
    cur = con.cursor();
    if name == "":

        # 3 定义一个sql语句
        sql = "select count(*) from t_check inner join t_staff on t_staff.staff_id = t_check.staff_id"
        # 4 运行sql
        cur.execute(sql)
    else:
        sql = "select count(*) from t_check inner join t_staff on t_staff.staff_id = t_check.staff_id where check_id = %s or t_check.staff_id =%s or name LIKE %s"
        cur.execute(sql,(name,name,"%"+name+"%"))
    # 5 获取查询结果
    rs = cur.fetchall()
    print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象0
    con.close()
    return rs[0][0]

def select(index,row,name):
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
    if name == "":
        # 3 定义一个sql语句
        sql = "select check_id,t_check.staff_id,name,type,money,check_peo from t_check inner join t_staff on t_staff.staff_id = t_check.staff_id limit %s,%s;"
        cur.execute(sql, (index, row))
    else:
        sql = "select check_id,t_check.staff_id,name,type,money,check_peo from t_check inner join t_staff on t_staff.staff_id = t_check.staff_id where check_id = %s or t_check.staff_id =%s or name LIKE %s limit %s,%s;"
        cur.execute(sql, (name,name,"%"+name+"%",index, row))
        # 4 运行sql

    # 5 获取查询结果
    rs = cur.fetchall()
    #print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs

def PanDuanId(staff_id):
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    cur = con.cursor();
    sql = "select staff_id from t_staff where staff_id = %s"
    cur.execute(sql,(staff_id))
    con.commit()
    rs1 = cur.fetchall()
    if rs1!=() :
        print("id存在")
        return True

    else:
        print("id不存在")
        return False

def money1():
    print('0000')
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8")
    cur = con.cursor()
    sql="SELECT t.staff_id, sum(t.money) from t_staff   ts INNER JOIN t_check t on ts.staff_id = t.staff_id where t.money>=0 GROUP BY t.staff_id "
    cur.execute(sql)
    rs = cur.fetchall()
    print("rs")
    for x in rs:
            sql1 = "update t_pay set bonus = %s where staff_id = %s;"
            cur.execute(sql1,(x[1],x[0]))
            con.commit()

    sql2 = "SELECT t.staff_id, sum(t.money) from t_staff   ts INNER JOIN t_check t on ts.staff_id = t.staff_id where t.money<=0 GROUP BY t.staff_id "
    cur.execute(sql2)
    rs1 = cur.fetchall()
    print("rs1")
    for y in rs1:
            sql3 ="update t_pay set fine = %s where staff_id = %s;"
            cur.execute(sql3, (y[1], y[0]))
            con.commit()
    sql4 = "UPDATE t_pay SET total = base_pay+merit_pay+bonus+fine"
    cur.execute(sql4)
    cur.close()
    # 关闭数据库链接对象
    con.close()

if __name__ == '__main__':
    money1()