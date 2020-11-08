###########################
# Problem One
###########################
# There is no unit testing 
# for this problem
###########################
import numpy as np
import matplotlib.pyplot as plt
import random as rn



def step(x,y,i):
    """
    TODO:

    Translates a random int into a step along the random walk
    
    parameters: INTEGER i for the step index, numpy array x for 
                tracking the left/right location at index i,
                numpy array y for tracking the forward/backward 
                location at index i

    return: none 
        You will be modifying x and y, since lists are mutable
    """
    direction = rn.randint(1,4) # keep this line
    # TODO: implement this function solution
    ########################################
    pass

def graphit(x,y,n):
    """
    Do not modify this function
    """
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print 
    statements. 
    """
    print("*"*30)
    print("* Executing Problem 1")
    print("*"*30)

    #number of steps
    n = 100000   #You should change the number of steps to see
                #to see how it affects the plot
    xArray = np.zeros(n) 
    yArray = np.zeros(n) 

    #fill array with step values 
    for i in range(1,n):
        step(xArray,yArray,i)

    graphit(xArray, yArray, n)


###########################
# Problem Two
###########################

import random as rn


#Assume this is in 2D dimension
def distance(p1,p2):
    """
    TODO: 
    Given two points, find the distance between the points.

    The points are given as a tuple with 2 values
    """
    pass



def brute(xlst):
    """
    TODO:
    Given a list of points, where each points is represented 
    by a tuple of 2 values. 
    """
    pass
 
if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print 
    statements. 
    """
    print()
    print("*"*30)
    print("* Problem 2")
    print("*"*30)


    x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    print("x", x)
    print("Distance between x[0] and x[1]: ", distance(x[0], x[1]))
    print("Brute:", brute(x))



###########################
# Problem Three
###########################

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math 

def productivity(N,T = 40):
    """
    TODO:

    Function described in the paper provided
    """
    pass

""" 
Do Not Change fp or newton
"""
def fp(f):
    """
    Do not modify
    """
    h = .00001
    return lambda x: (f(x + h) - f(x-h))/(2*h)

def newton(f,fp,x,tau):
    """
    Do not modify
    """
    def n(x):
        while f(x) > tau:
            x = x - f(x)/fp(x)
        return x
    return n(x)


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print 
    statements. 
    """
    print()
    print("*"*30)
    print("* Problem 3")
    print("*"*30)
    f = fp(productivity)
    x = math.ceil(newton(f,fp(f),62,.01))
    y = math.ceil(productivity(x))
 
    print("The maximum productivity is P({0}) ~ {1} person x hrs".format(x,y))

    t = np.arange(0.0, 100.0)
    fig,ax = plt.subplots()

    ax.plot(t, productivity(t),'g')
    ax.plot(x,productivity(x), 'bo--')
    ax.set(xlabel ="Number of people", ylabel="person x hrs", title = "Maximal Productivity P({0}) ~ {1}".format(x,y))

    ax.grid()
    plt.show()

    print("Please complete answering the questions described in the other PDF")



###############
# PROBLEM Four
###############

class Vector2D:
    def __init__(self, *x):
        if x:
            self.tuple_value = x
        else:
            self.tuple_value = (0,0)

    def get_tuple(self):
        return self.tuple_value

    def __mul__(self, other):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def __add__(self, other):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def __sub__(self, other):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def __abs__(self):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def scalar_mul(self, x):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def __neg__(self):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass

    def __eq__(self, other):
        """
        TODO:

        Implement function described in the homework PDF
        """
        pass


    def __str__(self):
        return "{0}".format(self.get_tuple())


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print 
    statements. 
    """
    print()
    print("*"*30)
    print("* Problem 4")
    print("*"*30)
    x = Vector2D(1,2)
    y = Vector2D(4,-1)
    w = Vector2D(1,2)
    print("Addition: ", x + y)
    print("Multiplication: ", x * y)
    print("Subtraction: ", x - y)
    print("Absolute value: ", abs(x))
    x.scalar_mul(5)
    print("Scalar Multiplication: ", x)
    -x
    print("Negative (1st): ", x)
    -x
    print("Negative (2nd): ", x)
    print("Equivalence: ", x == w)


###############
# PROBLEM Five
###############

import math

class MyComplexNumber:
    def __init__(self, rpart, ipart):
        self.rpart = rpart
        self.ipart = ipart
        self.cn = [self.rpart, self.ipart]
    
    def get_real(self):
        return self.rpart
    
    def get_imag(self):
        return self.ipart
    
    def __str__(self):
        return str(self.cn)

    #adds two complex numbers
    def add(self, ix):
        """
        TODO:
        """
        pass
    
    #extends the '+' operator to add two complex numbers
    #what's the different between __add__(self,ix) and add(self,ix)? 
    def __add__(self,ix):
        """
        TODO:
        """
        pass
        
     #extends the '-' operator to subtract two complex numbers
    # parameters: MyComplexNumber self, MyComplexNumber ix to subtract 
    #       from the MyComplexNumber self
    # return: a new MyComplexNumber containing the result
    def __sub__(self,ix):
        """
        TODO:
        """
        pass

    # extends the '/' operator to divide two complex numbers
    # parameters: MyComplexNumber self, MyComplexNumber ix to divide 
    #       into the MyComplexNumber self
    # return: a new MyComplexNumber containing the result
    def __truediv__(self,other):
        """
        TODO:
        """
        pass

    def __mul__(self,other):
        """
        TODO:
        """
        pass

    #calculates the modulus of the self MyComplexNumber
    #parameters: MyComplexNumber self
    #return: the value of the modulus
    def modulus(self):
        """
        TODO:
        """
        pass

    #converts the self MyComplexNumber to polar representation
    #parameters: MyComplexNumber self
    #return: a tuple (rho, theta) as defined in the text, but where theta is in degrees not radians
    def polar(self):
        """
        TODO: 
        """
        pass

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a9.py`. Feel free to add print 
    statements. 
    """
    print()
    print("*"*30)
    print("* Problem 5")
    print("*"*30)
    x1 = MyComplexNumber(3,-1) #3-i
    x2 = MyComplexNumber(1,4)  #1+4i
    x3 = MyComplexNumber(-3,1) #-3+i
    x4 = MyComplexNumber(2,-4) #2-4i
    x5 = MyComplexNumber(-2,1)
    x6 = MyComplexNumber(1,2)
    x7 = MyComplexNumber(0,3) 
    x8 = MyComplexNumber(-1,-1)
    x9 = MyComplexNumber(1,-1)
    x10 = MyComplexNumber(4,-3)
    x11 = MyComplexNumber(3,2)
    x12 = MyComplexNumber(1,1)


    print("Addition: ", x1 + x2)
    print("Multiplication: ", x1 * x2)
    print("Addition: ", x3 + x4)
    print("Multiplication: ", x3 * x4)
    print()
    print("Division: ", x5/x6)
    print("Division: ", x7/x8)
    print("Modulus: ", x9.modulus())
    print("Modulus: ", x10.modulus())
    print()
    print("Polar: ", x12.polar())

