if __name__ == '__main__':
    import numpy as np
    t1 = np.array([1,2,3,4,5,6,7,7,8,9,10,11,12])  #一维数组
    print(t1.shape)   #输出的shape有几个参数就是几维数组
    t2 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])  #二维数组
    print(t2.shape)
    t3 = np.array([[[1,2,3],[4,5,6]],
                   [[7,8,9],[10,11,12]]])   #三维数组
    print(t3.shape)
    t4 = np.arange(12).reshape(3,4)
    print('t4数组为','\n',t4)
    t5 = np.arange(24).reshape(2,3,4)
    # t5 = np.arange(24).reshape(4,6)    转变为一个二维数组
    # t5 = np.arange(24).reshape(24,)    转变为一个一维数组
    print('t5数组为','\n',t5)

    t6 = np.array([[1,2],[3,4],[5,6]])
    t6.flatten('A')
    print('t6的数组为','\n',t6)
