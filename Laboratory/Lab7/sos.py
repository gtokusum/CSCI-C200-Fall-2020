"""
Sum of squares is where you add the squares of all numbers from 1 to n (inclusive).
You can also think of it as the sum of squares from n down to 1.
The function is very similar to factorial in how it is set up.
"""

def while_sos(n):
    pass

def sos(n):
    pass

def tail_sos(n, a=1):
    pass

d = {}
def memo_sos(n):
    pass

if __name__ == "__main__":
    print("Sum of Squares Practice")
    indicies = [1, 2, 3,  4,   5,   6,   10]
    answers  = [1, 5, 14, 30,  55,  91, 385]
    functions = [while_sos, sos, tail_sos, memo_sos]

    for func in functions:
        if func(indicies[0]) != None:
            print("="*5, "Testing: "+func.__name__+"()", "="*5)
            print("Our Inputs:", indicies)
            print("Your Outputs:")
            for i in range(len(indicies)):
                result = func(indicies[i])
                correct = int(bool(result == answers[i]))
                print("  {0}({1}) == {2} \t{3}".format(func.__name__, indicies[i], result, ("WRONG", "RIGHT")[correct]))
            print("\n\n")