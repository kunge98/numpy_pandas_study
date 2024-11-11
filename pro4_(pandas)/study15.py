if __name__ == '__main__':

    #问题：使用matplotlib呈现出店铺总数排名前10的国家

    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np

    df = pd.read_csv('./starbucks_store_worldwide.csv')

    #先对df通过country分组，获取数量，取值’brand‘,通过降序排序，取前10个数据
    data1 = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]

    _x = data1.index
    _y = data1.values
    plt.figure(figsize=(20,8),dpi=80)
    plt.bar(range(len(_x)),_y)
    plt.xticks(range(len(_x)),_x)
    plt.show()
