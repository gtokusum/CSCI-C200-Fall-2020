def while_factorial(n):
    result = 1 # when multiplying, if you start with 0, you will always end with 0
    while n >= 1: #while n>0
        result *= n # result = result * n
        n -= 1 # n = n - 1 we can treat n as a variable and we are not modifing it out of the function
        # since it is an integer (immutable)
    return result



def factorial(n):
    if n == 1 : # if n == 0: # base case
        return 1
    else: # inductive step (loop)
        return n * factorial(n-1)        


def tail_factorial(n, a=1):
    if n == 0: # could also do n == 1
        return a # we are returning out accumulator
    else:
        return tail_factorial(n-1,a = a*n)


def memo_factorial(n):
    pass


if __name__ == "__main__":
    print("Factorial Practice")
    indicies = [1, 2, 3,  4,   5,   6,      10]
    answers  = [1, 2, 6, 24, 120, 720, 3628800]
    functions = [while_factorial, factorial, tail_factorial, memo_factorial]

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