if __name__ == '__main__':

    #问题：有全球排名靠前的10000本书的数据，那么请统计一下，不同年份书的数量

    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np

    df = pd.read_csv('./books.csv')
    # print(df.head(1))

    #查看信息发现年份那一列有的信息不全
    data = df[pd.notnull(df['original_publication_year'])]
    group = data.groupby(by='original_publication_year')['title'].count()

    _x = (group.index).astype(int)
    _y = group.values
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(_x)),_y)
    plt.xticks(list(range(len(_x)))[::20],_x[::20],rotation=45)
    plt.xlabel('年份')
    plt.ylabel('数量')
    plt.title('不同年份出版书籍的数量')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
