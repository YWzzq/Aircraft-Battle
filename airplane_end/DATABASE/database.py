from DATABASE import user, connect
##根据名字查找用户
##用于登录
##返回USER
def findbyName(name):
    conn = connect.cnt()
    # 创建游标对象
    cursor = conn.cursor()
    # 执行查询语句
    query = "SELECT * FROM users where Name=\'"+name+'\''  # 替换为你的查询语句
    print(query)
    cursor.execute(query)
    # 获取查询结果
    results = cursor.fetchall()
    if results:
        userss = user.User(results[0][1], results[0][2])
        userss.ID = results[0][0]
        userss.Grade = results[0][3]
        cursor.close()
        conn.close()
        return userss
    else:
        cursor.close()
        conn.close()
        return None

##添加用户，需要指定用户名和密码
##用于注册
def addtousers(user1):
    conn= connect.cnt()
    cursor = conn.cursor()
    # 执行查询语句
    if(findbyName(user1.name)):
        cursor.close()
        # 关闭连接
        conn.close()
        raise Exception('用户名存在')
        return None
    else:
        query = 'EXEC p_insert \''+user1.name+'\','+'\''+user1.password+'\''
        print(query)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        # 关闭连接
        conn.close()
        return True
##添加分数记录
##游戏结束写入
def addtorecord(id,grade):
    conn= connect.cnt()
    cursor=conn.cursor()
    query='EXEC p_insert_record '+str(id)+','+str(grade)
    print(query)
    cursor.execute(query)
    cursor.commit()
    cursor.close()
    conn.close()
##
#删除游客记录
def findbyID(id):
    conn = connect.cnt()
    # 创建游标对象
    cursor = conn.cursor()
    # 执行查询语句
    query = "SELECT * FROM record where ID="+str(id)  # 替换为你的查询语句
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        return True
    else:
        return False
##通过id删除用户数据
def deletebyid(id):
    conn= connect.cnt()
    curses=conn.cursor()
    ##首先检测是否有该用户
    if(findbyID(id)):
        query='delete from record where ID='+str(id)
        curses.execute(query)
        curses.commit()
    query1='delete from users where ID='+str(id)
    curses.execute(query1)
    curses.commit()
    curses.execute(query1)
    curses.commit()
    curses.close()
    conn.close()
##根据users的id寻找并修改用户数据
def updatebyid(users):
    conn= connect.cnt()
    curses=conn.cursor()
    id=users.ID
    if findbyID(id):
        query='update users set Name=\''+users.name+'\''+'where ID=id'
        query1='update users set Password=\''+users.password+'\''+'where ID=id'
        curses.execute(query)
        curses.commit()
        curses.execute(query1)
        curses.commit()
        curses.close()
        conn.close()
        return True
    else:
        curses.close()
        conn.close()
        return False
##得到前五排行
def get_paihang():
    conn=connect.cnt()
    curses=conn.cursor()
    query='select top 5 * from users where MaxGrade is not NULL ORDER BY MaxGrade DESC'
    curses.execute(query)
    results=curses.fetchall()
    curses.close()
    conn.close()
    print(results)
    return results
##得到user成绩
def get_record(name):
    conn = connect.cnt()
    curses = conn.cursor()
    query = 'select Grade,Time from users join record on(users.ID=record.ID) where users.Name='+'\''+name+'\''+' order by Time DESC'
    print(query)
    curses.execute(query)
    results = curses.fetchall()
    curses.close()
    conn.close()
    print(results)
    return results
