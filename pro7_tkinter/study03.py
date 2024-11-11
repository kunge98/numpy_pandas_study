# 面向对象方式创建GUI

from tkinter import *
from tkinter import messagebox


# 继承自frame
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createwidget()
        self.quit()

    def createwidget(self):
        # 显示label和字体
        self.label01 = Label(self,
                             text='第一个label',
                             width=10,
                             height=2,
                             bg='red',
                             fg='green')
        self.label01.pack()
        self.label02 = Label(self,
                             text='什么程序猿？',
                             width=30,
                             height=3,
                             bg='black',
                             fg='white',
                             font=('黑体',30))
        self.label02.pack()
        # 显示图像,设置为全局变量，不让随着循环局部变量会被销毁
        # 设置的图像只能是gif格式
        # global photo
        # photo = PhotoImage(file='./.gif')
        # self.label03 = Label(self,image=photo)
        # self.label03.pack()

        # 多行文本
        self.label04 = Label(self,
                             text='啦啦啦啦啦啦啦\n哈哈啊哈哈哈哈\n除了你函数的飞牛网\n',
                             borderwidth=1,
                             relief='solid',
                             justify='right')
        self.label04.pack()


    # 退出
    def quit(self):
        self.btnQuit = Button(self, text='退出', command=root.destroy)
        self.btnQuit.pack()

if __name__ == '__main__':

    root = Tk()
    root.title('一个经典的写法')
    root.geometry('400x300+200+200')
    app = Application(master=root)
    root.mainloop()