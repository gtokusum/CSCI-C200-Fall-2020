"""
Examples of using recursion with a list as the input
"""
### Example 1 - covered in class
## Created by Nick Mobley
def sos_list(xlst):
    """
    Given a list of numbers find the sum of squares 
    recrusively
    """
    if not xlst:
        return 0 # base case
    else:
        #print(xlst) # uncomment to see each xlist at each step of recursion
        return xlst[0]**2 + sos_list(xlst[1:]) # inductive step
print("Example 1 output:")
print(sos_list([1,2,3]))

#############################################
## Example 2 - covered in class
## Created by Nick Mobley
def addIndex(xlst,index = 0):
    """ 
    Given a list of numbers return a list of a numbers
    which is the original list plus it's index for example
    xlst: [13,14,8,10] would return
    [13,15,10,13] since 
    [13,14,8,10]
    [0,  1,2, 3]
    +-----------
    [13,15,10,13]
    """
    if not xlst:
        return []
    else:
        return [xlst[0] + index] + addIndex(xlst[1:],index+1)
print("Example 2 output: ")
print(addIndex([13,14,8,10]))
#########################################
# Example 3 - not covered in class
## Created by Teresa Perez
def fun(xlst):
    if not xlst:
        return []
    else:
        return [xlst[0]] + fun(xlst[1:]) 
print("Example 3 output: ")
print(fun([1,2,3,4,5])) 

#############################################
# Example 4 - not covered in class
## Created by Chris Alexeev
def only_ints(xlist):
    if not xlist:
        return []
    elif type(xlist[0]) != int:
        return [] + only_ints(xlist[1:])
    else: 
        return [xlist[0]] + only_ints(xlist[1:])
# outputs [1, 4, 4]
print("Example 4 output: ")
print(only_ints([1,4,"s",4]))
