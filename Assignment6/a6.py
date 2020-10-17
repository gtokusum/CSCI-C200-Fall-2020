###########################################################################
# Introduction Code (As reference)
###########################################################################

def o(x,xlst):
    if xlst:
        return xlst[0] == x or o(x, xlst[1:])
    else:
        return False

def ol(x,xlst):
    def oh(xlst):
        if xlst:
            return xlst[0] == x or oh(xlst[1:])
        else:
            return False
    return oh(xlst)

if __name__ == "__main__":
    print("~"*20 + "Introduction" + "~"*20 + "\n")
    print(o(1,[1,2,3]))
    print(o(4,[1,2,3]))
    print(ol(1,[1,2,3]))
    print(ol(4,[1,2,3]))
    print("\n" * 3)



###########################################################################
# Problem 1
###########################################################################
def F(n,m,p):
    """
    Function F in the PDF document as recursive
    """
    pass

def Ft(n,m,p,v = 100):
    """
    Function F in the PDF document **BUT** this one has to be tail recursive
    """
    pass


def gsf_close(a,r,n):
    """
    Function F in the PDF document in closed form
    """
    pass

def gsf(a,r,n):
    """
    Function F in the PDF using a for loop
    """
    pass

def g(a,r,n):
    """
    The sigma function (5) in the pdf that implements recursio
    """
    pass


def B(n):
    """
    Function B in the PDF using recursion
    """
    pass

def Bt(n,v=0):
    """
    Function B in the PDF using tail-recursion
    """
    pass



def x(n):
    """
    Function x in the PDF using recursion
    """
    pass

def xt(n,v=3):
    """
    Function x in the PDF using tail-recursion
    """
    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("~"*20 + "Problem 1" + "~"*20 + "\n")
    print("The next 3 lines are calls for F and Ft")
    print(F(5,5,5),Ft(5,5,5))
    print(F(1,2,3),Ft(1,2,3))
    print(F(5,4,2),Ft(5,4,2))
    print("The next 5 lines are calls for B and Bt")
    for i in range(5):
        print(B(i), Bt(i))
    print("The next 3 lines are for gsf, g, and gsf_close, respectively")
    print(gsf(2,3,5))
    print(g(2,3,5))
    print(gsf_close(2,3,5))
    print("The next 5 lines are for x and xt")
    for i in range(5):
        print(x(i),xt(i))



###########################################################################
# Problem 2
###########################################################################

d,c = "d","c"
def bk(xbook):
    """
    Implement an iterative solution for problem 2 (for or while loops)
    """
    pass

def bkr(xbook):
    """
    Implement a recursive solution for problem 2
    """
    pass    



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 2" + "~"*20 + "\n")
    d,c = "d","c"
    xbook1 = [[d, 895],[c,7500],[d,339],[c,234],[d,6400],[d,100]]
    xbook2 = [[d, 95],[c,500],[d,39],[c,234],[d,600],[d,10]]
    print("The next two lines are calls to bkr with xbook1 and xbook2 as parameters, respectively")
    print(bkr(xbook1))
    print(bkr(xbook2))
    print("The next two lines are calls to bk with xbook1 and xbook2 as parameters, respectively")
    print(bk(xbook1))
    print(bk(xbook2))



###########################################################################
# Problem 3
###########################################################################

def is_isogram(xword):
    """
    

    You are **not** allowed to use the .count() method
    """
    pass

def anagram(x,y):
    """
    An anagram is a rearrangment of letters from a word
    
    Hint: One way to think of this is to compare the number of letters that each string has
    """
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 3" + "~"*20 + "\n")
    words = ["dermatoglyphics","palindrome", "anagram"]
    word_pairs = [["abc", "cba"],["ddog", "dog"], ["anagram", "margana"]]
    print("The next " + str(len(words)) + " lines are calls to is_isogram")
    for w in words:
        print(is_isogram(w))
    print("The next " + str(len(word_pairs)) + " lines are calls to is_isogram")
    for i,j in word_pairs:
        print(anagram(i,j))



###########################################################################
# Problem 4
###########################################################################

def div_9(x):
    """
    Implement the logic in problem 4. You cannot simply divide by nine and return true.

    You are only allowed to use modulo (%) and evenly divides (//) only with the number 10. 
    i.e. 5 % 10
    """
    pass

    
if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 4" + "~"*20 + "\n")
    xlst = [99,0,18273645,22,27]
    print("The next " + str(len(xlst)) + " lines are calls to div_9")
    for i in xlst:
        print(div_9(i))




###########################################################################
# Problem 5
###########################################################################
xs = ["", "I","II","III","IV", "V","VI","VII","VIII", "IX"]
yd = ["", "X","XX","XXX","XL", "L", "LX","LXX","LXXX","XC","C"]

def cicero(epectitus):
    """
    This should print all of the roman numerals from 1-100 in the format that is shown in the assignments pdf
    """
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 5" + "~"*20 + "\n")
    for i in range(1,101):
        print("{0:<3} {1:<8}".format(i,cicero(i)),"   ", end="")
        if i % 5 == 0:
            print()



###########################################################################
# Problem 6
###########################################################################


import random as rn

#secret number
x_find = [rn.randint(1,1000), rn.randint(1,1000), rn.randint(1,1000), rn.randint(1,1000)]

def find_tuple(x):
    """
    x_find is a tuple of four randomly chosen integers
    This function is supposed to loop through all of the possiblities so to find what the tuple is
    One way to do this is to write four nested for-loops.
    """
    pass


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """    
    print("\n" * 3 + "~"*20 + "Problem 6" + "~"*20 + "\n")
    print("xfind:" + str(x_find))
    print("The next line is a call to find_tuple")
    print("Your xfind:" + str(find_tuple(x_find)))
                

###########################################################################
# Problem 7
###########################################################################


#Make it easier to type 
A,C,T,G = 'A','C','T','G'

def make_pairing(xseq):
    """
    Parameter (xseq): A DNA sequence as a string
    Returns: The complementary sequence
    """
    pass


def findError(s1,s2):
    """
    Parameters:
        s1: String of DNA sequence
        s2: String of DNA sequence
        (Assume len(s1) == len(s2))

    Returns: dash '-' if the pairing is correct and an '*' pointing to 
        where the violation of the pairing is
    """
    pass



if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a6.py`. Feel free to add print statements. 
    """
    print("\n" * 3 + "~"*20 + "Problem 7" + "~"*20 + "\n")
    
    s1 = "ATCGATTGAGCTCTAGCG"
    s2 = "TAGCTAACTCGAGATCGC"
    s3 = "TAACGAACTGGAGACCGC"

    print("The next line is a call to make_pairing")
    print("{0}\n{1}".format(s1,make_pairing(s1)))
    print(s2 == make_pairing(s1))
    print()
    print("The next line is a call to findError")
    print("{0}\n{1}\n{2}".format(s1,s3,findError(s1,s3)))
    
    

###########################################################################
# Extra Tests
###########################################################################

if __name__ == "__main__":
    """
    Feel free to add any tests below you want to try

    (Make sure you indent so it is inside of this if statement)
    """
    pass
