if __name__ == '__main__':

    #对于这一组电影数据，如果我们希望统计电影分类(genre)的情况，应该如何处理数据？
    #解决思路：创建一个全为0的数组，对于出现的电影分类将它设置为1

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt

    df = pd.read_csv('./IMDB-Movie-Data.csv')
    df = pd.DataFrame(df)
    # print(df.head(1))

    temp_list = df['Genre'].str.split(',').tolist()    #列表嵌套列表的形式
    genre_list = list(set(i for j in temp_list for i in j))   #需要双重循环才可以把列表中的值展开

    #下面这句话的解读：创建一个全为0的DataFrame数组，
    #用到了np.zeros里面包含两个参数，设置行和列
    #df.shape[0]设置的是行数，返回的是df的行数
    #len(genre_list)设置的是列数，
    #columns=genre_list 根据电影的种类设置列名
    zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))),columns=genre_list)
    # print(zero_df)

    #给每个电影出现的位置赋值
    for i in range(df.shape[0]):
        zero_df.loc[i,temp_list[i]] = 1
    # print(zero_df.head(3))
    #统计电影出现次数的和
    genre_count = zero_df.sum(axis=0)
    # print(genre_count)
    #排序
    genre_count = genre_count.sort_values(ascending=False)
    # print(genre_count)
    plt.figure(figsize=(20,8),dpi=80)
    _x = genre_count.index
    _y = genre_count.values
    plt.bar(range(len(_x)),_y,width=0.4,color='orange')
    plt.xticks(range(len(_x)),_x)
    plt.xlabel('电影种类')
    plt.ylabel('数量')
    plt.title('电影分类数量条形图')
    plt.show()
