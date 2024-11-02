import pyodbc
##函数返回连接对象
def cnt():
    # 连接参数
    server = 'LAPTOP-ICT3T44U'  # 服务器名称或地址
    user = 'sa'  # 用户名
    password = 'yang030709'  # 密码
    database = 'airplane'  # 数据库名称

    # 创建连接字符串
    connection_string = (
            r'DRIVER={ODBC Driver 17 for SQL Server};'r'SERVER=' + server + ';'r'DATABASE=' + database + ';'r'UID=' + user + ';'r'PWD=' + password + ';')

    # 建立连接
    conn = pyodbc.connect(connection_string)
    return conn
