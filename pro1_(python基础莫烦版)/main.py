# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('wzk')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#1.输出，输出的格式不用字符串加上加号，直接用逗号代替，java已经哭晕在厕所
# print(2)
# print('李欣芮大傻逼')
# print('读研期间发愤图强')
# print(1+2)
# print(3*2)
# print(2**2)
# print(3**2**2)   #  平方为两个星号 **
# print(9%1)
# print(5//3)
#print("c的数值是:",c,"a的数值是",a,"b的数值是",b)


#2.while判断
# break 和continue的用法和c、java用法一致
# condition = 1
# apple = 200
# while condition < 10:
#     print(condition)
#     condition = condition +1
# while apple > 0:
#     print("真厉害"+str(apple))
#     apple = apple - 1

#3.for循环
# example_list = [23,4,'lxr',6,'人工智能',8,9,"王增坤"]
# for i in example_list:
#     print(i)

#4.if判断
# x=3
# y=3
# z=4
# if x<y<z:   #判断写法很智能
#     print("x比y小而且y比z小")
# else:
#     print("x和y相等")
#和其他语言一样在if判断之中只要是满足条件就会终止判断
# x=0
# if x>1:
#     print("x>1")
# elif x<-1:
#     print("x<-1")
# else:
#     print("x在-1和1之间")


#5.def函数,函数的作用范围只是向下数四行，前面必须有空格的那种
# a=5
# def function(a,b):
#     print("函数调用")
#     a=4
#     c=a*b
#     print("c的数值是:",c,"a的数值是",a,"b的数值是",b)
#function(a,b=3)

#6.全局变量，局部变量,可以设置某个变量为global即可设置为全局变量

#7.文件的读写
#创建文件可以用open的方式，第一个参数是文件名字，第二个参数设置选择可以使w读 r写 a(append)补充追加内容，
#每一次读写完文件之后要close一下

# my_file = open('myFileTest','w')
# my_file.write("this is a test context \n i like you just like you!  \n i just kidding")
# my_file.close()

# my_file = open('myFileTest','a')
# my_file.write("\nthis is appeded context")
# my_file.close()

# my_file = open("myFileTest","r")
# print(my_file.read())
# cont = my_file.readline()
# print(cont)

#8.class类
#类的定义和创建对象比java要简单。里面也是可以创建变量和函数（属性和动作），这个和java一样。
# 右键初始化函数init类似于java的构造函数，其中self和java中的this一模一样

# class Person:
#
#     def __init__(self):
#         self.name = 'lxr'
#         self.age = 18
#         self.sex = '女'
#         self.address = '地球村'
#
#     name = '王增坤'
#     age = 18
#     sex = '男'
#     address = '山东省临沂市沂水县'
#     def info(self,name,age,sex,address):
#         print("姓名是：",name,"年龄是：",age,"性别：",sex,"家庭住址是：",address)
#
# people = Person()  #创建一个person对象
# print(people.info('wzk',17,'男','山东省临沂市沂水县'))


#9.input 返回值是一个string类型的。如果以后用于判断用户输入的内容需要转换类型。
# 类似于java中的scanner类，可以在控制台输入字符

# print("亲输入一个字符")
# a_input = input()
# print("您输入的字符时",a_input)

#10.元组和列表.其中tuple可以用括号也可以省略。list使用中括号
# a_tuple = (13,4,8,5,4,0)
# a_tuple = 1,3,8,4,6,4,45
# a_list = [67,0,8,9,4,6,0]
# a_list.append(857)    #在list的最后面添加数据
# a_list.insert(0,66666)  #1.索引的位置  2.在索引的地方添加数据
# a_list.remove(4)   #删除的数值
# print(a_list[len(a_list)-1])    #打印list的最后一个数
# print(a_list[-1])               #打印list的最后一个数，所以在python中直接使用-1 代替 len(a_list)-1
# print(a_list[0:4])    #打印索引在0-3之间的数值（左闭右开的区间）
# print(a_list[-3:])    #打印从后向前数到第三个的数（从后面数索引就是从1开始）
# print(a_list.index(857))   #打印list中某个数值的索引，第一次出现的位置
# print(a_list.count(0))    #计算list中出现0的次数
# print(a_list.sort())     #对list进行从小到大的排序（默认）
# print(a_list)
# print(a_list.sort(reverse=0))     #设置reverse=一个非0的数字或者True都是可以的 对list进行从大到小的排序
# print(a_list)
# for index in range(len(a_list)):
#     print("index的序号是", index, "a_list的数值是", a_list[index])
# for index in range(len(a_tuple)):
#     print("index的序号是",index,"a_tuple的数值是",a_tuple[index])


#11.字典.字典存储的形式类似于键值对儿，一个关键词对应一个数值。字典中还可以嵌套字典，或者是定义函数都可以

# def add(x,y):
#     return x + y
#
# dict = { 'apple':'expensive',
#          'banana':'delicious',
#          'pear':'sweet',
#          'vegetables':'healthy',
#          'add()':add(x=2,y=3)
#          }
# print(dict['apple'])
# del dict['vegetables']   #删除字典中的元素
# print(dict)
# dict['watermelon'] = 'water'   #向字典中添加元素
# print(dict)

#12.import载入  名字过长用as起一个别名
#导入自己的模块这个和java中创建实体类和业务层调用对象类似
# import time as t
# print(t.localtime())
# print(t.time())
# import test
# people = test.Person()      #调用test中的Person类
# print(people.name,people.age)

#13   异常抛出快捷键  ctrl + Alt + T
# try:
#     file = open('error','r')
# except Exception as e:
#     print(e)

#14.  zip功能强大可以将多个list放在一起，联想英文单词zip拉链
# a=[7,5,3,4]
# b=[3,4,6,7]
# print(zip(a,b))
# print(list(zip(a,a,b,b)))
# for i,j in zip(a,b):
#     print(i/j,i*j)

#15. lambda,用处不大只是简化了函数的写法，用在复杂逻辑的函数上会很鸡肋
# def fun1(x,y):
#     return x+y
# fun2 = lambda x,y :x+y
# print(fun1(2,3))
# print(fun2(2,3))

#16. map。参数的数量根据调用的函数的参数数量而定。
#  调用的fun1中有6个参数，所以这时必须要有6组数据将每组数据的第一个元素相加，每组数据的第二个元素相加。
#  次数想要实现加减运算，将map对象转为list集合
# fun1 = lambda x,y,u,v,w,z :x+y+u+v+w+z
# fun2 = lambda x,y:x+y
# print(list(map(fun1,[2,3],[5,6],[23,1],[0,87],[3,4],[2,6])))
# print(list(map(fun2,[2,3],[5,6])))


#17. copy与deepcopy
import copy
# 例子1，简单的引用内存地址和实际的数值都是共用的
# a = [1,2,3]
# b = a
# print(b[0])
# print(a[0])
# print(id(a))
# print(id(b))
# print(id(b) == id(a))
# a[2] = 888
# print(b[2])

# 例子2   copy.copy()
# c = copy.copy(a)
# print(id(a)==id(c)) #输出为false，说明copy只是复制了列表的数值，内存地址没有复制
# print(c)  #输出的列表数值和a的一样
# print(c[2])
# c[2] = 666  #改变c的数值并不会影响a的数值
# print(a[2])  #并没有改变a[2]的数值
# f = [1,2,3,[4,5,6]]  #f定义了两层列表如果对它进行copy复制，那么只能复制第一层列表的内容
# g = copy.copy(f)
# print(g[3][0] == f[3][0])
# print(id(g[3][0]) == id(f[3][0]))
# print(id(g) == id(f))  #输出为false ，只能复制第一层列表的内容

#例子3   copy.deepcopy（）  完全copy过来内存空间也会不一样
# e = copy.deepcopy(a)
# print(id(a[0]) == id(e[0]))
# print(a[0] == e[0])
#  总结： （1） b = a 时共有一个内存空间。干啥都用一个
#  （2） copy.copy() 打包带走第一层的数据，第二层的数据还是公用
#  （3） copy.deepcopy() 把所有的数据都打包带走

#18. pickle（对象序列化模块）(读写文件)
#pickle适合一些不大的python对象，对于较大的python，pickle模块就显得有点吃力
# import pickle
# a_dict1 = {'A':857,
#           'B':123,
#           'C':{'D':dict}}
# my_file = open('pickle_example.pickle','wb')
# pickle.dump(a_dict1,my_file)   #dump可以将字典对象转化为字符串存放在my_file中
# my_file.close()
#
# my_file1 = open('pickle_example.pickle','rb')
# print(pickle.load(my_file1))  #加载文件的内容
# my_file.close()
#
# with open('pickle_example.pickle','rb') as my_file:
#     a_dict2 = pickle.load(my_file)
#     print(a_dict2)

#19. set找不同
# chae_list = ['a','b','b','c','c','c','d','d','d']
# print(set(chae_list))   #将重复的内容都删除掉
# print(type(set(chae_list)))   #输出的是set类型（乱序）
# sentence = 'welcome back home'
# print(set(sentence))  #空格部分也会保留下来
# after1 = sentence.__add__('W')
# print(set(after1))
# after2 = sentence.removeprefix('wel')
# print(set(after2))

#20. 正则表达式
import re

#21. 多线程
# join的功能的就是会等待所有的程序都执行完才去执行之后的语句！
# lock锁
# import threading
# from queue import Queue

# def thread_job():
#     print('this is a added thread ')
#
# def thread():
#     added_thread = threading.Thread(target = thread_job())
#     added_thread.start()   #启动这个线程
#     print(threading.active_count())  #计算当前的线程数量
#     print(threading.enumerate())  #查看线程
#     print(threading.current_thread())   #查看当前运行的线程
#
# if __name__ == '__main__':
#     thread()

#22. tkinter  是一个可视化窗口UI
import tkinter as tk
window = tk.Tk()
window.title('my_Windows')   #窗口标题
window.geometry('500x500')   #窗口大小

#Label和Button标签和按钮
# var = tk.StringVar()
# a1=tk.Label(window,textvariable=var,bg='red',font=('Arial',12),width=15)
# onclick = False
# def hit_me():
#     global onclick
#     if onclick == False:
#         onclick = True
#         var.set('you hit me')
#     else:
#         var.set('you cancled')
#         onclick = False
# button = tk.Button(window,text='hit me!',bg='blue',width='19',command=hit_me)
# a1.pack()
# button.pack()

#Entry和Text输入文本框
# entry = tk.Entry(window,show='')
# def insert_point():
#     var=entry.get()
#     text.insert('insert',var)
# def insert_end():
#     var.get()
#     text.insert('end',var)
# button1=tk.Button(window,text='insert point',width=18,command=insert_point)
# button2=tk.Button(window,text='insert end',width=18,command=insert_end)
# text=tk.Text(window,height=2)
# entry.pack()
# button1.pack()
# button2.pack()
# text.pack()

#Listbox列表部件
# var1=tk.StringVar()
# var2=tk.StringVar()
# var2.set((11,22,33,44))
# a2=tk.Label(window,textvariable=var1,bg='yellow',font=('Arial',12),width=4)
# listbox=tk.Listbox(window,listvariable=var2)
# list_items=[1,2,3,4]
# for item in list_items:
#     listbox.insert('end',item)
# listbox.insert(1,'first')
# def print_selection():
#     value=listbox.get(listbox.curselection())
#     var1.set(value)
# button3=tk.Button(window,text='print selection',width=18,command=print_selection)
# a2.pack()
# listbox.pack()
# button3.pack()

#radiobutton  单选按钮
# var3=tk.StringVar()
# a3=tk.Label(window,bg='yellow',width=40,text='empty')
# def print_selection1():
#     a3.config(text='you have selected Option'+var3.get())
# radiobutton1=tk.Radiobutton(window,text='Option A',variable=var3,value='A',command=print_selection1)
# radiobutton2=tk.Radiobutton(window,text='Option B',variable=var3,value='B',command=print_selection1)
# radiobutton3=tk.Radiobutton(window,text='Option C',variable=var3,value='C',command=print_selection1)
# a3.pack()
# radiobutton1.pack()
# radiobutton2.pack()
# radiobutton3.pack()

#checkbutton
# a4=tk.Label(window,bg='orange',width=40,text='empty')
# var4=tk.IntVar()
# var5=tk.IntVar()
# def print_selection2():
#     if(var4.get()==1)&(var5.get()==0):
#         a4.config(text='I only Python')
#     if(var4.get()==0)&(var5.get()==1):
#         a4.config(text='I only Java')
#     if(var4.get()==0)&(var5.get()==0):
#         a4.config(text='I love neither')
#     if(var4.get()==1)&(var5.get()==1):
#         a4.config(text='I love both')
# checkbutton1=tk.Checkbutton(window,text='Python',variable=var4,
#                             onvalue=1,offvalue=0,command=print_selection2)
# checkbutton2=tk.Checkbutton(window,text='Java',variable=var5,
#                             onvalue=1,offvalue=0,command=print_selection2)
# a4.pack()
# checkbutton1.pack()
# checkbutton2.pack()

#scale 尺度
# a5=tk.Label(window,bg='pink',width=40,text='empty')
# def print_selection3(v):
#     a5.config(text='you have selected'+v)
# scale = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,length=200,
#                  showvalue=1, tickinterval=2, resolution=0.1, command=print_selection3)
# a5.pack()
# scale.pack()

#canvas 画布
# canvas=tk.Canvas(window,bg='blue',height=200,width=200)
# x0,y0,x1,y1=50,50,80,80
# line=canvas.create_line(x0,y0,x1,y1)   #画一条直线
# oval=canvas.create_oval(x0,y0,x1,y1,fill='red')   #画一个圆
# arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=90)    #画一个半圆
# rect=canvas.create_rectangle(100,30,120,50)    #画一个正方形
# def move():
#     canvas.move(rect,3,2)
# button4=tk.Button(window,text='move',command=move)
# canvas.pack()
# button4.pack()

#frame
# frame = tk.Frame(window)
# frame_l = tk.Frame(frame)
# frame_r = tk.Frame(frame)
# frame_l.pack(side='left')
# frame_r.pack(side='right')
# tk.Label(frame_l, text="左上", bg="pink").pack()
# tk.Label(frame_l, text="左下", bg="blue").pack()
# tk.Label(frame_r, text="右上", bg="green").pack()
# tk.Label(frame_r, text="右下", bg="purple").pack()
# frame.pack()


#menubar 菜单  看不懂
# a6=tk.Label(window,bg='pink')
# menubar=tk.Menu(window)
# file=tk.Menu(menubar,tearoff=0)
# counter=0
# def do_job():
#     global counter
#     a6.config(text='do'+str(counter))
#     counter+=1
# menubar.add_cascade(label='file',menu=filemenu)
# filemenu.add_command(label='New',command=do_job)
# filemenu.add_seporator()
# a6.pack()

#messagebox弹窗   相当于js中的alert弹窗
# import tkinter.messagebox
# def hit_me():
#     tk.messagebox.showinfo(title='Hi,',message='你点我了')
#     tk.messagebox.showerror(title='Hi,',message='知错能改')
#     tk.messagebox.showwarning(title='Hi,',message='我劝耗子尾汁！')
#     tk.messagebox.askquestion(title='Hi,', message='你点我了')   #返回值是yes、no
#     tk.messagebox.askyesno(title='Hi,', message='你点我了')   #返回值是true/false
#     tk.messagebox.askokcancel(title='Hi,', message='你点我了')   #返回值是true/false
#     tk.messagebox.askretrycancel(title='Hi,', message='你点我了')   #返回值是true/false
# tk.Button(window,text='hit me',command=hit_me).pack()

#pack grid place 位置放置  和css非常相似
#方式一
# a7=tk.Label(window,bg='pink',width=10).pack(side='top')
# a7=tk.Label(window,bg='pink',width=10).pack(side='bottom')
# a7=tk.Label(window,bg='pink',width=10).pack(side='left')
# a7=tk.Label(window,bg='pink',width=10).pack(side='right')
#方式二
# for i in range(4):
#     for j in range(3):
#         tk.Label(window,bg='yellow',text='6').grid(row=i,column=j,padx=10,pady=10)
#方式三(放置位置很精准)
# tk.Label(window,text=6,bg='yellow').place(x=100,y=100)
window.mainloop()
