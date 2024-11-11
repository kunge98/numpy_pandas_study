if __name__ == '__main__':

    # 问题：接study10，统计中国每个省份的星巴克的数量
    import pandas as pd
    import numpy as np

    df = pd.read_csv('./starbucks_store_worldwide.csv')

    print(df.head(2))
    print(df.info())
    # 找到country中为CN的数据
    china_data = df[df['Country']=='CN']
    print(china_data)

    group = china_data.groupby(by='State/Province')['Brand'].count()
    print(group)

