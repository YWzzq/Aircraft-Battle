import tkinter.messagebox
from  tkinter import *
from PIL import Image, ImageTk
import random
from userservice import Login
class ZhuceJiemian:
    def creatAuthCode(self):
        res1 = ""
        res2 = ""
        res3 = ""
        for i in range(2):
            num = random.randint(0, 9)
            res1 += str(num)
            num = random.randint(65, 91)
            res2 += str(chr(num))
            num = random.randint(97, 123)
            res3 += str(chr(num))
        string = str(res1 + res2 + res3)
        self.codestr['text']=string
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

        # 设置用户密码确定输入框
        self.confirm_password = Label(self.root, text="确认密码:")
        self.confirm_password.place(relx=0.28, rely=0.5, anchor=CENTER)
        self.text3 = Entry(self.root)
        self.text3.place(relx=0.5, rely=0.5, anchor=CENTER, width=150, height=25)

        # 设置验证码输入框
        self.code_label = Label(self.root, text="验证码:")
        self.code_label.place(relx=0.3, rely=0.6, anchor=CENTER)
        self.code_entry = Entry(self.root)
        self.code_entry.place(relx=0.42, rely=0.6, anchor=CENTER, width=60, height=25)

        # 设置获取验证码的按钮
        self.codestr = Button(self.root, text='获取验证码', command=self.creatAuthCode, fg="red", bg="blue")
        self.codestr.place(relx=0.57, rely=0.6, anchor=CENTER)

        # 设置游戏名
        self.game_name = Label(self.root, text="飞机大战", font=("微软雅黑", 30))
        self.game_name.place(relx=0.5, rely=0.1, anchor=CENTER)

        # 创建注册按钮
        self.register_button = Button(self.root, text="注册", font=("微软雅黑", 12),command=self.register_handler)
        self.register_button.place(relx=0.45, rely=0.8, anchor=CENTER)



    def start_register(self):
        self.root.mainloop()
    def register_handler(self):
        name=self.text1.get()
        password1=self.text2.get()
        print(password1)
        password2=self.text3.get()
        yan=self.code_entry.get()
        yan1=self.codestr['text']
        try:
            Login.register(name,password1,password2,yan,yan1)
        except Exception as ex:
            tkinter.messagebox.showinfo('提示',str(ex))
        else:
            self.root.destroy()
            tkinter.messagebox.showinfo('提示','注册成功')
