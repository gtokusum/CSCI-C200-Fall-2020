"""
This is test code. You do not need to modify any of this code. 

You do not need to priortize understanding this code, as this will be beyond you level at the moment. 
We needed to create this code in order to help automate code checking
"""

from lab2 import *


functions = [warping, driving_time, driving_speed, 
             driving_distance, race, most_distance, most_speed, whichAssingmentToWorkOn,
             didIMakeHonorRoll, gradeToGetAnA, squarea, midlist, twenty_four_twelve, speed, 
             distance, time, hours_to_min, min_to_sec, feet_to_mile, miles_to_kilometers, 
             k_to_m, miles_to_feet, degrees_to_radians, loc_c, c_to_f, f_to_c, k_to_f, 
             pc, p_to_k, ly_to_p]

inputValues = {
    "warping": [(0,), (41.0,),(10.2,), (1111,)],
    "driving_time": [(30,5,),(10,2,),(45,3,)],
    "driving_speed": [(30,10,),(50,5,),(100,22,)],
    "driving_distance": [(40,3,),(20,20,),(80,7,)],
    "race": [(5,50,6,60,),(5,25,4,60,)],
    "most_distance": [(5,50,6,60,),(5,25,4,60,)],
    "most_speed": [(5,50,6,60,),(5,25,4,60,)],
    "whichAssingmentToWorkOn": [[("Math",3,),("History",5,),("Computer Science",1,)],[("Art",10),("Music",3),("Lego Building",7)],[("History of Japanese Literature",1),("History of US Literature",3),("History Polish Literature",30)]],
    "didIMakeHonorRoll": [(3.4,12,"B-",),(2.0,14,"D",),(3.8,15,"B+",)],
    "gradeToGetAnA": [(.83,.20,),(.90,.10,),(.70,.35,)],
    "squarea": [(20,1,),(23,5,),(33,8)],
    "midlist": [((30,20,10,),),((23,24,10,11,14,),),((45,88,15,36,18,44,848,66,),)],
    "twenty_four_twelve": [(8,'pm',),(11,'am',),(3,'pm',)],
    "speed": [(20,13,),(10,11,),(42,68,)],
    "distance": [(243,21,),(110,123,),(79,11,)],
    "time": [(12,22,),(123,341,),(11,41,)],
    "hours_to_min": [(10,),(23,),(234,)],
    "min_to_sec": [(61,),(33,),(132,)],
    "feet_to_mile": [(5256,),(10_546,),(11_550_634,)],
    "miles_to_kilometers": [(458,),(12,),(789,)],
    "k_to_m": [(3212,),(4321,),(5321,)],
    "miles_to_feet": [(321,),(112,),(532,)],
    "degrees_to_radians": [(2341,),(6432,),(2102,)],
    "loc_c": [(34,13,82,),(11,3,67,),(12,35,55,)],
    "c_to_f": [(23,),(11,),(66,)],
    "f_to_c": [(77,),(91,),(100,)],
    "k_to_f": [(293,),(345,),(527,)],
    "pc": [(170.90,-3.31,),(100.2,2.5,),(600.7,-7.3,)],
    "p_to_k": [(50,),(350,),(280,)],
    "ly_to_p": [(100,),(300,),(420,)]
}

expectedOutputValues = {
    "warping": [0, 3, 2, 8],
    "driving_time": [6.0,5.0,15.0],
    "driving_speed": [3.0,10.0,4.545454545454546],
    "driving_distance": [120,400,560],
    "race": [-1,1],
    "most_distance": [1,1],
    "most_speed": [-1,0],
    "whichAssingmentToWorkOn": ["Computer Science","Music","History of Japanese Literature"],
    "didIMakeHonorRoll": [False,False,True],
    "gradeToGetAnA": [1.33,1.2,1.3571428571428574],
    "squarea": [20,115,264],
    "midlist": [20,10,18],
    "twenty_four_twelve": [20,11,15],
    "speed": [1.5384615384615385,0.9090909090909091,0.6176470588235294],
    "distance": [5103,13530,869],
    "time": [1.8333333333333333,2.772357723577236,3.727272727272727],
    "hours_to_min": [600,1380,14040],
    "min_to_sec": [3660,1980,7920],
    "feet_to_mile": [0.9954545454545455,1.9973484848484848,2187.6200757575757],
    "miles_to_kilometers": [737.07772,19.31208,1269.76926],
    "k_to_m": [1995.8492301191793,2684.951595063815,3306.3243317136216],
    "miles_to_feet": [1694880,591360,2808960],
    "degrees_to_radians": [40.85815778918725,112.25957748827528,36.686820876920805],
    "loc_c": [22.03372222462269,12.812993669947213,36.74797306981648],
    "c_to_f": [73.4,51.8,150.8],
    "f_to_c": [25.0,32.77777777777778,37.77777777777778],
    "k_to_f": [68.0,161.6,489.2],
    "pc": [-0.019368051492100635,0.024950099800399306,-0.012152488763109592],
    "p_to_k": [1.543e+38,1.0801e+39,8.640800000000001e+38],
    "ly_to_p": [30.67484662576687,92.02453987730063,128.83435582822088]
}




def getSolutions(testCases,answers,function):
    """
    Not used in this lab
    """
    print(f"------ TESTING {function.__name__}-------")
    print(f"[ {[function(*testCases[i]) for i in range(len(testCases))]} ]")
        #print(f": The answer should be -> {answers[i]}")


def functionOutput(function, inputParams, expectedOutputValue):
    """
    Given a function (the object), tuple of the input parameters, and the epected values.
    """
    testResult = function(*inputParams)
    if expectedOutputValue != testResult:
        print("\t{}{}".format(function.__name__, inputParams))
        print("\tExpected: {}\n\tReturned:{}\n".format(expectedOutputValue, testResult))
        return 0
    else:
        # print("\tOutput Matches")
        return 1

if __name__ == "__main__":
    finalString = "Overall Results:\n"
    for f in functions:
        result = 0
        print("Function: {}".format(f.__name__))
        iv = inputValues[f.__name__]
        eov = expectedOutputValues[f.__name__]
        for i in range(len(iv)):
            inputs = iv[i]
            outs = eov[i]
            result += functionOutput(f, inputs, outs)

        print("\t Number Complete: {}/{}".format(result, len(iv)))        
        finalString += "Function {}: {} / {}\n".format(f.__name__, result, len(iv))
        print("")
    
    print("\n\n\n")
    print(finalString)
            

