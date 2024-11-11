if __name__ == '__main__':

    # 复合索引  ----   赋值

    import pandas as pd
    import numpy as np

    df1 = pd.DataFrame(np.array(range(12)).reshape(3,4),index=list('123'))
    # 给索引普通赋值
    # df1.index = ['X','Y','Z']
    # 将原先的索引更换为当前的索引，如果有对应的索引值，则输出，没有对应的新的索引填充为NaN
    # df1 = df1.reindex(['2','3','4'])


    df2 = pd.DataFrame({'Country': ['China', 'China', 'India', 'India', 'America', 'Japan', 'China', 'India'],
                       'Income': [10000, 10000, 5000, 5002, 40000, 50000, 8000, 5000],
                       'Age': [50, 43, 34, 40, 25, 25, 45, 32]})
    # 使用Country作为索引,
    # drop删除用作新索引的那一列，默认是true删除的,设置为false该列照常出现
    # append是否将列附加到现有索引，默认为False
    df2 = df2.set_index('Country',drop=True,append=True)
    print(df2)


