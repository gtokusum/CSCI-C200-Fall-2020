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
        finalProbs += (i*(math.log(i)/math.log(2)))
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
            print(emlst)
            

        else:
            if xlst[0] != x:
                emlst.append(xlst[0])
                # print(emlst)
                remov(x,xlst[1:])
            else:
                # print(emlst)
                remov(x,xlst[1:])
    def ans(y):
        return y
    remov(x,xlst)
    # return emlst
    
        


#Using only while loops
#refer to lecture 13 on sorting
def bubble_sort(a):
    pass

#recursive selection sort
def rec_sort(xlst):
    pass

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
    pass


if __name__ == "__main__":
    # Feel free to add your own tests here to help with error handling. 
    print("This is the code file. To see test results, please run 'test_a5.py'")
    print("Feel free to write your own tests here. The tests you write below will not be graded.")
    remove_allr(1,[1,1,2,1,2])
    remove_allr(3,[1,1,2,1,2])
    # Add your own code below to write your own tests
