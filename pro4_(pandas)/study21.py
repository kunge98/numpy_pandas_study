if __name__ == '__main__':

    #现有北上广成沈5个城市空气质量数据，请绘制出5个城市的PM2.5随时间的变化情况

    import pandas as pd
    from matplotlib import pyplot as plt

    df1 = pd.read_csv('./PM2.5/BeijingPM20100101_20151231.csv')
    df2 = pd.read_csv('./PM2.5/ShanghaiPM20100101_20151231.csv')
    df3 = pd.read_csv('./PM2.5/GuangzhouPM20100101_20151231.csv')
    df4 = pd.read_csv('./PM2.5/ChengduPM20100101_20151231.csv')
    df5 = pd.read_csv('./PM2.5/ShenyangPM20100101_20151231.csv')
    # print(df1.tail(10))
    # print('*'*100)
    # print(df2.head(1))
    # print('*'*100)
    # print(df3.head(1))
    # print('*'*100)
    # print(df4.head(1))
    # print('*' * 100)
    # print(df5.head(1))
    #把分开的时间字符串通过periodIndex的方法转化为pandas时间类型
    period_beijing = pd.PeriodIndex(year=df1['year'],month=df1['month'],day=df1['day'],hour=df1['hour'],freq='H')
    period_shanghai = pd.PeriodIndex(year=df2['year'],month=df2['month'],day=df2['day'],hour=df2['hour'],freq='H')
    period_guangzhou = pd.PeriodIndex(year=df3['year'],month=df3['month'],day=df3['day'],hour=df3['hour'],freq='H')
    period_chengdu = pd.PeriodIndex(year=df4['year'],month=df4['month'],day=df4['day'],hour=df4['hour'],freq='H')
    period_shenyang = pd.PeriodIndex(year=df5['year'],month=df5['month'],day=df5['day'],hour=df5['hour'],freq='H')
    #设置五个城市的datetime作为索引
    df1['datetime'] = period_beijing
    df2['datetime'] = period_shanghai
    df3['datetime'] = period_guangzhou
    df4['datetime'] = period_chengdu
    df5['datetime'] = period_shenyang
    df1.set_index('datetime', inplace=True)
    df2.set_index('datetime', inplace=True)
    df3.set_index('datetime', inplace=True)
    df4.set_index('datetime', inplace=True)
    df5.set_index('datetime', inplace=True)
    # 生成的图样本太密集，所以对样本进行降采样,D为day，7D意思就是一周，再去平均值
    df1 = df1.resample('7D').mean()
    df2 = df2.resample('7D').mean()
    df3 = df3.resample('7D').mean()
    df4 = df4.resample('7D').mean()
    df5 = df5.resample('7D').mean()
    #
    data_beijing = df1['PM_Dongsihuan'].dropna()
    data_shanghai = df2['PM_Jingan'].dropna()
    data_guangzhou = df3['PM_City Station'].dropna()
    data_chengdu = df4['PM_Caotangsi'].dropna()
    data_shenyang = df5['PM_Taiyuanjie'].dropna()

    _x_beijing = [i.strftime('%Y%m%d') for i in data_beijing.index]
    _y_beijing = data_beijing.values

    _x_shanghai = [i.strftime('%Y%m%d') for i in data_shanghai.index]
    _y_shanghai = data_shanghai.values

    _x_guangzhou = [i.strftime('%Y%m%d') for i in data_guangzhou.index]
    _y_guangzhou = data_guangzhou.values

    _x_chengdu = [i.strftime('%Y%m%d') for i in data_chengdu.index]
    _y_chengdu = data_chengdu.values

    _x_shenyang = [i.strftime('%Y%m%d') for i in data_shenyang.index]
    _y_shenyang = data_shenyang.values


    plt.figure(figsize=(20,8),dpi=80)
    plt.plot(range(len(_x_beijing)),_y_beijing,label='北京', alpha=0.7)
    plt.plot(range(len(_x_shanghai)),_y_shanghai,label='上海', alpha=0.7)
    plt.plot(range(len(_x_guangzhou)),_y_guangzhou,label='广州', alpha=0.7)
    plt.plot(range(len(_x_chengdu)),_y_chengdu,label='成都', alpha=0.7)
    plt.plot(range(len(_x_shenyang)),_y_shenyang,label='沈阳', alpha=0.7)
    plt.xticks(range(0,len(_x_guangzhou),10),list(_x_guangzhou)[::10],rotation=45)

    plt.xlabel('时间')
    plt.ylabel('排放量')
    plt.title('城市排放PM2.5折线图')
    plt.legend(loc='best')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()


