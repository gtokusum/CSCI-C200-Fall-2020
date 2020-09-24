def findTheEvens(theList):
    """
    Given a list of at least one number,
    return a **new** list that only contains the even numbers
    Parameters:
      - theList: a list of integers
    """
    evenList = []
    # for i in theList: goes through values
       
    for j in range(len(theList)):
        itemAtVaule = theList[j] #accessing the list at the j index/position
        # determine if the number is even
        # Modulo of a number ==> %
        # 5 % 2 == 1 --> gives remainder
        if itemAtVaule % 2 == 0:
            evenList = evenList + [itemAtVaule]
        else:
            pass
    return evenList


def findTheDivisibles(theList, theNumber):
    """
    Given a list of at least one number, return a **new** list of 
    values that are divisible by the given number

    Parameters:
    - theList: a list of integers
    - theNumber: An integer
    """
    divisibleList = []
    for i in range(len(theList)):
        value = theList[i]
        if value % theNumber ==0:
            divisibleList += [value]
    return divisibleList


def getIndexOfNumbers(theList,numsToIndex):
    """
    Given a list of random numbers (theList) we want to map the values in numsToIndex into what their index is in theList
    Example:
    theList: [3,5,1,6]
    numsToIndex: [6,5]
    should return [3,1] (since 6 is the third index and 5 is the first)
    """
    indexResult = []
    for num in numsToIndex:
        for i in range(len(theList)):
            value = theList[i]
            if num == value :
                indexResult += [i]
    return indexResult


def sumsOfInnerList(listOfLists):
    """
    Given a list of lists (of arbritary length)
    return a new list that is the sum of the 
    inner lists. E.G
    [[1,2,3],[4,5,6],[7,8,9]]
    [6,15,24] 
    """
    finalList =[]
    for innerList in listOfLists:
        innerSum = 0 
        for num in innerList:
            innerSum += num
        finalList += [innerSum]

    return finalList
    


def getSumByindex(listOfLists):
    """
    Given a list of lists (assume the inner lists are the same size),
    Return a list of the sums of each index
    Ex. 
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]] should return 
    [12, 15, 18] 
    where 1+4+7 = 12, 2+5+8 = 15, 3+6+9 = 18 
    """
    

def deleteChar(string, chars):
    """
    Given a string S, and a list chars,
    Delete each character in the list from the string
    Ex.
    ("CSCI-C 200", ["C"]) should return "SI- 200"
    """
    pass

def targetSum(listNumbers,target):
    """ 
    Given a list of numbers and a target value
    return a tuple of indices of the two numbers that when added together make up the target value example
    listNumbers = [2,6,9,10] 
    target = 11
    would return (0,2)

    Assume you will always produce a value.
    """
    pass


def validPassword(password):
    """
    Given a string, determine if it's a valid password.
    To be valid the password must:
    - be at least 10 characters long
    - contain 1 uppercase character
    - contain 1 lowercase character
    - contain 1 digit
    - contain one special character
        - We can assume special characters include !,@,#,$,%,^,&,*,(,)
    """
    pass

