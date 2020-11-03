############################################################
# PROBLEM ONE
############################################################
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def cost(x):
    return 2000+500*x

def revenue(x):
    return 2000*x - 10*x**2

def profit(x):
    return revenue(x) - cost(x)

""" 
Do Not Change `fp` or `newton` 
"""
def fp(f):
    h = .00001
    return lambda x: (f(x + h) - f(x-h))/(2*h)

def newton(f,fp,x,tau):
    def n(x):
        while f(x) > tau:
            x = x - f(x)/fp(x)
        return x
    return n(x)


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the test file. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 1" + "~" * 30)
    f = fp(profit)
    x = newton(f,fp(f),1,.0001)
    print("The maximum profit is about ${0}".format(profit(round(x,0))))

    t = np.arange(0.0, 100.0)
    fig,ax = plt.subplots()

    ax.plot(t, profit(t),'g')
    ax.plot(75,profit(75), 'bo--')
    ax.set(xlabel ="Widgets Sold", ylabel="Profit ($)",
        title = "Maximal Profit = ${0}".format(profit(75)))
    ax.grid()
    # plt.show()



############################################################
# PROBLEM TWO
############################################################

ex_f = lambda x: x**6 - x - 1

def sign(x):
    if x <= 0:
       return -1
    else:
        return 1


def bisect(f,a,b,tau):
    c = (a+b)/2
    fb = f(b)
    fc = f(c)
    if b-c <= tau:
        return c
    if sign(fb)*sign(fc) <= 0:
        return bisect(f,c,b,tau)
    else:
        return bisect(f,a,c,tau)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the test file. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 2" + "~" * 30)
    x = bisect(ex_f,1.0,2.0,.001)
    print(x,ex_f(x))

 
############################################################
# PROBLEM THREE
############################################################
# THERE IS NO UNIT TEST ON THIS PROBLEM
############################################################
import sys
import random as rn

try:
    import pygame
    pygame.init()
    installed = True
except:
    installed = False
    print("*"*30)
    print("{:^30}".format("Pygame is not installed. Please install it"))
    if sys.platform == "win32" or sys.platform == "cygwin":
        print("\tRun command:")
        print("\tpy -m pip install pygame")
    elif sys.platform == "darwin" and sys.platform == "linux":
        print("\tRun command:")
        print("\tpython3 -m pip install pygame")
    else:
        print("\tRun command:")
        print("\tpython3 -m pip install numpy")
    print("*"*30)

 
#DARKGREEN (v define it here like below v)
BLACK = ( 0,0,0)
WHITE = (255,255,255)
BLUE =  (0,0,255)
RED =   (255,0,0)
YELLOW = (255,255,0)

class Rectangle:

    def __init__(self,color,loc):
        self.loc = loc
        self.color = color

    def my_draw(self,screen):
        pygame.draw.rect(screen, self.color, self.loc)
    
    def my_move(self,xoffset,yoffset):
        self.loc = [self.loc[0]+xoffset,self.loc[1]+yoffset] + self.loc[2:]
  

def problem3():
    size = [300, 300]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("C200 CHANGE")


    r = Rectangle(RED, [0, 0, 20, 20])

    STAY_IN_GAME = True
    while True and STAY_IN_GAME:
        
        pygame.time.wait(40)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                STAY_IN_GAME = False
                break
                # sys.exit()
    
        if STAY_IN_GAME:
            screen.fill(WHITE)
        
            r.my_draw(screen)
            
            if r.loc[0] > 280:
                xd = -rn.randint(1,3)
            if r.loc[1] > 280:
                yd = -rn.randint(1,3)
            if r.loc[0] < 10:
                xd = rn.randint(1,3)
            if r.loc[1] < 10:
                yd = rn.randint(1,3)
            r.my_move(xd,yd)

            pygame.display.flip()


if __name__ == "__main__" and installed:
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 3" + "~" * 30)
    problem3()


############################################################
# PROBLEM FOUR
############################################################
ex_f = lambda x: x**6 - x - 1

def secant(f,x0,x1,tau):
    fx = f(x1)
    if abs(fx) > tau:
        x2 = x1 - f(x1) * ((x1-x0)/(f(x1)-f(x0)))
        secant(f,x1,x2,tau)
    else:
        return (f(x1))


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 4" + "~" * 30)
    x = secant(ex_f,2.0,1.0,.0001)
    # print(x,ex_f(x))
    print(x)
    

############################################################
# PROBLEM FIVE
############################################################
import math 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def even(x):
    if x % 2 == 0:
        return 1
    else:
        return -1

def simpson(fn,a,b,n):
    dx = (b-a)/n
    gx = (b-a)/(3*n)
    if even(n) == 1:
        x = [i for i in np.arange(a,b+dx,dx)]
        y = [4*fn(x[i]) for i in range(len(x)) if x[i] != x[0] and x[i] != x[-1] and i % 2 != 0]
        z = [2*fn(x[i]) for i in range(len(x)) if x[i] != x[0] and x[i] != x[-1] and i % 2 == 0]
        return gx* (sum(z) + sum(y) + fn(a) + fn(b))
    else:
        return 'n is not even'



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 5" + "~" * 30)

    data = [[lambda x:3*(x**2)+1, 0,6,2],
            [lambda x:x**2,0,5,6],
            [lambda x:math.sin(x), 0,math.pi, 4],
            [lambda x:1/x, 1, 11, 6]]


    for d in data:
        f,a,b,n = d
        print(simpson(f,a,b,n))

    t = np.arange(0.0, 10.0,.1)
    fig,ax = plt.subplots()
    s = np.arange(0,6.1,.1)
    ax.plot(t, (lambda t: 3*(t**2) + 1)(t),'g')
    plt.fill_between(s,(lambda t: 3*(t**2) + 1)(s)) 
    ax.grid()
    # The line below will have a red (not a syntax error)
    ax.set(xlabel ="x", ylabel=r"$f(x)=3x^2 + 1$",
        title = r"Area under the curve $\int_0^6\,f(x)$")

    # plt.show()


############################################################
# PROBLEM SIX
############################################################

#recursive
def V(n,m):
    if m == 0:
        return 4
    else:
        return 2*n - V(n-1,m-1)

#update dictionary e inside Vm
#memoization
e = {}

def Vm(n,m):
    if (n,m) not in e.keys():
        if m == 0:
            e[(n,m)] = 4
        else:
            e[(n,m)] = 2*n - Vm(n-1,m-1)
    return e[(n,m)]
#generator
def h(n,m):
    while True:
        if m == 0:
            yield 4
        else:
            yield 2*n - h(n-1,m-1)

def Vg(n,m):
    z = V(n,m)
    for i in h(n,m):
        if i == z:
            return i 
        else:
            yield i
      



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a8.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 6" + "~" * 30)
    for i in range(5):
        for j in range(5):
            print(i,j,V(i,j), Vm(i,j), Vg(i,j))