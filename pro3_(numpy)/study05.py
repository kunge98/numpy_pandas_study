if __name__ == '__main__':
    import numpy as np
    from matplotlib import pyplot as plt
    #索引和切片、nan
    us_file_path = './US_vedio_data.csv'
    # gb_file_path = './GB_vedio_data.csv'

    t1 = np.loadtxt(us_file_path,delimiter=',',dtype='int')  #转置
    # t2 = np.loadtxt(gb_file_path,delimiter=',',dtype='int')

    print(t1[2,:])  #取第三行数据，从0开始
    print('*****')
    print(t1[2:6,:])  #取连续的数据，3-6行
    print('*****')
    print(t1[[2,4,6],:])  #取不连续的数据，第三行，第五行，第七行，多加一个中括号
    print('*****')
    print('*****')
    print(t1[:,0])
    print('*****')
    print(t1[:,2:])
    print('*****')
    print(t1[:,[0,2,3]])
    print('*******')
    print(t1[[3,5,9],[0,1,3]])
    print('*****')
    print(t1[2:5,1:4])
    t2 = np.array(range(24)).reshape(4,6)
    t2[t2 < 10] = 5   #找到数组中小于10的索引并把这些索引的值设置为5
    print(t2)
    t3 = np.array(range(24)).reshape(4,6)
    t3 = np.where(t3<10,1,2)
    print(t3)
    t4 = np.array(range(24)).reshape(4,6)
    t4 = t4.astype(float)
    t4[0,0]= np.nan   #赋值为nan前先进行类型转换
    t4.clip(10,18)
    print(t4)
    t5 = np.array(range(6)).reshape(2,3)
    t5 = t5.astype(float)
    t5[1,1] = np.nan
    np.isnan(t5)
    np.count_nonzero(t5)
    print(np.isnan(t5))

    print(np.count_nonzero(t5))  #不为nan的个数

    print(np.count_nonzero(t5 != t5))
    np.sum(t5)
    t7 = np.sum(t5,axis=0)
    t6 = np.sum(t5,axis=1)
    print(t7)
    print(t6)




