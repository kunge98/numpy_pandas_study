if __name__ == '__main__':
    from matplotlib import pyplot as plt
    #问题知道了列表中电影分别在2017.09.14/15/16三天中的单日票房，展示一下比对情况
    #注意在设置多个条形图的时候，设置的间距要向右挪一下，防止重叠
    x=['猩球崛起','终极之战','英雄归来','战狼2','敦刻尔克']
    y_14 = [15746,312,4497,15844,319]
    y_15 = [12357,456,2045,18247,168]
    y_16 = [15358,399,2357,16424,362]

    #每个的第一个数据不可能都放在一起，避免重叠要向右移动一下
    bar_width = 0.2
    x_14 = list(range(len(x)))
    x_15 = [i+bar_width for i in x_14]
    x_16 = [i+bar_width*2 for i in x_14]

    plt.figure(figsize=(20,8),dpi=80)

    plt.bar(range(len(x)),y_14,width=bar_width,label='09.14',color='red')
    plt.bar(x_15,y_15,width=bar_width,label='09.15')
    plt.bar(x_16,y_16,width=bar_width,label='09.16',color='yellow')
    plt.xticks(x_15,x)
    plt.legend(loc='best')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()