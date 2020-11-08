import as9
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

class MyTester(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(as9.distance((4,0),(0,3)), 5)
        self.assertAlmostEqual(as9.distance((20, 10), (42, 45)), 41.340053217188775)

    def test_brute(self): 
        x = [(5,5),(50,50),(75,75),(4,4)]  
        y = sorted(as9.brute(x)[0:2])
        self.assertEqual(y, [(4, 4), (5, 5)])

    def test_productivity(self):
        self.assertAlmostEqual(as9.productivity(55),883.30,1)
      
    def test_Vector2D(self):
        x = as9.Vector2D(1,2)
        y = as9.Vector2D(4,-1)
        z = x + y
        self.assertEqual(z, as9.Vector2D(5,1))
        self.assertEqual(x * y, 2)
        self.assertEqual(x - y, as9.Vector2D(-3,3))
        self.assertAlmostEqual(abs(x), 2.236, 1)
        self.assertEqual(x.scalar_mul(5), as9.Vector2D(5,10)) 
        self.assertEqual(-x, as9.Vector2D(-5,-10))
        self.assertEqual(x == z, False)
        self.assertEqual(as9.Vector2D(1,1) == as9.Vector2D(1,1), True)
        

    def test_MyComplexNumber(self):
        
        x1 = as9.MyComplexNumber(3,-1) #3-i
        x2 = as9.MyComplexNumber(1,4)  #1+4i
        x3 = as9.MyComplexNumber(-3,1) #-3+i
        x4 = as9.MyComplexNumber(2,-4) #2-4i
        x5 = as9.MyComplexNumber(-2,1)
        x6 = as9.MyComplexNumber(1,2)
        x7 = as9.MyComplexNumber(0,3) 
        x8 = as9.MyComplexNumber(-1,-1)
        x9 = as9.MyComplexNumber(1,-1)
        x10 = as9.MyComplexNumber(4,-3)
        x11 = as9.MyComplexNumber(3,2)
        x12 = as9.MyComplexNumber(1,1)
        r = (x1 + x2).get_real()
        i = (x1 + x2).get_imag()
        self.assertEqual([r,i], [4,3])
        r = (x1 * x2).get_real()
        i = (x1 * x2).get_imag()
        self.assertEqual([r,i], [7,11])
        r = (x5/x6).get_real()
        i = (x5/x6).get_imag()
        self.assertEqual([r,i],[0.0, 1.0])
        self.assertEqual(x10.modulus(),5.0)
        rho = x12.polar()[0]
        theta = x12.polar()[1] 
        self.assertAlmostEqual(rho, 1.414, 1)
        self.assertEqual(theta, 45.0)









if __name__=="__main__":
    unittest.main()

