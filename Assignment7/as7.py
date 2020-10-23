###############
# PROBLEM ONE
###############

#recursive
def d(n):
    """
    Recursive
    """
    pass

#recursive
def cr(n,m):
    """
    Must be recursive
    """
    pass

#recursive
def B(n):
    """
    Must be recursive
    """
    pass

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 1" + "~" * 30)
    for i in range(5):
        print("d({0}) = {1}".format(i,d(i)))

    for i in range(1,5):
        for j in range(i):
            print("cr({0},{1}) = {2}".format(i,j,cr(i,j)))
    
    for i in range(6):
        print("B({0}) = {1}".format(i,B(i)))

###############
# PROBLEM TWO
###############
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def get_data(path,name):
    """
    Do not edit this function
    """
    tmp = []
    pn = path + "\\" + name
    file = open(pn, "r")
    for d in file:
        x,y = d.split(",")
        tmp += [[int(x), int(y)]]
    return tmp


#population model
def pop(year):
    pass

#average relative error function
def error(theData):
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 2" + "~" * 30)
    data = get_data("Assignment7", "pop.txt")
    #uncomment this to generate graph
    # total_error = round(error(data),4)

    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #     ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Growth. Total ave error = %{0}".format(total_error))
    # ax.grid()
    # plt.show()

###############
# PROBLEM THREE
###############

#recursive
def a(n):
    """
    Function must be recursive
    """
    pass

#bottom-up memoization
#use this dictionary below
d1 = {0:1}
def am(n):
    """
    Should not be recursive
    """
    pass



#generator
def h():
    """
    Must be written as a generator
    """
    pass

#function ag uses the generator h()
def ag(n):
    """
    Function must utilize the generator
    """
    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """
    print("~" * 30 + "Problem 3" + "~" * 30)
    for i in range(0,6):
        print("a({0}) = {1},{2},{3}".format(i,a(i),am(i),ag(i)))


###############
# PROBLEM FOUR
###############

def palindrome(word):
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 4" + "~" * 30)
    words = ["", "nolemonnomelon","ratsliveonnoevilstar","abba","madamimadamm"]
    for w in words:
        print(palindrome(w))


###############
# PROBLEM FIVE
###############

def div_11(n):
    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 5" + "~" * 30)
    nlst = [587657752,11,22,2728,31415,1358016]

    for n in nlst:
        print(div_11(n))



###############
# PROBLEM SIX
###############

#you must code your own sort (I'd use quicksort)
#if you decide to use sorting
def nn(x,y,z):
    pass

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 6" + "~" * 30)

    x = [1,2,3,4,5,6,7,8,9,10]
    y = 5
    z = 3

    print(x,y,z)
    print(nn(x,y,z))