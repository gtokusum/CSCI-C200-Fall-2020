def reverse_str(s):
    pass

def reverse_str_while(s):
    pass

def reverse_str_tail(s,a=''):
    pass 

def is_palin(s):
    """
    Determine whether a word is spelled the same forwards and backwards.
    
    Note:
        We are assuming all characters are lower case and there are no spaces or punctuations.
        If you are feeling adventurous, go ahead and try to account for spaces, punctuation, and capitalization. 
    """
    pass

if __name__ == "__main__":
    print("Sum of Squares Practice")
    indicies = ["hello","qwerty","racecar","","!@#$%^&*()"]
    answers  = ["olleh","ytrewq","racecar","",")(*&^%$#@!"]
    functions = [reverse_str, reverse_str_while, reverse_str_tail]

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

    indicies = ["hello", "racecar", "madam", "davinci", "deleveled", "hellokitty", "evitative", "kayak", ""]
    answers  = [False,   True,      True,    False,     True,        False,        True,        True,    True]

    if is_palin(indicies[0]) != None:
        print("="*5, "Testing: "+func.__name__+"()", "="*5)
        print("Our Inputs:", indicies)
        print("Your Outputs:")
        for i in range(len(indicies)):
            result = is_palin(indicies[i])
            correct = int(bool(result == answers[i]))
            print("  {0}({1}) == {2} \t{3}".format(is_palin.__name__, indicies[i], result, ("WRONG", "RIGHT")[correct]))
        print("\n\n")