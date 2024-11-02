import tkinter.messagebox
from PIL import Image, ImageTk
from Register import ZhuceJiemian
from userservice import Login
from Register import *
from Gameservice import Start
class DengluJiemian:
    def __init__(self):
        self.root = Tk()
        self.root.title("飞机大战")
        self.root.geometry("500x400+500+200")

        # 设置背景图片
        image = Image.open("E:\\桌面\\pic1\\2.png")
        photo = ImageTk.PhotoImage(image)
        label = Label(self.root, image=photo)
        label.image = photo  # 保持对图片对象的引用
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # 设置用户账号输入框
        self.ID = Label(self.root, text="账号:")
        self.ID.place(relx=0.3, rely=0.3, anchor=CENTER)
        self.text1 = Entry(self.root)
        self.text1.place(relx=0.5, rely=0.3, anchor=CENTER, width=150, height=25)

        # 设置用户密码输入框
        self.password = Label(self.root, text="密码:")
        self.password.place(relx=0.3, rely=0.4, anchor=CENTER)
        self.text2 = Entry(self.root)
        self.text2.place(relx=0.5, rely=0.4, anchor=CENTER, width=150, height=25)

        # 设置游戏名
        self.code = Label(self.root, text="飞机大战", font=("微软雅黑", 30))
        self.code.place(relx=0.5, rely=0.1, anchor=CENTER)

        # 创建登录按钮
        self.login_button = Button(self.root, text="登录", font=("微软雅黑", 12),command=self.login)
        self.login_button.place(relx=0.25, rely=0.65, anchor=CENTER)

        # 创建注册按钮
        self.register_button = Button(self.root, text="注册", font=("微软雅黑", 12),command=self.inregister)
        self.register_button.place(relx=0.45, rely=0.65, anchor=CENTER)

        # 创建试玩按钮
        self.play_button = Button(self.root, text="游客登录", font=("微软雅黑", 12),command=self.startgame)
        self.play_button.place(relx=0.7, rely=0.65, anchor=CENTER)

    def login(self):
        name=self.text1.get()
        password=self.text2.get()
        try:
            Login.user_login(name,password)
        except Exception as ex:
            tkinter.messagebox.showinfo('提示',str(ex))
        else:
            tkinter.messagebox.showinfo('提示', '登录成功')
            ##startgame
            self.startgame(name)

    def inregister(self):
        self.root.destroy()
        ZhuceJiemian().start_register()
        DengluJiemian().start_login()

    def startgame(self,name='youke'):
        self.root.destroy()
        Start.Startgame(name).start_game()

    def start_login(self):
        self.root.mainloop()
    #试玩
DengluJiemian().start_login()
