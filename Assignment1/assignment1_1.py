#INPUT two values
#RETURN A and B
def myAnd(A,B):
#TO DO: Implement function
    return A and B

#INPUT two values
#RETURN A or B 
def myOr(A,B):
#TO DO: Implement function
    return A or B

#INPUT one value
#RETURN not A
def myNot(A):
#TO DO: Implement function
return not A

#INPUT two values
#RETURN not (A and B) (called nand)
#REQUREMENTS use only previous functions
def myNand(A,B):
#TO DO: Implement function
    return not (A and B)

#INPUT two values
#RETURN not (A or B) (called nor)
#REQUIREMENTS use only previous functions
def myNor(A,B):
#TO DO: Implement function
    return not (A or B)

#INPUT two values A,B
#Return material implication A => B 
#REQUIREMENTS use only previous functions
def myImplication(A,B):
#TO DO: Implement function
    return A >= B

#EXTRA CREDIT 5%
#INPUT two values A,B
#RETURN A or B 
#REQUIREMENTS only use myNand gate
def ECmyWeirdOr(A,B):
#TO DO: Implement function
    return not myNand(A,B)