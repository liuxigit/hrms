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

    sql = 'select * from t_admin where username=%s and password=%s'

    cur.execute(sql, (username, password))

    rs = cur.fetchall()
    print(rs)
    cur.close()
    connection.close()
    if len(rs) > 0:
        return True
    else:
        return False