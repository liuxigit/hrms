#导入pymysql
import pymysql

def update(pay_id,base_pay,merit_pay,bonus,fine,total,get_time):
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
    sql = "update t_pay set base_pay=%s,merit_pay=%s,bonus=%s,fine=%s,total=%s,get_time=%s where pay_id = %s;"
    cur.execute(sql, (base_pay,merit_pay,bonus,fine,0,get_time,pay_id))
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
def add(staff_id,base_pay,merit_pay,bonus,fine,total,get_time):
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

        sql = "INSERT into t_pay (staff_id,base_pay,merit_pay,bonus,fine,total,get_time) values (%s,%s,%s,%s,%s,%s,%s);"
        cur.execute(sql,(staff_id,base_pay,merit_pay,bonus,fine,total,get_time))
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
    sql ="DELETE FROM t_pay WHERE pay_id=%s;"
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
    rs1 = selectStaff_id(name)
    if name == "":

        # 3 定义一个sql语句
        sql = "select count(*) from t_pay"
        # 4 运行sql
        cur.execute(sql)
    else:
        rs1 = selectStaff_id(name)
        sql = "SELECT count(*) from t_staff   ts INNER JOIN t_pay t on ts.staff_id = t.staff_id where ts.staff_id =%s or name like %s"
        cur.execute(sql, (name,"%"+name+"%"))
    # 5 获取查询结果
    rs = cur.fetchall()
    #print(rs)
    # 关闭游标对象
    cur.close()
    # 关闭数据库链接对象
    con.close()
    return rs[0][0]

def select(name,index,row):
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

    #rs1 = selectStaff_id(name)
    if name == "":
        # 3 定义一个sql语句
        sql = "SELECT * from t_pay limit %s,%s;"
        cur.execute(sql, (index, row))
    else:

        sql = "SELECT pay_id,ts.staff_id,base_pay,merit_pay,bonus,fine,total,get_time from t_staff   ts INNER JOIN t_pay t on ts.staff_id = t.staff_id where ts.staff_id =%s or name like %s limit %s,%s "
        cur.execute(sql, (name,"%"+name+"%",index, row))

    rs = cur.fetchall()
    print(rs)
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
        cur.close()
        # 关闭数据库链接对象
        con.close()

    else:
        print("id不存在")
        return False
        cur.close()
        # 关闭数据库链接对象
        con.close()

def selectStaff_id(name):
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
    sql = "select staff_id from t_staff where name like %s;"
    cur.execute(sql,("%"+name+"%"))
    con.commit()
    rs1 = cur.fetchall()
    list = []
    for x in rs1:
        list.append(x[0])
    return list
def updateTotal(total,staff_id):
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
    sql = "update t_pay set total=%s where pay_id = %s;"
    cur.execute(sql,(total,staff_id))
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    selectStaff_id()



