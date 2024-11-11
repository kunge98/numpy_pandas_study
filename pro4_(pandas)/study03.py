if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import string

    #想知道使用次数最高的前几个名字是什么呢？（狗的名字）

    df = pd.read_csv('./dogNames2.csv')
    #排序
    df = df.sort_values(by='Count_AnimalName',ascending=False)
    print(df.head(10))
    print(df[:10])     #取前10行数据
    print(df['Row_Labels'])  #取完列之后变为一维数组Series
    print(df[:30]['Row_Labels'])    #取前30行数据列名字为Row_Labels的数据
    t1 = pd.DataFrame(np.array(range(12)).reshape(3,4),index=list('abc'),columns=list('1234'))
    print(t1)
    print(t1.loc['a',:])   #取行索引为a的一行
    print(t1.loc['a','3'])  #取索引为a的行数据且索引为3的列数据
    print(t1.loc[:,'3'])  #取列索引为3的一列
    print(t1.loc[['a','b'],['1','4']]) #取索引为a和b的行数据且索引为1和4的列数据
    print(t1.loc['a':'c',['1','4']])   #取索引从a到c的行数据且索引为1和4的列数据，注意a到c在numpy中不包含c，但是在loc方法中是包含的
    print(type(t1.loc['a','3']))
    t1 = t1.astype(int)
    t1.loc['a','1'] = 43
    print(t1)
    print(t1.iloc[:,2])
    print(t1.iloc[2,:])
    print(t1.iloc[2,1])  #从0开始，取第三行第二列数据
    print(t1.iloc[[2],[0,2]])
    print(t1.iloc[1:,:2])  #取第二行之后的且第三列之前的连续的数据
    #赋值
    t1.iloc[0, 0] = 76
    t1.iloc[0, 1] = np.nan
    print(t1)
    t2 = df[df['Count_AnimalName']>50]
    t3 = df[(df['Count_AnimalName']>50) & (df['Count_AnimalName']<100)]
    print(t2)
    print(t3)
    df = pd.DataFrame(df)
    print(df.head(10))


