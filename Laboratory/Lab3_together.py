def warping(speed):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    In the wonderful world of Star Trek, they have a way to travel faster than light. Below is a table of the speed representation. 
    The table is from "The Star Trek Encyclopedia: A Reference Guide to the Future. Updated and Expanded Edition" by Michael Okuda 
    and Denise Okuda.
    Speed                   |    Number of times speed of light (Number represents lower bound)
    Sublight(Warp Factor 0) |    0
    Warp Factor 1           |    1
    Warp Factor 2           |    10
    Warp Factor 3           |    39
    Warp Factor 4           |    102
    Warp Factor 5           |    214
    Warp Factor 6           |    392
    Warp Factor 7           |    656
    Warp Factor 8           |    1,024
    Warp Factor 9           |    1,516
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: A float or number
    Returns: A number representing the warp factor
    """
    finalWarpSpeed = -1
    if speed < 1:
        finalWarpSpeed = 0
    elif speed < 10:
        finalWarpSpeed = 1
    elif speed < 39:
        finalWarpSpeed = 2
    elif speed < 102:
        finalWarpSpeed = 3
    elif speed < 214:
        finalWarpSpeed = 4
    elif speed < 392:
        finalWarpSpeed = 5 
    elif speed < 656:
        finalWarpSpeed = 6
    elif speed < 1024:
        finalWarpSpeed = 7
    elif speed < 1516:
        finalWarpSpeed = 8
    else:
        finalWarpSpeed = 9
    return finalWarpSpeed

def driving_time(miles,speed):
    """
    Finds the amount of time (hours) it takes to drive a given number of miles at a given speed (mph)
    Inputs: miles (int), speed (int)
    Returns: time (int in hours)
    """
    pass

def race(a_miles,a_speed,b_miles,b_speed):
    """
    Finds the who will reach their destination first (a or b)
    Inputs: a_miles (miles), a_speed (mph), b_miles (miles), b_speed (mph)
    Returns: 0 if player A arrives first, 1 if player B arrives first, -1 if equal
    """
    pass

def countLetters(letters, theLetter):
    """
    Given a string of letters and the letter you are looking for, return the number of times that happens.
    """
    pass

def countLetters2(letters, theLetter):
    """
    Given a string of letters and the letter you are looking for, return the number of times that happens.
    """
    pass


def myTestString(func, params):
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))

# For more information about the line below, refer to the link: https://docs.python.org/3/library/__main__.html
#   You can read more about it but it is to help when handling multiple files
#   Will be dicussed at a later point
if __name__ == "__main__":
    print("Final Test Code\n")
    print("Testing warping()")
    for x in [(0,), (41.0,),(10.2,), (1111,)]:
        print(myTestString(warping, x))
    
    print()
    print("Testing race()")
    for x in [(5,50,6,60,),(5,25,4,60,)]:
        print(myTestString(race, x))
    
    print()
    print("testing countLetters()")
    testing = [("aaabbbaaacccdddifkf;lkajsdf;lkjA", "b"), ("The quick brown fox jumped very lazily over the green short worm", "i")]
    for x in testing:
        print(myTestString(countLetters, x))
    
    print()
    print("testing countLetters2()")
    testing = [("aaabbbaaacccdddifkf;lkajsdf;lkjA", "b"), ("The quick brown fox jumped very lazily over the green short worm", "i")]
    for x in testing:
        print(myTestString(countLetters2, x))