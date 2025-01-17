if __name__ == '__main__':
    from matplotlib import pyplot as plt
    #问题假设获取了100部电影的时长，统计画出这些电影的分布状态频率信息，如何呈现？
    #直方图
    x = [118,123,140,117,128,108,98,97,104,107,108,160,137,124,116,117,128,132,178,100,
         103,113,127,98,92,120,143,123,132,142,124,156,165,112,121,132,141,114,116,112,
         110,105,104,103,98,97,95,123,114,116,123,127,180,126,118,107,114,125,136,148,
         109,99,98,174,90,95,114,113,102,108,107,163,137,148,158,142,100,97,107,140,
         127,114,145,112,117,96,114,127,130,138,108,107,120,145,118,114,102,154,117,120]
    plt.figure(figsize=(20,8),dpi=80)
    d = 5   #建议设置组距的时候,最大值-最小值除组距尽量为整数，
    num_bins = (max(x)-min(x))//d   #得到分组的数量
    plt.hist(x,num_bins,density=True)
    plt.xticks(range(min(x),max(x)+d,d))  #设置x轴的刻度
    plt.xlabel('分钟')
    plt.ylabel('频率')
    plt.title('电影时长直方图')
    plt.grid(alpha=0.6)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
