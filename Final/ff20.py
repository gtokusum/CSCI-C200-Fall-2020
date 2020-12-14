
# #######################
# Problem One
# #######################

import numpy as np
from numpy import linalg as LA

def convergence(matrix, vector, tau):
    """
    TODO: Complete the function

    Parameters:
    - matrix: 2-D numpy array
    - vector: An array (1-D) 
    - tau: numerical value
    """
    exp = 2
    a = matrix
    b = vector
    current = np.matmul(a,b)
    last = b
    t = tau
    while abs(LA.norm(current-last))>t:
        last = current
        current = np.matmul(a,current)
        # exp += 1
    return current
    
if __name__=="__main__":
    print("Problem 1")
    a = np.zeros((4,4,), dtype = float)

    rows = [[0,0,1,1/2],[1/3,0,0,0],[1/3,1/2,0,1/2],[1/3,1/2,0,0]]
    for r in range(4):
        for c in range(4):
            a[r][c] = rows[r][c]
    b = np.array([.25,.25,.25,.25])

    print(convergence(a,b,.002))


    
########################
#Problem Two
########################
class stack:
    """
    DO NOT MODIFY, only use this class
    """
    def __init__(self):
        self.s = []
    def push(self,item):
        self.s = [item] + self.s
    def empty(self):
        return self.s == []
    def pop(self):
        item = self.s[0]
        self.s = self.s[1:]
        return item

    def size(self):
        return len(self.s)

class RPS_calculator:
    def __init__(self, exp):
        """
        TODO: complete the constructor

        Parameter: A string representing RPN
        No return statement
        """
        self.exp = exp.split()
        # super().__init__('RPS_calculator')
        
        
    def run(self):
        """
        TODO: complete the function

        Parameter: No parameters
        Returns: A numberical value from the expression
        """
        x = stack()
        ops = {"+":(lambda a,b:a+b),"-":(lambda a,b:a-b),"*":(lambda a,b: a*b),"/":(lambda a,b: a/b),"abs":(lambda a: abs(a))}
        for i in self.exp:
            if i in ops:
                if i != 'abs':    
                    b = x.pop()
                    a = x.pop()
                    result = ops[i](a,b)
                    x.push(result)
                else:
                    a = x.pop()
                    result = ops[i](a)
                    x.push(result)
            # if i == 'abs':
            #     c = x.pop()
            #     result = ops[i](c)
            else:
                x.push(int(i))
        return x.pop()
                

    def __str__(self):
        """
        DO NOT MODIFY
        """
        return str(self.calc)


if __name__=="__main__":
    print("\n"*3)
    print("Problem 2")
    RPSlist = ["3 1 2 + *", "4 2 5 * + 1 3 2 * + /", \
           "3 4 + 5 2 - *", "-2 -2 *", "-200 abs 2 /"]
    for rpn in RPSlist:
        x = RPS_calculator(rpn)
        print("RPN:", rpn, "\t Run:",  x.run())      





# #######################
# Problem Three
# #######################

import sqlite3


def createTable():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    Example: Complete the creating of a table
    NOTE: DO NOT MODIFY **THIS** Function
    """
    return "CREATE TABLE G (X text, Y text, Value real)"


def insert1():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the insert statement for row 1 of the table
    """
    return "INSERT INTO G VALUES('A','B',1)" 

def insert2():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the insert statement for row 2 of the table
    """
    return "INSERT INTO G VALUES('A','C',2)"

def insert3():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the insert statement for row 3 of the table
    """
    return "INSERT INTO G VALUES('A','D',5)"

def insert4():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the insert statement for row 4 of the table
    """
    return "INSERT INTO G VALUES('B','D',3)"

def insert5():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the insert statement for row 5 of the table
    """
    return "INSERT INTO G VALUES('C','D',5)"


def query1():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 1
    """
    return "SELECT * FROM G"

def query2():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 2
    """
    return "SELECT * FROM G WHERE Value > 2"

def query3():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 3
    """
    return "SELECT * FROM G WHERE Value = 2"

def query4():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 4
    """
    return "SELECT X,Y,Y,sum(Value) FROM G WHERE Value = 2"

def query5():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 5
    """
    return "SELECT SUM(Value)/COUNT(Value) FROM G"

def query6():
    """
    THIS FUNCTION ONLY RETURNS A STRING. 
    Do NOT call any `sqlite3` functions here

    TODO: Complete the QUERY 6
    """
    return "SELECT X,Y FROM G WHERE Value > (SELECT AVg(Value) FROM G) "


if __name__=="__main__":
    ####
    # DO NOT MODIFY CODE IN THIS SECTION
    # No code will be graded in this section
    #
    # All code must be answered in the functions above
    ####
    print("\n"*3)
    print("Problem 3")
    connection = sqlite3.connect("final.db")
    my_cursor = connection.cursor()
    my_cursor.execute("DROP TABLE IF EXISTS G")
    my_cursor.execute(createTable())   

    my_cursor.execute(insert1())
    my_cursor.execute(insert2())
    my_cursor.execute(insert3())
    my_cursor.execute(insert4())
    my_cursor.execute(insert5())
    connection.commit()


    #QUERY 1 Select All the tuples
    print("Query 1")
    for i in my_cursor.execute(query1()):
        print(i)

    print("*"*30)
    #QUERY 2 Select All the edges greater than 2
    print("Query 2")
    for i in my_cursor.execute(query2()):
        print(i)

    print("*"*30)
    #QUERY 3 Select All the paths of length 2
    print("Query 3")
    for i in my_cursor.execute(query3()):
        print(i)

    print("*"*30)
    #QUERY 4 Select the path of length
    # 2 that has the greatest sum and display the sum
    print("Query 4")
    for i in my_cursor.execute(query4()):
        print(i)

    print("*"*30)
    #QUERY 5 Give the average of the edge weights
    print("Query 5")
    for i in my_cursor.execute(query5()):
        print(i)


    print("*"*30)
    #QUERY 6 Give the edges whose values are greater than the average weight
    print("Query 6")
    for i in my_cursor.execute(query6()):
        print(i)


    connection.close()
