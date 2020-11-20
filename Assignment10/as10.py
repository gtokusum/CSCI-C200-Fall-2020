########################
#Problem One
########################

class Binary:

    def __init__(self, value = 0):
        y = 0 
        p = 0
        n = abs(int(value))
        while n != 0:
            y = (n%2) * (10**p) + y
            p += 1
            n = n//2
        if value < 0:
            self.val = -y
        else:
            self.val = y

    def __str__(self):
        return 'b'+str(self.val)
    def b_to_d(self):
        x = 0
        b = list(str(abs(self.val)))
        binary = b[::-1]
        power = 0
        for i in binary:
            if i == '1':
                x += 2**power
            power += 1
        if self.val < 0:
            return -1*x
        else:
            return x

    def d_to_b(self,v):
        """
        HINT: Does not modify any instance variables
        """
        y = 0 
        p = 0
        n = abs(int(v))
        while n != 0:
            y = (n%2) * (10**p) + y
            p += 1
            n = n//2
        if v < 0:
            return -y
        else:
            return y

    def __add__(self, other):
        return Binary(self.b_to_d() + other.b_to_d())

    def __sub__(self,other):
        return Binary(self.b_to_d() - other.b_to_d())

    def __mul__(self,other):
        return Binary(self.b_to_d() * other.b_to_d())

    def __neg__(self):
        return Binary(-1*self.val)
    def __abs__(self):
        return Binary(abs(self.val))

    def __len__(self):
        if self.val < 0:
            x = str(self.val)
            return len(x[1:])
        else:
            return len(str(self.val))

    def __and__(self,other):
        x = str(self.val)[::-1]
        y = str(other.val)[::-1]
        z = ''
        while len(x) != len(y):
            if len(x) > len(y):
                y += '0'
            else:
                x += '0'
        x = x[::-1]
        y = y[::-1]
        for i in range(len(x)):
            if x[i] == '1' and y[i] == '1':
                z += '1'
            else:
                z += '0'
        z = int(z)
        g = 0
        b = list(str(z))
        binary = b[::-1]
        power = 0
        for i in binary:
            if i == '1':
                z += 2**power
            power += 1
        return Binary(z)
    
    #free :)
    def __eq__(self, other):
        return self.b_to_d() == other.b_to_d()

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    # """
    print("~"*30)
    print("Problem 1")
    print("~"*30)
    x = Binary(7)
    y = Binary(1)
    z = x + y
    u = x & y
    print("Binary Printed:", x,y,u)
    print("b_to_d():",z,z.b_to_d())
    -z # HINT: Calling __neg__ function
    print("b_to_d() after using __neg__:",z,z.b_to_d())
    w = y - x
    print("Binary printed:", w)
    print("Length of w:", len(w))
    v = x - y
    print("Binary printed:", v)
    t = v * Binary(2)
    print("Binary printed:", t)
    print("Length of a binary:",len(Binary(7)))
    print("Length of w:",len(Binary(1)))
    abc = Binary(8)
    print("Binary printed:",abc)
    print("Length of abc:",len(abc))
    -abc # HINT: Calling __neg__ function
    print("Binary printed after using __neg__:",abc)
    print("Length of abc after using __neg__:",len(abc))

    print("Next 16 lines are first 16 numbers in binary")
    for i in range(16):
        x = Binary(i)
        print(i,x)


########################
#Problem Two
########################

#change lat,lon to radians in the functions
from math import radians, sin, cos, sqrt, asin 

#INPUT two tuples that have lat, lon values
#RETURN distance in miles
def hd(loc1,loc2):
    r = 3961
    loc1 = (radians(loc1[0]),radians(loc1[1]))
    loc2 = (radians(loc2[0]),radians(loc2[1]))
    latd = (loc2[0] - loc1[0])/2
    lond = (loc2[1] - loc1[1])/2
    dnot = (sin(latd))**2 + cos(loc1[0])*cos(loc2[0])*sin(lond)**2
    d = 2 * r * asin(sqrt(dnot))
    return d

def dd(loc1,loc2):
    """
    Standard distance formula
    """
    lat1,lon1 = loc1
    lat2,lon2 = loc2
    x = lat1 - lat2
    y = (lon1 - lon2)*cos(radians(lat2))
    return 69.385*sqrt(x**2 + y**2)

def eu_distance(loc1,loc2):
    """
    Euclidian Distance Forumula
    """
    return sqrt(sum([(i-j)**2 for i,j in zip(loc1,loc2)]))


if __name__ == "__main__": 
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print 
    statements. 
    """
    print("~"*30)
    print("Problem 2")
    print("~"*30)
    #Lindley Hall where we had C200 on 
    #south side of campus
    l1 = (39.165341,-86.523588)

    #Luddy Hall the new Luddy building, where we have C200
    #on northside of campus
    l2 = (39.172725,-86.523295)

    #Distance between Lindley and Luddy
    print("haversine", hd(l1,l2), "mi")
    print("Euclidean", eu_distance(l1,l2), "mi")
    print("Approximate", dd(l1,l2), "mi")




########################
#Problem Three
########################

import matplotlib.pyplot as plt
import numpy as np

plt.gca().set_prop_cycle('color', ['red', 'green', 'blue', 'black'])

class MyLine:

    def __init__(self, *args, **kwargs):
        if '2pts' in kwargs.values():
            x = args[0]
            y = args[1]
            m = (x[1]-y[1])/(x[0]-y[0])
            self.slope = m
            line = lambda x:m*x
            g = 1
            pointInt = 0
            while g != 0:
                g = m*pointInt
                pointInt += 1
            self.intercept = pointInt
            
            
        elif 'point-slope' in kwargs.values():
            p = args[0]
            m = args[1]
            self.slope = m
            self.intercept = p[0]
            
            
        elif 'lambda' in kwargs.values():
            z = args[0]
            y = lambda x:eval(args[0])
            self.intercept = y(0)
            self.slope = 
            
            
        else:
            pass
        
        self.line = lambda x:eval(str(self.get_line()[3:]))

    def draw(self):
        abscissa = np.arange(20)
        plt.plot(abscissa,self.line(abscissa))
 
    def get_line(self):
        return "y = {0:.2f}*x + {1:.2f}".format(self.slope, self.intercept)

    def __str__(self):
        return self.get_line()

    def __mul__(self,other):
        if self.slope == other.slope:
            return ()
        else:
            return ((other.intercept - self.intercept)/(self.slope - other.slope),(other.slope-self.slope)/(self.slope-other.slope))

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print 
    statements. 
    """
    print("~"*30)
    print("Problem 3")
    print("~"*30)
    x1 = MyLine((0,0), (5,5),options = "2pts")
    x1.draw()
    x2 = MyLine((5,0),-1/4, options = "point-slope")
    x2.draw()
    x3 = MyLine("(-4/5)*x + 5", options = "lambda")
    x3.draw()
    x4 = MyLine("x + 2", options = "lambda")
    x4.draw()

    print("The intersection of {0} and {1} is {2}".format(x1,x2,x1*x2))
    print("The intersection of {0} and {1} is {2}".format(x1,x3,x1*x3))
    print("The intersection of {0} and {1} is {2}".format(x1,x4,x1*x4))


    plt.legend([x1.get_line(), x2.get_line(), x3.get_line(),x4.get_line()], loc='upper left')
    plt.show()

########################
#Problem Four
########################

import matplotlib.pyplot as plt

xlst, ylst = [],[]

def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return n*3 + 1
    

def g(n,i):
    xlst.append(i)
    ylst.append(n)
    print(str(n)+' ',end='')
    if n == 1:
        return 1
    else:
        return g(f(n),i+1)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    """
    print("~"*30)
    print("Problem 4")
    print("~"*30)
    g(26,0) # Change to g(27, 0) if you want to see other graph mentioned in PDF
    xmax = max(tuple(xlst))
    ymax = max(tuple(ylst))
    print(ylst)
    print("\nNumber of recursive calls: {0}\nMaximum number: {1}".format(xmax,ymax))
    plt.plot(xlst,ylst,'r--')
    plt.axis([0,xmax,0,ymax])
    plt.show()


########################
#Problem Five
########################


import matplotlib.pyplot as plt
import numpy as np

def get_data(path, name):
    """
    Path and name are both `str` objects in python. 

    File paths in python should be combined with "/" character

    Returns: A list of lists, where each inner list is a pair of floats
    """
    x = open('Assignment10/stockdata.txt','r')
    contents = x.readlines
    x.close()
    return contents

def mean(lst):
    return sum(lst)/len(lst)

def sd(xlst):
    pass

def r(x, y):
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a10.py`. Feel free to add print statements. 
    """
    print("~"*30)
    print("Problem 5")
    print("~"*30)
    data = get_data("Assignment10", "stockdata.txt")
    

    xData = [i[0] for i in data]
    yData = [i[1] for i in data]

    correlation = r(xData, yData)
    print(correlation)
    # Example of creating a plot
    plt.plot(xData, yData, 'ro')
    t = np.arange(0,6,.1)
    plt.plot(t,t*.65 + .5,'g--')
    plt.axis([0,6,0,6])
    plt.xlabel("A values")
    plt.ylabel("B value")
    plt.title("r = {0:.3}".format(correlation))
    plt.show()

