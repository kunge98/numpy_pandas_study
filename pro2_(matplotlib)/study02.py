if __name__ == '__main__':
    #练习题目要求：列表A表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？
    #不识别中文的字体该问题还没有解决。   plt.rcParams['font.sans-serif'] = ['SimHei']
    import random
    from matplotlib import pyplot as plt
    x=range(0,120)
    y=[random.randint(20,35) for i in range(120)]
    plt.plot(x,y)
    _xtick_labels = ['10:{}'.format(i) for i in range(60)]   #10点的时间
    _xtick_labels += ['11:{}'.format(i) for i in range(60)]   #11点之后的时间
    plt.xticks(list(x)[::30],_xtick_labels[::30])  #rotation设置坐标轴上的表示方向
    plt.xlabel('时间')
    plt.ylabel('温度 单位（℃）')
    plt.title('10点到12点每分钟的变化情况')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
