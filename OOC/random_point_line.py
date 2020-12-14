import random as rn
import matplotlib.pyplot as plt 
import numpy as np

def get_points():
    return rn.random()

def plot(n):
    x = []
    y = []
    under = 0
    for i in range(n):
        x.append(get_points())
        y.append(get_points())
    for i in range(n):
        if y[i] < x[i]:
            under += 1
    fig,ax = plt.subplots()
    ax.set(xlabel='x axis',ylabel='y axis',title='ration of points under y = x: {}'.format(under/n))
    z = np.linspace(0,1,1000)
    plt.plot(x,y,'r *')
    plt.plot(z,z)
    plt.show()


if __name__ == '__main__':
    plot(10000)