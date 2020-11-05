###############
# PROBLEM ONE
###############

#recursive
def d(n):
    """
    Recursive
    """
    if n == 0:
        return 1
    else:
        return 3* d(n-1) + 1

#recursive
def cr(n,m):
    """
    Must be recursive
    """
    if m == 0 or n == m:
        return 1
    else:
        return cr(n-1,m) + cr(n-1,m-1)

#recursive
def B(n):
    """
    Must be recursive
    """
    if n == 0:
        return 1
    else:
        return (-1/(n+1)) * sum([cr(n+1,i)*B(i) for i in range(n)])
    

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
    return 1436.53*(1.01395**year)

#average relative error function
def error(theData):
    x = [i[1] for i in theData]
    s = [i - 1900 for i in x]
    y = [np.absolute(pop(i)) for i in s]
    return 100/12 * sum(y)

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    """
    print("~" * 30 + "Problem 2" + "~" * 30)
    data = get_data("Assignment7", "pop.txt")
    # uncomment this to generate graph
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
    if n == 0:
        return 1
    else:
        return n*((-1)**n) +a(n-1)

#bottom-up memoization
#use this dictionary below
d1 = {0:1}
def am(n):
    """
    Should not be recursive
    """
    for i in range(1,n+1):
        if i not in d1.keys() :
            d1[i] = d1[i-1] + (i*((-1)**i))
#             print(d1)
        else:
            pass
    return d1[n]




#generator
def h():
    """
    Must be written as a generator
    """
    x,y = 1,1
    while True:
        yield x
        x = x + (y)*(-1)**y
        y = y + 1

#function ag uses the generator h()
def ag(n):
    """
    Function must utilize the generator
    """
    s = h()
    while n >0:
        next(s)
        n -= 1
    return next(s)


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
    a = list(word)
    b = ''.join(a)
    x = list(word[::-1])
    y = ''.join(x)
    return str(y) == str(b)


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
    x = [int(i) for i in str(n)]
    count = 0
    ans = 0
    for i in x:
        if count % 2 == 0:
            ans += i
            count += 1
        else:
            ans -= i
            count += 1
    return ans == 11 or ans == -11 or ans == 0



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
    def qs(n):
        if len(n) <= 1:
            return n
        else:
            left,right = [],[]
            pivot = n[0]
            for i in n[1:]:
                if i <= pivot:
                    left.append(i)
                else:
                    right.append(i)
        return qs(left) + [pivot] + qs(right)
    ans = [i for i in qs(x) if i == y]
    more = [i for i in qs(x) if i > y]
    less = [i for i in qs(x) if i < y]
    def repeat(ans,less,more,y,z):
        while len(ans) < z:
            if len(less) == 0 or len(more)==0:
                return ans
            elif np.absolute(less[-1]-y) < np.absolute(more[0]-y):
                ans.append(less[-1])
                repeat(ans,less[:-1],more,y,z)
            elif np.absolute(less[-1]-y) < np.absolute(more[0]-y):
                ans.append(more[0])
                repeat(ans,less,more[1:],y,z)
            else:
                ans.append(more[0])
                ans.append(less[-1])
                repeat(ans,less[:-1],more[1:],y,z)
        return ans
    if len(ans) < z:
        repeat(ans,less,more,y,z)
    else:
        pass
    return ans
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