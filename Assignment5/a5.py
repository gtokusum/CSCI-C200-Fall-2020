import math

def makeProbability(xlst):
    pass    

def entropy(xlst):
    pass

def magic(x):
    pass

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
    pass

#recursive
def occurs_r(x,xlst):
    pass

#while loop
def remove_allw(x,xlst):
    pass

#recursive
def remove_allr(x,xlst):
    pass
#Using only while loops
#refer to lecture 13 on sorting
def bubble_sort(a):
    pass

#recursive selection sort
def rec_sort(xlst):
    pass

#longest run of ones
def lr(xlst):
    pass

def is_magic(ms):
    pass


if __name__ == "__main__":
    # Feel free to add your own tests here to help with error handling. 
    print("This is the code file. To see test results, please run 'test_a5.py'")
    print("Feel free to write your own tests here. The tests you write below will not be graded.")

    # Add your own code below to write your own tests
