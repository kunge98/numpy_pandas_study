if __name__ == '__main__':
    #numpy--数组array
    import numpy as np
    import random
    t1 = np.array([1,2,3],dtype='int64')
    t2 = np.array(range(10))
    t3 = np.arange(10)
    print(t1)
    print(type(t1))  # t1的类型---- numpy.ndarray
    print(t1.dtype)  # 当前存放数据的类型
    print(t2)
    print(t3)
    t4 = np.array([1,2,3,4],dtype=float)
    print(t4.dtype)  # 当前存放数据的类型
    t5 = np.array([1,1,0,1,0,0,1,0,1],dtype=bool)
    print(t5.dtype)  # 当前存放数据的类型
    t6 = t5.astype('int8')  #更改数据的类型
    print('t6的数值是',t6)
    print(type(t6))
    t7 = np.array([random.random() for i in range(10)])  #在10的范围内循环取随机数
    print(t7)
    t8 = np.round(t7,2)   #参数1：操作的对象，参数2：保留小数的位数
    print(t8)

    t9 = np.array(range(12)).reshape(3,4)
    print(t9.shape[1])
    print(t9.shape[0])

