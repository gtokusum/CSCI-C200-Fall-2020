import random as rn
import matplotlib.pyplot as plt
import time
def flip(x):
    heads = 0
    for i in range(x):
        f = rn.randint(0,1)
        if f == 0:
            heads += 1
        else:
            pass
    return heads

def plot(x):
    h = [i for i in range(1,x+1)]
    y = [flip(i)/i for i in range(1,x+1)]
    fig,ax = plt.subplots()
    plt.plot(h,y)

    plt.show()
start = time.time()
plot(10000)
end = time.time()
print(end-start)