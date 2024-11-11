if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import string
    df = pd.read_csv('./dogNames2.csv')
    print(df)
    t1 = pd.DataFrame(np.array(range(12)).reshape(3,4))
    print(t1)
    t2 = pd.DataFrame(np.array(range(12)).reshape(3,4),index=list('abc'),columns=list('WXYZ'))
    print(t2)
    t3 = pd.DataFrame(np.array(range(12)).reshape(3,4),
                      index=list(string.ascii_uppercase[:3]),
                      columns=list(string.ascii_lowercase[-4:]))
    print(t3)
    d1 = {'姓名':['王增坤','wwy'],'性别':['男','男'],'年龄':['22','23'],'国籍':['中国','中国']}
    t4 = pd.DataFrame(d1)
    print(t4)
    d2 = [{'name':'WZK','age':'22','tel':'153'},
          {'name':'WWY','age':'','tel':'157'},
          {'name':'','age':'22','tel':'139'},
          {'name':'LZH','age':'','tel':'183'}]
    print(pd.DataFrame(d2))
    df = np.array(range(24)).reshape(4,6)
    df = pd.DataFrame(df)
    print('df为',df)
    print(df.index)         #数组的行
    print(df.columns)       #数组的列
    print(df.shape)         #数组的形状
    print(df.ndim)          #数据维度
    print(df.dtypes)        #列数据类型
    print(df.values)        #输出对象的值，二维的ndarray数组
    print(df.head(2))       #显示头部几行，默认是5
    print(df.tail(1))       #显示尾部几行，默认是5
    print(df.info())        #展示df的概览包括
    print(df.describe())    #快速综合统计结果：计数、均值、标准差、最大值、四分位数、最小值（更适合数值型数组）




