if __name__ == '__main__':
    import numpy as np
    #将两个国家的数据整合在一起进行分析,同时保留国家信息，设置美国为0，英国为1
    #数组的拼接
    us_file_path = './US_vedio_data.csv'
    gb_file_path = './GB_vedio_data.csv'
    #读取文件
    us_data = np.loadtxt(us_file_path,delimiter=',',dtype=int)
    gb_data = np.loadtxt(gb_file_path,delimiter=',',dtype=int)
    #分别创建两列0和1代表着国家信息,astype解决了数组拼接之后是科学计数法的bug
    us_0 = np.zeros((us_data.shape[0],1)).astype(int)
    gb_1 = np.ones((gb_data.shape[0],1)).astype(int)
    #进行数组的拼接，美国的原数组和新创建的0进行拼接，英国的原数组和新创建的1进行拼接
    us_data = np.hstack((us_data,us_0))
    gb_data = np.hstack((gb_data,gb_1))
    #将整合拼接完成后的新的两个国家的数据进行垂直拼接
    final = np.vstack((us_data,gb_data))
    print(final)


