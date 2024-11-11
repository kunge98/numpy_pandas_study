import numpy as np

# numpy 100道题练习

# 3.创建1个长度为10的空向量
a03 = np.zeros(10)

# 4.如何找到任何一个数组的内存大小
a04 = np.zeros((10, 10))
# print(a04.size * a04.itemsize)

# 6.创建一个长度为10并且除了第五个值为1的空向量
a06 = np.zeros(10)
a06[4] = 1
# print(a06)

# 7.创建一个值域范围从10到49的向量
a07 = np.arange(10, 50) # 左闭右开
# print(a07)

# 8.反转一个向量（第一个变最后一个）
a08 = np.arange(10)
a08 = a08[::-1]
# print(a08)

# 9.创建一个3*3并且值从0-8的矩阵
a09 = np.arange(9) # 左闭右开
a09 = a09.reshape(3, 3)
# print(a09)

# 10.找到数组[1,2,0,0,4,0]中非0元素的位置索引
a10 = [1,2,0,0,4,0]
a10 = np.nonzero(a10)
# print(a10)

# 11.创建3*3单位矩阵
a11 = np.eye(3)
# print(a11)

# 12.创建3*3*3随机数组
a12 = np.random.random((3, 3, 3))
# print(a12)

# 13.创建10*10随机数组并找到最大最小值
a13 = np.random.random((10, 10))
# print(a13, np.max(a13), np.min(a13))

# 14.创建长度为30的随机向量并找到平均值
a14 = np.random.random(30)
print(a14, np.mean(a14))

# 15.创建二维数组，边界值为1，其余值为0
a15 = np.ones((10, 10))
a15[1:-1,1:-1] = 0
# print(a15)

# 16.对于一个存在的数组，如何添加一个用0填充的边界
a15 = np.ones((5, 5))
a15[1:-1,1:-1] = 0
# print(a15)

