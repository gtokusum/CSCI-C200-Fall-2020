import math

def makeProbability(xlst):
    getnums = {}
    getprobs = []
    for i in xlst:
        getnums[i] = xlst.count(i)
    for i in getnums.values():
            getprobs.append(i/len(xlst))
    return getprobs    

def entropy(xlst):
    probs = makeProbability(xlst)
    finalProbs = 0
    for i in probs:
        finalProbs += (i*(math.log(i,2)))
    return -finalProbs

def magic(x):
    return ((((((x+15)*3)-9)/3)-12))

#remove using for as example
def remove_all(x,xlst):
    xtmp = []
    for i in xlst:
        if i != x:
            xtmp.append(i)
    return xtmp

#occurs using for as example
def occurs(x,xlst):
    found = False
    for i in xlst:
        if x == i:
            found = True
            break
    return found

#while loop
def occurs_w(x,xlst):
    found = False
    num = len(xlst)
    while num > 0:
        for i in xlst:
            if i == x:
                found = True
                break
            num -= 1
    return found
#recursive
def occurs_r(x,xlst):
    if xlst == []:
        return False
    else:
        return xlst[0] == x or occurs_r(x,xlst[1:])
#while loop
def remove_allw(x,xlst):
    lst = []
    num = len(xlst)
    while num > 0:
        for i in xlst:
            if i != x:
                lst.append(i)
            num -= 1
    return lst
#recursive
def remove_allr(x,xlst):
    emlst = []
    
    def remov(x,xlst):
        if xlst == []:
            return emlst
            

        else:
            if xlst[0] != x:
                emlst.append(xlst[0])
                # print(emlst)
                remov(x,xlst[1:])
            else:
                # print(emlst)
                remov(x,xlst[1:])
    
    remov(x,xlst)
    return emlst
    
        


#Using only while loops
#refer to lecture 13 on sorting
def bubble_sort(a):
    i = 0
    while a != sorted(a):
        if i > len(a) - 2:
            i = 0
        else:
            if a[i+1] < a[i] and i < len(a)-1:
                a[i],a[i+1] = a[i+1],a[i]
    
                i+=1
        
            
        
            else:
                i += 1
    return a
#recursive selection sort
def rec_sort(xlst):
    if xlst == [] or len(xlst) == 1:
        return xlst
    else:
        w = []
        def sortingmech(y):
            if y == []:
                return w
            else:
                a = min(y)
                w.append(a)
                y.remove(min(y))
                return sortingmech(y)
        sortingmech(xlst)
    return w
#longest run of ones
def lr(xlst):
    size = 0
    maxSize = 0
    for i in xlst:
        if i == 1:
            size += 1
        else:
            size = 0
        if size > maxSize:
            maxSize = size
    return maxSize
        

def is_magic(ms):
    mag = False
    alpha = ms[0]
    beta = ms[1]
    omeg = ms[2]
    col1 = alpha[0] + beta[0] + omeg[0]
    col2 = alpha[1] + beta[1] + omeg[1]
    col3 = alpha[2] + beta[2] + omeg[2]
    diagLR = alpha[0] + beta[1] + omeg[2]
    diagRL = alpha[2] + beta[1] + omeg[0]
    if sum(alpha) == sum(beta) == sum(omeg) == col1 == col2 == col3 == diagLR == diagRL:
        mag = True
        return mag
    else:
        return mag


if __name__ == "__main__":
    # Feel free to add your own tests here to help with error handling. 
    print("This is the code file. To see test results, please run 'test_a5.py'")
    print("Feel free to write your own tests here. The tests you write below will not be graded.")
    rec_sort([44, 65, 79, 83, 86, 89, 3, 43, 83, 91])
    # Add your own code below to write your own tests
