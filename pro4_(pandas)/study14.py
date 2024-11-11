if __name__ == '__main__':

    import pandas as pd
    import numpy as np

    t1 = pd.DataFrame({'a': range(7),
                        'b': range(7, 0, -1),
                        'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                        'd': list("hjklmno")})
    # 以b和c为索引，drop=true将之前的cd两列不再作为数值
    t2 = t1.set_index(['c','d'],drop=True)
    print(t2)
    #取出列索引为a的数据
    t3 = t2['a']
    print(t3)
    # #Series类型
    # # print(type(t3))
    t4 = t3['one']['k']
    # # t4 = t3['one','k']    这种方式取也可以
    print(t4)
    t5 = t3['two']['n']
    # # t5 = t3.loc['two'].loc['n']   用dateFrame的方式取数据
    print(t5)

    # #想去内层的数据的时候，使用swaplevel（）使索引内外的位置互换，从来达到取数据的目的
    t6 = t1.set_index(['d','c'],drop=True)
    print(t6)

    t7 = t6.swaplevel()
    t7 = t7.loc['two'].loc['m']
    print(t7)

    # #取数据使dateFrame与Series的区别就是在二维数组取数据时要加上loc
    t8 = t6.swaplevel().loc['one'].loc['k']
    print(t8)


