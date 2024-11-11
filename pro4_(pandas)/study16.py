if __name__ == '__main__':

    #使用matplotlib呈现出中国每个城市的店铺数量

    from matplotlib import pyplot as plt
    import pandas as pd
    import numpy as np

    df = pd.read_csv('./starbucks_store_worldwide.csv')
    # print(df.info())

    df = df[df['Country']=='CN']
    #先对df通过country分组，获取数量，取值’brand‘,通过降序排序，数据太多所以只取了前30个数据
    data1 = df.groupby(by='City')['Brand'].count().sort_values(ascending=False)[:30]

    _x = data1.index
    _y = data1.values

    plt.figure(figsize=(30,8),dpi=80)
    plt.bar(range(len(_x)),_y)
    plt.xticks(range(len(_x)),_x,rotation=45)
    plt.xlabel('城市')
    plt.ylabel('数量')
    plt.title('各城市星巴克的数量')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()