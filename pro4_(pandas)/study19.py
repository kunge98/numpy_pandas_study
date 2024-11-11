if __name__ == '__main__':

    #时间序列

    import pandas as pd
    import numpy as np

    missing_you = pd.date_range(start='20210112',periods=86400,freq='H')
    missing_you2 = pd.date_range(start='20210112',end='20210113',freq='H')

    # print(missing_you)
    # print(type(missing_you))
    # print(missing_you2)
    t1 = pd.DataFrame(np.array(range(12)).reshape(3,4),index=list('XYZ'),columns=list('ABCD'))
    # t1['Y',:] = np.nan
    # t1.dropna(axis=)
    t1['B'] = np.nan
    # t1 = t1.dropna(axis=0)
    t1[ t1 == 0] = np.nan
    print(t1)
