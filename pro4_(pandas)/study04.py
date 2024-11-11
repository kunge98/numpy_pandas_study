if __name__ == '__main__':

    #对缺失数据的处理

    import pandas as pd
    import numpy as np

    t1 = pd.DataFrame(np.array(range(12)).reshape(3,4),index=list('XYZ'),columns=list('abcd'))
    t1.astype(float)
    t1.iloc[1,1] = np.nan
    print(t1)
    # print(pd.isnull(t1))
    # print(pd.notnull(t1))
    print(t1.dropna(axis=0,how='all'))
    print(t1.dropna(axis=0,how='any'))
    print(t1.dropna(axis=1,how='any'))
    t2 = t1.fillna(666)
    t3 = t1.fillna(t1.mean)
    print(t2)
    print(t3)
    print(t1.mean())