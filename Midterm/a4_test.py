import a4_exam
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

x1 = []
x2 = [1,0,0,1]
x3 = [1,2,3,4,0]
x4 = [5]
x5 = [-1,0,2,2,0,-1]

x = [x1,x2,x3,x4,x5]
y = [(), (0, 2), (0, 1), (5, 1), (-1, 2)]
p = {'Act': 63746.04999999999, 'gold': 4, 'silver': 20, 'platinum': 5, 'paladium': 10}

class MyTester(unittest.TestCase):

    def test_my_range(self):
        self.assertEqual(a4_exam.my_range(1,7,3),[1,4]) 
        self.assertEqual(a4_exam.my_range(7,0,3),[]) 
        self.assertEqual(a4_exam.my_range(0,10,1),[0,1,2,3,4,5,6,7,8,9])

    def test_ASCII_triangle(self):
        self.assertEqual(a4_exam.ASCII_triangle(3)," *\n***\n")
        self.assertEqual(a4_exam.ASCII_triangle(5),"  *\n ***\n*****\n")
    
    def test_ASCII_square(self):
        self.assertEqual(a4_exam.ASCII_square(2),"**\n**\n")
        self.assertEqual(a4_exam.ASCII_square(0),"")


    def test_how_much(self):
        self.assertEqual(a4_exam.how_much(a4_exam.portfolio,a4_exam.Au),52.0)
        self.assertEqual(a4_exam.how_much(a4_exam.portfolio,a4_exam.Ag),4127.0)
        self.assertEqual(a4_exam.how_much(a4_exam.portfolio,a4_exam.Pd),42.0)
        self.assertEqual(a4_exam.how_much(a4_exam.portfolio,a4_exam.Pt),109.0)


    def test_purchase(self):
        a4_exam.purchase(a4_exam.portfolio,a4_exam.Au,2)
        a4_exam.purchase(a4_exam.portfolio,a4_exam.Ag,20)
        a4_exam.purchase(a4_exam.portfolio,a4_exam.Pt,5)
        a4_exam.purchase(a4_exam.portfolio,a4_exam.Pd,10)
        a4_exam.purchase(a4_exam.portfolio,a4_exam.Au,2)
        self.assertEqual(a4_exam.portfolio, p)
        self.assertEqual(a4_exam.worth(a4_exam.portfolio), 100000)

    def test_find_num_min(self):
            for i,j in zip(x,y):
                self.assertEqual(a4_exam.find_num_min(i), j)

if __name__=="__main__":
    unittest.main()

