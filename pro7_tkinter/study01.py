#

from tkinter import *
from tkinter import messagebox


root = Tk()

# 定义窗口的名称
root.title('这是我的第一个GUI界面')

# 定义窗口在整个屏幕的位置
# 里面传递的参数包括：窗口的大小、水平的距离、垂直的距离
# 500x300表示界面窗口的大小
# +100表示距离左边100个像素
# -200表示距离距离下面200个像素
root.geometry('500x300+500-100')

# 创建一个按钮对象
btn01 = Button(root)
btn01['text'] = '点我一下,送花'

# 布局管理器 pack，place，grid
# 把按钮放在可视化窗口上
btn01.pack()


# 送花函数
def songhua(e):
    # e表示事件对象
    messagebox.showinfo('Message', '送你一朵小红花')
    print('送花成功！')


# 绑定事件
btn01.bind('<Button-1>',songhua)

root.mainloop()

