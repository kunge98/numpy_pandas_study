if __name__ == '__main__':
    from matplotlib import pyplot as plt
    #加入在30岁的时候，根据自己的实际情况，统计出从11岁到30岁每年交的女朋友的数量，列表A，请绘制出折线图(如果是两个人的只需要加入新的y即可)
    #分析自己每年交女朋友的数量走势   y表示个数，x表示岁数
    # 注意在设置多个折线图的时候，设置的间距要向右挪一下，防止重叠
    y1=[1,0,1,2,4,3,2,3,2,4,5,6,5,4,3,3,2,1,1,6]
    y2=[0,0,1,1,3,2,3,5,4,5,3,2,1,2,2,3,3,2,2,3]
    y3=[3,2,1,2,2,4,4,4,3,4,1,1,2,2,1,2,2,0,1,2]
    x=range(11,31)
    plt.figure(figsize=(20,8),dpi=80)
    _x_labels=['{}岁'.format(i) for i in x]
    plt.xticks(x,_x_labels)
    plt.xlabel('年龄')
    plt.ylabel('男(女)朋友个数')
    plt.title('不同年龄处对象的个数')
    plt.grid(alpha=0.3)  #绘制表格,alpha设置透明度
    plt.plot(x,y1,label='WZK的恋爱曲线',color='yellow',linestyle='--',linewidth=5)
    plt.plot(x,y2,label='LXR的恋爱曲线',color='skyblue',linestyle=':')
    plt.plot(x,y3,label='陆仁贾的恋爱曲线',color='red',linestyle='-.')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.legend(loc='best')  #设置图例,loc可以设置图例摆放在图片中的位置 upper，lower，center，left，right，best
    plt.show()
