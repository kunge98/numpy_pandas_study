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
        self.btn01 = Button(self)
        self.btn01['text'] = '点击送花'
        self.btn01.pack()
        self.btn01['command'] = self.songhua

    # 送花
    def songhua(self):
        messagebox.showinfo('送花','送你99朵玫瑰')

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