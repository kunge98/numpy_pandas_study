if __name__ == '__main__':

    #接study11，想要统计中国和每个省份的店铺的数量(按照多个条件进行分组）

    import pandas as pd
    import numpy as np

    df = pd.read_csv('./starbucks_store_worldwide.csv')

    #数组按照多个条件进行分组返回一个Series
    group = df['Brand'].groupby(by=[df['Country'],df['State/Province']]).count()
    print(group)
    print(type(group))

    group1 = df[['Brand']].groupby(by=[df['Country'],df['State/Province']]).count()
    group2 = df.groupby(by=[df['Country'],df['State/Province']])['Brand'].count()
    group3 = df.groupby(by=[df['Country'],df['State/Province']]).count()[['Brand']]

    # 三种写法一样的效果

    print(group1,type(group1))
    print('*'*100)
    print(group2,type(group2))
    print('*'*100)
    print('*'*100)
    print(group3,type(group3))

