if __name__ == '__main__':

    #数组的分组聚合
    #问题：要统计美国和中国的星巴克的数量，我们应该怎么做？

    import pandas as pd
    import numpy as np
    #读取文件
    df = pd.read_csv('./starbucks_store_worldwide.csv')
    # print(df.head(1))
    # print(df.info())

    # 通过country分组
    group = df.groupby('Country')
    # print(group)
    # 获取group中的品牌的数量
    country_count = group['Brand'].count()
    # country_count = group.count()['Brand']   取值可以任意位置

    # 计算出所有国家品牌的数量
    print(country_count)
    # 找到美国和中国的数量
    print(country_count['US'])
    print(country_count['CN'])

    # 从df数据中取出country为us的数据
    # df = df[df['Country']=='US']
    # print(df)
    # count数量统计方法
    # print(group.count())
    # print(group['Brand'].count())
    # print(df.count())
