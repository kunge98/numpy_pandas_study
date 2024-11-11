if __name__ == '__main__':
    import pandas as pd
    import string
    t1 = pd.Series([1,3,7,8,6,7,6])
    t2 = pd.Series([1,3,7,8,6],index=list('abcde'))
    print(t1)
    print(t2)
    t3 = pd.Series( {'姓名':'王增坤','年龄':'22','性别':'男'} )
    print(t3)
    t4 = {string.ascii_lowercase[i] for i in range(10)}
    print(t4)
    t5 = pd.Series({'姓名': '王增坤', '年龄': '22', '性别': '男'})
    print(t5['姓名'])
    print(t5['性别'])
    print(t5[0])
    print(t5[1])
    print('*****')
    print(t5[:2])
    print('*****')
    print(t5[[0,2]])
    print('*****')
    print(t5[['姓名','性别']])
    print('*****')
    t7 = pd.Series([1,3,7,8,6],index=list('abcde'))
    print(t7[t7>3])    #布尔取值

    #循环遍历t7的索引
    for i in t7.index:
        print(i)
    print(len(t7.index))
    print(type(t7.index))
    print((t7.index)[:2])

    print(type(t7.values))



