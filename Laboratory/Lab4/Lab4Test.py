#import Lab4 as L4
from Lab4 import *


FUNCTIONS = [
    findTheEvens,
    findTheDivisibles,
    getIndexOfNumbers,
    sumsOfInnerList,
    getSumByindex,
    deleteChar,
    targetSum,
    validPassword    
]

testCases = {
    findTheEvens: [
                    ([12,3,24,1,54123,],),
                    ([342,23,2,3,512],),
                    ([3,432,123,234],)
                    ],
    findTheDivisibles: [
                    ([234,321,5342,5,32234,],3,),
                    ([432,35,2323,5234,234,],7,),
                    ([392,43895,2340,2348,],5,)
                    ],
    getIndexOfNumbers: [
                    ([2342,1231,5432,34,235,23],[1231,34],),
                    ([532,5,32,54,754,],[5,754,532]),
                    ([234,6435,654,345,],[654,]),
                    ],
    sumsOfInnerList: [
                    ([[1,2,3],[4,5,6],[7,8,9],],), 
                    ([[13,36,55],[25,34,62],[10,23,34],],)
                     ],
    getSumByindex: [
                    ([[1,2,3],[4,5,6],[7,8,9],],), 
                    ([[13,36,55],[25,34,62],[10,23,34],],),
                    ],
    deleteChar: [
                    ("CSCI-C 200: Intro to Computers And Programming", ["C", "K", "m"],),
                    ("What is your passphrase?: >", ["s", " "],)
                ],
    targetSum: [
                    ([3,2,7,4],7,),
                    ([1,7,9,10,13,],23,),
                    ([3,42,10,98,2],101,),
                ],
    validPassword: [
                    ("",),
                    ("Foobar123!",),
                    ("foobar123!",),
                    ("foo",),
                    ("FOOBAR123!",),
                ]    
}

correctValues = {
    findTheEvens: [
            [12, 24],
            [342, 2, 512],
            [432, 234],
    ],
    findTheDivisibles: [
            [234, 321],
            [35],
            [43895, 2340],
    ],
    getIndexOfNumbers: [
            [1, 3],
            [1, 4, 0],
            [2],
    ],
    sumsOfInnerList: [
            [6, 15, 24],
            [104, 121, 67],
    ],
    getSumByindex: [
            [12, 15, 18],
            [48, 93, 151],
    ],
    deleteChar: [
            "SI- 200: Intro to oputers And Prograing",
            "Whatiyourpaphrae?:>",
    ],
    targetSum: [
            (0, 3),
            (3, 4),
            (0, 3),
    ],
    validPassword: [
            False,
            True,
            False,
            False,
            False,
],
}




def getSolutions():
    """
    NOT USED FOR LAB
    """
    results = {}
    for func in FUNCTIONS:
        results[func] = [func(*x) for x in testCases[func]]
    for key in results:
        print(f"\t{key.__name__}: [")
        for value in results[key]:
            print(f"\t\t{value},")
        print("\t],")


def myTestString(func, params):
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))

def testYourFunctions():
    """
    This function will test if your function produces the right result
    Don't have to worry how it works
    """
    for func in FUNCTIONS:
        print(f"  ~~~TESTING {func.__name__}~~~")
        yourAnswer = [func(*testCase) for testCase in testCases[func]]
        ourAnswer = correctValues[func]
        numberRight = len(ourAnswer)
        for i in range(len(ourAnswer)):
            if yourAnswer[i] != ourAnswer[i]:
                print(f"Failed test case: {testCases[func][i]}")
                print(f"Your Answer {yourAnswer[i]}: Expect Answer {ourAnswer[i]}")
                numberRight -= 1
        print("\t{}/{} Right".format(numberRight,len(ourAnswer)))
        print()

##### Testing if you have certain modules installed

print("\n"*3)
print("~"*30)
import sys

print("Checking Installation of numpy and matplotlib")

try:
    import numpy
    print("\tNumpy is installed, Version: " + str(numpy.__version__))

except:
    print("\tModule Numpy is not installed")
    if sys.platform == "win32" or sys.platform == "cygwin":
        print("\tRun command:")
        print("\tpy -m pip install numpy")
    elif sys.platform == "darwin" and sys.platform == "linux":
        print("\tRun command:")
        print("\tpython3 -m pip install numpy")
    else:
        print("\tRun command:")
        print("\tpython3 -m pip install numpy")

print()

try:
    import matplotlib
    print("\tmatplotlib is installed, Version: " + str(matplotlib.__version__))

except:
    print("\tModule matplotlib is not installed")
    if sys.platform == "win32" or sys.platform == "cygwin":
        print("\tRun command:")
        print("\tpy -m pip install matplotlib")
    elif sys.platform == "darwin" and sys.platform == "linux":
        print("\tRun command:")
        print("\tpython3 -m pip install matplotlib")
    else:
        print("\tRun command:")
        print("\tpython3 -m pip install matplotlib")

if __name__ == "__main__":
    testYourFunctions()