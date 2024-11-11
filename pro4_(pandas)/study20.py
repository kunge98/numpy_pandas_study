if __name__ == '__main__':

    #比较中国和美国pm2.5的折线图

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt

    df = pd.read_csv('./PM2.5/BeijingPM20100101_20151231.csv')
    print(df.head(1))
    # print(df.info())

    # 把分开的时间字符串通过periodIndex的方法转化为pandas时间类型
    period = pd.PeriodIndex(year=df['year'],month=df['month'],day=df['day'],hour=df['hour'],freq='H')
    print(period)
    print(type(period))

    # 把分开的时间字符串通过periodIndex的方法转化为pandas时间类型
    df['datetime'] = period

    # 把datatime设置为索引
    df.set_index('datetime',inplace=True)

    # 生成的图样本太密集，所以对样本进行降采样,D为day，7D意思就是一周，再去平均值
    df = df.resample('7D').mean()

    # 处理缺失数据，删除缺失数据
    # print(df["PM_US Post"])
    data_us = df['PM_US Post']
    data_cn = df['PM_Dongsihuan']

    # 画图
    _x = data_us.index
    _x_us = [i.strftime('%Y%m%d') for i in _x]
    _y_us = data_us.values

    _x2 = data_cn.index
    _x_cn = [i.strftime('%Y%m%d') for i in _x2]
    _y_cn = data_cn.values


    plt.figure(figsize=(20,8),dpi=80)

    plt.plot(range(len(_x_us)),_y_us,label='US_POST', alpha=0.7)
    plt.plot(range(len(_x_cn)),_y_cn,label='CN_POST', alpha=0.7)
    plt.xticks(range(0,len(_x_us),10),list(_x_us)[::10],rotation=45)
    plt.xlabel('月份')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.legend('best')
    plt.show()
