if __name__ == '__main__':
    #英国和美国的视频结合matplotlib绘制各自评论的直方图
    from matplotlib import pyplot as plt
    import numpy as np

    us_file_path = './US_vedio_data.csv'
    gb_file_path = './GB_vedio_data.csv'

    t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int')
    t2 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')

    comments = t1[:,0]
    d = 10000  #设置组距
    num_bins = (comments.max()-comments.min())// d   #设置组数
    plt.figure(figsize=(20,8),dpi=80)
    plt.xticks(range(comments.min(),comments.max(),d))
    plt.hist(comments,num_bins)
    plt.xlabel('评论数')
    plt.ylabel('数量')
    plt.title('视频评论直方图')
    plt.grid(alpha=0.3)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
