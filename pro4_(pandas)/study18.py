if __name__ == '__main__':

    #不同年份书的平均评分情况

    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np

    df = pd.read_csv('./books.csv')
    # print(df.info())

    #找到df中不为空的出版年份
    data = df[pd.notnull(df['original_publication_year'])]

    #对data按照出版年份进行分组，并取出‘average_rating’该列的数据,求平均值
    data = data.groupby(by=data['original_publication_year'])['average_rating'].mean()
    # print(data)

    _x = data.index.astype(int)
    _y = data.values
    plt.figure(figsize=(20,8),dpi=80)
    plt.xticks(list(range(len(_x)))[::10],_x[::10],rotation=45)
    plt.plot(range(len(_x)),_y)
    plt.show()

