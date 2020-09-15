import math
import random as rn


#INPUT two values A,B
#Return A + B
#REQUIREMENTS 
def myPlus(A,B):
#TO DO: Implement function
    return A+B

#INPUT two values A,B
#Return A - B
#REQUIREMENTS 
def myMinus(A,B):
#TO DO: Implement function
    return A-B

#INPUT two values A,B
#Return A divided by B
#REQUIREMENTS 
def myDivide(A,B):
#TO DO: Implement function
    return A/B

#INPUT two values A,B
#Return A x B
#REQUIREMENTS 
def myProduct(A,B):
#TO DO: Implement function
    return A*B

#INPUT two values A,B
#Return A raise to the power of B
#REQUIREMENTS 
def myExponent(A,B):
#TO DO: Implement function
    return A ** B

#INPUT two values A,B
#B is not zero
#Return The Bth root of A
#REQUIREMENTS: Use myExponent function
def myRoot(A,B):
#TO DO: Implement function
    return myExponent(B,1/A)

#INPUT one non-negative value A and base x
#Return log base x of A
#REQUIREMENTS use math module
def myLog(A,x):
#TO DO: Implement function
    return math.log(A,x)

#INPUT one value A
#Return absolute value of A
#REQUIREMENTS 
def myAbs(A):
#TO DO: Implement function
    return abs(A)

#INPUT one value A
#Return e raised to A (Euler's constant)
#REQUIREMENTS use math module
def myExp(A):
#TO DO: Implement function
    return math.exp(A)

#INPUT one value A
#Return floor of A, greatest integer less than A
#REQUIREMENTS use math module
def myFloor(A):
#TO DO: Implement function
    return math.floor(A)