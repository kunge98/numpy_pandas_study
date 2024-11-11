if __name__ == '__main__':
    # numpy中的统计函数
    import numpy as np
    t1 = np.array(range(12)).reshape(3,4)
    t1 = t1.astype(float)
    t1[1,2] = np.nan
    print('行计算','\n',np.sum(t1,axis=0))
    print('列计算','\n',np.sum(t1,axis=1))
    print('行均值','\n',t1.mean(axis=0))
    print('行中值','\n',np.median(t1,axis=0))
    print('最大值','\n',t1.max(axis=0))
    print('最大值','\n',t1.max(axis=1))
    print('最小值','\n',t1.min(axis=0))
    print('最小值','\n',t1.min(axis=1))
    print('极值','\n',np.ptp(t1,axis=0))
    print('极值','\n',np.ptp(t1,axis=1))
    print('极值','\n',np.ptp(t1))
    print('标准差','\n',t1.std(axis=0))



