import ff20
import unittest
import numpy as np
from numpy import linalg as LA

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

class MyTester(unittest.TestCase):

    def test_convergence(self):
        b = np.array([.25,.25,.25,.25])
        zz = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        self.assertEqual(list(ff20.convergence(zz,b,1)),list(b))

    def test_RPN_calculator(self):
        RPSlist = [ "3 1 2 + *", "4 2 5 * + 1 3 2 * + /", \
                    "3 4 + 5 2 - *", "-2 -2 *", "-200 abs 2 /"]
        V = [9.0,2.0,21.0,4.0,100.0]
        for rpn,v in zip(RPSlist,V):
            x = ff20.RPS_calculator(rpn).run()
            self.assertEqual(x,v)

if __name__=="__main__":
    unittest.main()

