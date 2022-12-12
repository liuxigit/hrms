#导入pymysql
import pymysql

def update(applic_id,staff_id,state):
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
    if state == "签约完成" :
        rs = PanDuanId(applic_id,staff_id)
        if rs == True :
            sql = "update t_recruit set staff_id=%s,state=%s where applic_id = %s;"
            cur.execute(sql, (staff_id, state,applic_id))
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
        else :
            return False
    else:
        sql = "update t_recruit set staff_id=null,state=%s where applic_id = %s;"
        cur.execute(sql, (state, applic_id))
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
def add(applic_id,staff_id,state):
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
    #3 定义一个sql语句
    if state == "签约完成":
        rs = PanDuanId(applic_id,staff_id)
        if rs == True:
            sql = "INSERT into t_recruit (applic_id,staff_id,state) values (%s,%s,%s);"
            cur.execute(sql,(applic_id,staff_id,state))
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

        else:
            rs = "id错误"
            return rs
    else:
        sql = "INSERT into t_recruit (applic_id,staff_id,state) values (%s,null,%s);"
        cur.execute(sql,(applic_id,state))
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
    sql ="DELETE FROM t_recruit WHERE applic_id=%s;"
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
        sql1 = "SELECT count(*) from t_recruit "
        cur.execute(sql1)
        rs = cur.fetchall()
        print(rs)
        return rs[0][0]

    else:
        sql1 = "select count(*) from t_staff where edu_back = %s or duty = %s or entry_time like %s or state=%s or section =%s; "
        cur.execute(sql1,(name,name,"%name%",name,name))
        rs = cur.fetchall()
        print(rs)
        return rs[0][0]

def selectAll2(staff_id):
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
    sql ="select edu_back,section,duty,entry_time,state from t_staff where staff_id =%s"
    cur.execute(sql, (staff_id))
    con.commit()
    rs1 = cur.fetchall()
    print(rs1)
    return rs1


def selectlAll(index,row,name):
    dict1 = {"dict": ""}
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
    list = []
    if name =="":
        sql1 = "SELECT t_application.applic_id,t_application.`name`,t_application.sex,t_application.birth,t_application.phone,t_application.email,t_recruit.state ,t_recruit.staff_id FROM t_application,t_recruit WHERE t_application.applic_id = t_recruit.applic_id limit %s,%s;"
        cur.execute(sql1, (index,row))
        con.commit()
        rs1 = cur.fetchall()#不是工人，需要加空值
        for x in rs1:
            # 创建一个字典

            if x[6]=="签约完成":
                print(x[7])
                rs2=selectAll2(x[7])
                print(rs2[0])
                print(rs2)
                dc = {"id": x[0], "name": x[1], "sex": x[2], "birth": x[3], "phone": x[4], "email": x[5], "state": x[6],
                      "staff_id": x[7], "edu_back": rs2[0][0], "section": rs2[0][1], "duty": rs2[0][2], "entry_time": rs2[0][3], "staTe": rs2[0][4]}
                list.append(dc)
            else:
                print("-----")
                dc = {"id": x[0], "name": x[1], "sex": x[2], "birth": x[3], "phone": x[4], "email": x[5], "state": x[6],
                      "staff_id": "", "edu_back": "", "section": "", "duty": "", "entry_time": "", "staTe": ""}
                list.append(dc)


        print(list)
        return list

    else:
        rs =  PanDuanSelect(name,index,row)
        for x in rs:
            sql0 = "SELECT t_application.applic_id,t_application.`name`,t_application.sex,t_application.birth,t_application.phone,t_application.email,t_recruit.state ,t_recruit.staff_id FROM t_application,t_recruit WHERE t_application.applic_id = t_recruit.applic_id and t_recruit.staff_id = %s;"
            cur.execute(sql0, (x[0]))
            con.commit()
            rs3 = cur.fetchall()
            dc = {"id": rs3[0][0], "name": rs3[0][1], "sex": rs3[0][2], "birth": rs3[0][3], "phone": rs3[0][4], "email": rs3[0][5], "state": rs3[0][6],
                  "staff_id": x[0], "edu_back": x[1], "section": x[2], "duty": x[3],
                  "entry_time": x[4], "staTe": x[5]}
            list.append(dc)


        return list

def PanDuanSelect(name,index,row):
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1234",
        database="hrms",
        charset="utf8"
    )
    cur = con.cursor();
    print("name=",name)
    sql = "select staff_id,edu_back,section,duty,entry_time,state from t_staff where edu_back = %s or duty = %s or entry_time like %s or state=%s or section =%s limit %s,%s;"
    cur.execute(sql, (name,name,"%name%",name,name,index,row))
    con.commit()
    rs1 = cur.fetchall()
    print(rs1)
    return rs1

def PanDuanId(staff_id,applic_id):
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
    sql2 = "select applice_id from t_application where applice_id = %s"
    cur.execute(sql, (applic_id))
    con.commit()
    rs2 =cur.fetchall()
    print(rs1)
    print(rs2)
    if rs1!=() and rs2!=():
        print("id存在")
        return True

    else:
        print("id不存在")
        return False



if __name__ == '__main__':
    selectCount("研发部")