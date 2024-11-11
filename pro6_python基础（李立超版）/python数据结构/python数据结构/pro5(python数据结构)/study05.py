if __name__ == '__main__':
    from scipy import interpolate
    import numpy as np
    from  matplotlib import pyplot as plt
    x=np.linspace(0,2*np.pi,10)
    y = np.sin(x)
    plt.plot(x,y,'o')
    plt.show()