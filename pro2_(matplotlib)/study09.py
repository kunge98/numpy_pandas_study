if __name__ == '__main__':
    from matplotlib import pyplot as plt
    #问题：美国2004年人口普查发现有1.24亿在离家相对较远的地方工作，给出了他们从家到上班工作的地方需要的时间，绘制成直方图
    #注意：数据已经进行了处理，所以直接制作直方图有困难，可以制作条形图设置间距变成直方图
    x = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
    interval = [0,5,10,15,20,25,30,35,40,45,60,90]
    plt.figure(figsize=(20,8),dpi=80)
    plt.bar(range(12),x,width=1)
    _x = [i-0.5 for i in range(13)]
    _xtick_labels = interval +[150]
    plt.xticks(_x,_xtick_labels)
    plt.grid(alpha=0.5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
