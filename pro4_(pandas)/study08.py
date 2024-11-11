if __name__ == '__main__':

    #数组的合并  ----   concat

    import pandas as pd
    import numpy as np

    df1 = pd.DataFrame(np.ones((3,4))*0,index=list('XYZ'),columns=list('abcd'))
    df2 = pd.DataFrame(np.ones((3,4))*1,index=list('XYZ'),columns=list('abcd'))
    df3 = pd.DataFrame(np.ones((3,4))*2,index=list('XYZ'),columns=list('abcd'))

    # 0表示行，对列操作，1表示列，对行操作,
    #ignore_index合并之后是否忽略原先的索引
    # print(pd.concat([df1,df2,df3],axis=0,ignore_index=True))

    #join  inner做交集   默认是outer，做并集
    df4 = pd.DataFrame(np.ones((3,4))*0,index=list('123'),columns=list('abcd'))
    df5 = pd.DataFrame(np.ones((3,4))*1,index=list('234'),columns=list('bcde'))

    #两个数组索引值不完全相同，所以在进行outer合并是会将不同的索引没有的数值填充为NaN
    # print(pd.concat([df4,df5],join='outer'))

    #inner表示找交集，相同的部分
    #axis的值为0对列操作，只需要找出列中相同的部分即可，行全部写出
    #axis的值为1对行操作，只需要找出行中相同的部分即可，列全部写出
    print(pd.concat([df4,df5],join='inner',ignore_index=True,axis=0))

    # print(pd.concat([df4,df5],join='inner',ignore_index=True,axis=1))
    # print(df4.append([df5,df5],ignore_index=True))
    res1 = df4.append(pd.Series([1,2,4,7],index=list('abcd')),ignore_index=True)   #在df4的最下面一行添加[1,2,4,7]数据
    # print(res1)







