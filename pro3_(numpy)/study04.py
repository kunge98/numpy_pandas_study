if __name__ == '__main__':
    import numpy as np
    #读取文件（了解）

    us_file_path = './US_vedio_data.csv'
    gb_file_path = './GB_vedio_data.csv'

    t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int')  #转置
    t2 = np.loadtxt(us_file_path,delimiter=',',dtype='int',unpack=True)
    t3 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')
    print('*************************')
    print(t1)
    print('*************************')
    print(t2)
    print('*************************')
    print(t3)

    t4 = np.array(range(24)).reshape(4,6)
    print(t4)
    # t4.swapaxes(1,0)
    # t4.T
    # t4.transpose()
    print(t4)
