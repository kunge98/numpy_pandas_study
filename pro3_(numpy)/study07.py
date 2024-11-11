#问题：将数组中的nan用均值来替换，该函数名字取A
def A():
    for i in range(t1.shape[1]):  #索引取1表示列，0表示行
        # t1.shape[1] 代表列有几列
        # t1.shape[0] 代表行有几行

        column = t1[:,i]  #循环遍历每一列
        countNan = np.count_nonzero(column != column)  #判断数组中nan的个数
        if countNan != 0:   #不为0，说明这一列有nan
            columnNotNan = column[column == column]  #当前这一列不为nan的array
            columnNotNan.mean()  #求出该列的均值
            column[np.isnan(column)] = columnNotNan.mean()#选中当前为nan的位置，把值赋值给不为nan的均值
    return t1

if __name__ == '__main__':
    import numpy as np
    t1 = np.array(range(12)).reshape(3,4).astype(float)
    t1[1,2:] = np.nan
    print('原来的数组','\n',t1)
    t1 = A()
    print('替换后的数组','\n',t1)