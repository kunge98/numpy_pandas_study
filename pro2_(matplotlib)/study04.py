if __name__ == '__main__':
    from matplotlib import pyplot as plt
    #绘制散点图
    y_3 = [11,17,16,12,11,12,11,16,16,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
    y_10 =[23,25,26,19,21,18,19,18,22,23,17,20,22,15,11,15,15,13,17,10,11,13,12,16,15,19,21,22,22,17]
    x_3=range(1,32)
    x_10=range(51,81)
    plt.figure(figsize=(20,8),dpi=80)
    plt.scatter(x_3,y_3,label='3月份气温散点图')
    plt.scatter(x_10,y_10,label='10月份气温散点图')
    #调整x轴的刻度
    _x = list(x_3) + list(x_10)
    _xtick_labels = ['3月{}日'.format(i) for i in x_3]
    _xtick_labels += ['10月{}日'.format(i-50) for i in x_10]
    plt.xlabel('时间')
    plt.ylabel('温度 单位（℃）')
    plt.title('两个月份的温度散点图')
    plt.legend(loc='best')
    plt.grid(alpha=0.3)
    plt.xticks(_x[::3],_xtick_labels[::3],rotation=45)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()