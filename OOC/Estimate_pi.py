import random as rn
import matplotlib.pyplot as plt 
import math
#getting random floats between 0 and 1
def get_float():
    return rn.random()

def plot(n):
    x = []
    y = []
    for i in range(n):
        x.append(get_float())
        y.append(get_float())
    in_circ = 0 
    #counts how many points were inside the circle
    for i in range(n):
        if math.sqrt(x[i]**2 + y[i]**2) < 1:
            in_circ += 1
    fig,ax = plt.subplots()
    ax.set(xlabel='x axis',ylabel = 'y axis',title = 'Estimat of pi = {}'.format(4*in_circ / n))
    plt.plot(x,y,'r *')
    plt.show()


if __name__ == '__main__':
    plot(1000)