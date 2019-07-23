# coding: utf-8
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入os模块，用来执行宿主机命令
import os
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建style对象，用来管理ttk组件样式
        style = ttk.Style()
        style.configure("fkit.TPanedwindow", background="darkgray", relief=RAISED)
        pwindow = ttk.Panedwindow(self.master,
            orient=VERTICAL, style="fkit.TPanedwindow")
        pwindow.pack(fill=BOTH, expand=1)
    	# 创建Panedwindow组件，通过style属性设置分割线
        self.first = Label(pwindow, text="hello world", height=2, font=('Verdana',10), fg='green')
    	# 调用add方法添加组件，每个组件占一个区域
        pwindow.add(self.first)
        # 创建button按钮
        okBn = Button(pwindow, text="on", width=30, height=2, bg='pink', fg='black',
            command=self.open_on  # 点击按钮调用self.open_on实例
            )
        okBn2 = Button(pwindow, text="off", width=30, height=2, bg='pink', fg='black',
            command=self.open_off  
            )
        okBn3 = Button(pwindow, text="reboot", width=30, height=2, bg='pink', fg='black',
            command=self.open_reboot  
            )
        okBn4 = Button(pwindow, text="Enter", width=30, height=2, bg='pink', fg='black',
            command=self.open_enter  
            )
        # 调用add方法加入这些button
        pwindow.add(okBn)
        pwindow.add(okBn2)
        pwindow.add(okBn3)
        pwindow.add(okBn4)
    def files(self,str):
    	hi = open("test.txt","w")
    	hi.write( str )
    	hi.close()
    	self.first['text']='已写入内容：'+str
    def open_on(self):
        str = "on"
        self.files(str)
        return 0
    def open_off(self):
        str = "off"
        self.files(str)
        return 0
    def open_reboot(self):
        str = "reboot"
        self.files(str)
        return 0
    def open_enter(self):
        # 传送本地文件到远程服务器
        os.system('scp -P 198 test.txt root@107.172.122.190:/data')
        self.first['text']='传输结果：成功'
        return 0
root = Tk()
root.title("服务器间文件传输")
App(root)
root.mainloop()