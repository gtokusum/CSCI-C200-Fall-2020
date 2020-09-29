"""
TODO: Add comment about who your partner was (or if you worked alone). 
Include anything else you want to in this comment

"""

import math


###########################################################################
# Functions for Problem 1
###########################################################################
def y(d,r,t):
    return d * math.exp(r*t)

def N(n_0, m, t):
    return n_0*math.exp(m*t)

def N_t(t):
    return math.ceil(71.8*math.exp(-8.98*math.exp(-0.0685*t)))


def K(t):
    eq = (((9/2.6)*t)/((2*(t**2))+3))/100
    return round(eq, 5)

def r(t):
    eq = (1.5207*t**4) - (19.166*t**3) + (62.91*t**2) + (6.0726*t) + (1026)
    return round(eq, 2)
    
def p(x):
    return (4*(x**2)) - (100*x) - (1000)

def W(P_i, P_f):
    r = 8.314
    return math.ceil(r * 300 * (math.log(P_i/P_f)))

def dep(c,s,el):
    return round((c-s)/el,0)

def L(V,A,C_l):
    k = 0.0033
    return math.ceil(k * (V**2) * A * C_l)

###########################################################################
# Functions for Problem 2
###########################################################################
def q(a,b,c):
    # This function will return a tuple of 2 values
    # The "plus" value must be first in the tuple
    # The "minus" value must be second in the tuple 
    # Please note, this dealing with the +/- (plus/minus) sign in the equation
    d = (b**2) - (4*a*c)
    if d >= 0:
        x = (-b + math.sqrt(d)) / (2*a)
        y = (-b - math.sqrt(d)) / (2*a)
        return (x,y)
    
    else:
        x = (-b/(2*a))  
        xj = (math.sqrt(-d)/(2*a))
        y = (-b/(2*a)) 
        yj = - (math.sqrt(-1*d)/(2*a))
        return (complex(x,xj),complex(y,yj))

###########################################################################
# Functions for Problem 3
###########################################################################
def checkout(xlst):
    price = 0
    for alst in xlst:
        if alst[2] == 1:
            gamma = alst[0] * alst[1]
            price += (gamma*1.07)
        else:
            gamma = alst[0] * alst[1]
            price += gamma
    return round(price,2) 




###########################################################################
# Functions for Problem 4
###########################################################################
def e(xlst):
    emptySeats = []
    for alst in xlst:
        for i in alst:
            if i == 0:
                emptySeats.append(i)
    return len(emptySeats)

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
