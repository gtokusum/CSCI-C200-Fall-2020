#PROBLEM 1 a2_1
#INPUT speed s as integer
#RETURN change in speed as integer
def speed(s):
#TO DO Implement function
    SpeedValue = 1
    if s >= 55:
        SpeedValue = 5
    elif s < 55 and s > 30:
        SpeedValue = 0
    else:
        SpeedValue = -5
    return SpeedValue



#PROBLEM 2 a2_2
#INPUT temp in Fahrenheit float
#RETURN temp in Celcius float
def F_C(t):
#TO DO Implement function
    return t*1.8+32

#a2_3
#You cannot use Python's max function
#You must use if-statement
#INPUT two numbers
#RETURN maximum of the two
def max(x,y):
#TO DO Implement function
    if x > y:
        return x
    else:
        return y


#You cannot use Python's sum function
#You must use a bounded loop
#INPUT a non-empty list of numbers
#RETURN the average
def ave(xlst):
#TO DO Implement function
    AVERAGE = 0
    for i in xlst:
        AVERAGE += i
    return AVERAGE / len(xlst)

#You must use your max function
#You must use a bounded loop
#INPUT non-empty list of numbers
#RETURN maximum number in list
def max_list(xlst):
#TO DO Implement function
    maximum = 0
    for i in xlst:
        maximum = max(maximum,i)
    return maximum
    

