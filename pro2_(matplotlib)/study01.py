if __name__ == '__main__':
    from matplotlib import pyplot as plt
    x = range(3, 24, 3)
    y = [15, 14, 13, 18, 17, 20, 21]
    picture = plt.figure(figsize=(20, 15), dpi=80)  # 设置生成图片的大小
    plt.plot(x, y)
    plt.xticks(range(0, 31))  # 设置在x轴生成的参数
    plt.yticks(range(0, 31))  # 设置在x轴生成的参数
    # plt.xticks(x[::2])
    # plt.yticks(range(min((y)),max(y)+1))  #根据传入的y的参数的大小指定坐标轴
    plt.savefig('./test1_study01.png')
    plt.savefig('./test1_study01.svg')  #.svg后缀生成矢量图
    plt.show()