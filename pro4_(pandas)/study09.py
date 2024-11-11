if __name__ == '__main__':

    #数组的合并   ----  merge
    import numpy as np
    import pandas as pd

    #匹配1个key的情况
    left1 = pd.DataFrame({'key':['K4','K1','K2','K5'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
    right1 = pd.DataFrame({'key':['K0','K1','K2','K3'],
                         'C':['C0','C1','C2','C3'],
                         'D':['D0','D1','D2','D3']})
    #按照关键字key进行合并，两者都有key，key放中间，依次合并
    res1 = pd.merge(left1,right1,on='key')
    # print(res1)


    #匹配2个key的情况
    left2 = pd.DataFrame({'key1':['K0','K0','K1','K2'],
                          'key2':['K0','K1','K0','K1'],
                             'A':['A0','A1','A2','A3'],
                             'B':['B0','B1','B2','B3']})
    right2 = pd.DataFrame({'key1':['K0','K1','K1','K2'],
                           'key2':['K0','K0','K0','K0'],
                              'C':['C0','C1','C2','C3'],
                              'D':['D0','D1','D2','D3']})
    # 按照关键字key进行合并，两者都有key，key放中间，依次合并,对比两个key的值要完全相同
    #默认是inner
    #left2中的key1和key2的值要和right2中的key1和key2的值一模一样
    #left2中对应的k0和k0，在right2中要找到所有的k0，k0
    #left2中对应的k0和k1，在right2中要找到所有的k0，k1，在right中有两组k0，k1，则输出全部对应的数据
    #相当于笛卡尔积
    res2 = pd.merge(left2,right2,on=['key1','key2'],how='inner')
    print(res2)
    #outer取并集
    #根据key1和key2的值将没有该key的那部分数据填充为NaN，打印输出一目了然
    res3 = pd.merge(left2,right2,on=['key1','key2'],how='outer')
    print(res3)
    # #right表示以merge（）第2个参数为准，分别输出第2个参数的key值，从第1个找与第2个对应的key输出，找不到则填充NaN
    res4 = pd.merge(left2,right2,on=['key1','key2'],how='right')
    print(res4)
    # # left表示以merge（）第1个参数为准，分别输出第1个参数的key值，从第2个中找与第1个对应的key输出，找不到则填充NaN
    res5 = pd.merge(left2,right2,on=['key1','key2'],how='left')
    print(res5)
    #
    # # 参数  indicator  两个数组在合并的时候，显示的是怎么进行merge的，默认为false不显示，可以把值设置为字符串进行该列名称的赋值
    df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
    df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
    res6 = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator~~~')
    print(res6)
    #
    # #  参数 index
    left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],'B': ['B0', 'B1', 'B2']},
                          index=['K0','K1','K2'])
    right3 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],'B': ['D0', 'D1', 'D2']},
                          index=['K3','K3','K5'])
    # print(left3)
    # print(right3)
    # # 将两个数组的index作文合并的key
    res7 = pd.merge(left3,right3,left_index=True,right_index=True,how='outer')
    print(res7)
    #
    # # 参数 suffixes 在合并相同列名的时候为了区分给合并后的列加上后缀
    left4 = pd.DataFrame({'key':['K0','K1','K2'],'age':[18,22,24]})
    right4 = pd.DataFrame({'key':['K0','K0','K3'],'age':[4,5,6]})
    res8 = pd.merge(left4,right4,on='key',suffixes=['_boys','_grils'],how='outer')
    print(res8)






