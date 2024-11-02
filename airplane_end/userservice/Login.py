from DATABASE import database
import re

##事务处理调用函数
##根据返回值弹出不同页面

##1表示用户名为空，2表示密码未输入，3表示用户名不存在，4表示密码错误,0表示登录成功
def user_login(name,password):
    if (name == ''):
        raise Exception('请输入用户名')
    elif password == '':
        raise Exception('请输入密码')
    user = database.findbyName(name)
    if user:
        print(user.password,password)
        if user.password == password:
            return
        else:
            raise Exception('密码错误')
    else:
        raise Exception('用户名不存在')
##注册
##1.非空检查，检验数据合法性
##2.检测密码相同
##3.写入数据库
def register(name,password1,password2,yan,yan1):
    if name=='':
        raise  Exception('请输入用户名')
    else:
        ##用户名规则
        pattern=r'[a-z]{3,5}_[0-9]{3,5}'
        if re.match(pattern,name):
            if password2 and password1:
                if len(password1)>=6 and len(password1)<=10 and len(password2)>=6 and len(password2)<=10:
                    if password2==password1:
                        if yan=='':
                            raise Exception('请输入验证码')
                        elif yan!=yan1:
                            print(yan,yan1)
                            raise  Exception('验证码错误')
                        else:
                            database.addtousers(database.user.User(name, password1))

                    else:
                        raise  Exception('两次密码输入不一致')
                else:
                    raise  Exception('密码长度为6-10字符')
            else:
                raise  Exception('请输入密码')
        else:
            raise  Exception('用户名由3至5位字母+_+3至5位数字组成')

