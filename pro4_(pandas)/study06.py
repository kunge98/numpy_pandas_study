if __name__ == '__main__':

    #如果我们想rating，runtime的分布情况，应该如何呈现数据？直方图

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt

    df = pd.read_csv('./IMDB-Movie-Data.csv')
    df = pd.DataFrame(df)
    # print(df.info())

    #电影时长
    runtime_data = df['Runtime (Minutes)'].values

    max_runtime = runtime_data.max()
    min_runtime = runtime_data.min()

    d = 5

    num_bin = (max_runtime-min_runtime) // d
    plt.figure(figsize=(20,8),dpi=80)
    plt.xticks(range(min_runtime,max_runtime+5,5))
    plt.hist(runtime_data,num_bin)
    plt.show()

    #电影评分

    # ration_data = df["Rating"].values
    #
    # max_rating = ration_data.max()
    # min_rating = ration_data.min()
    # print(max_rating - min_rating)
    #
    # num_bin = (max_rating- min_rating) // 0.5
    #
    # plt.figure(figsize=(20, 8), dpi=80)
    # plt.hist(ration_data, num_bin)
    # _x = [min_rating]
    # i = min_rating
    # while i <= max_rating + 0.5:
    #     i = i + 0.5
    #     _x.append(i)
    # plt.xticks(_x)
    # plt.show()

