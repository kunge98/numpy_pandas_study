if __name__ == '__main__':
    #了解文件中评论数和喜欢数的关系，绘制散点图来表示关系
    import numpy as np
    from matplotlib import pyplot as plt

    gb_file_path = './GB_vedio_data.csv'
    t1 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')
    # t1 = [t1[:,1>0]]
    comments = t1[:,1]   #评论
    likes = t1[:,2]        #喜欢
    plt.figure(figsize=(20,8),dpi=80)
    plt.scatter(comments,likes)

    plt.show()



