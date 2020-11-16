import as10_solutions as as10
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

class MyTester(unittest.TestCase):

    def test_Binary(self):
        notNeeded = as10.Binary(16)
        self.assertEqual(notNeeded.d_to_b(17), 10001) # This is testing on 17 (not 16)
        x = as10.Binary(10)
        y = as10.Binary(5)
        z = x + y
        self.assertEqual(z, as10.Binary(10) + as10.Binary(5))
        z = (x - y).b_to_d()
        self.assertEqual(z, 5)
        z = y - x
        -z
        self.assertEqual(z.b_to_d(), 5)
        z = y * x
        self.assertEqual(z.b_to_d(), 50)
        z = as10.Binary(9)
        self.assertEqual(len(z), 4)
        -z
        self.assertEqual(len(z), 4)
        x = as10.Binary(12) #1100
        y = as10.Binary(5)  #0100
        self.assertEqual((x & y).b_to_d(), 4)
        w = -z
        self.assertEqual(w, abs(z))
        
    def test_hd(self):
        l1 = (51.5007, 0.1246)
        l2 = (40.6892, 74.0445)
        self.assertAlmostEqual(as10.hd(l1,l2), 3466.00895, 3)

    def test_MyLine(self):
        x1 = as10.MyLine((0,0), (5,5),options = "2pts")
        x2 = as10.MyLine((5,0),-1/4, options = "point-slope")
        x3 = as10.MyLine("(-4/5)*x + 5", options = "lambda")
        x4 = as10.MyLine("x + 2", options = "lambda")
        self.assertEqual(x1 * x2, (1.0, 1.0))
        self.assertAlmostEqual((x1 * x3)[0], 2.778, 3)
        self.assertAlmostEqual((x1 * x3)[1], 2.778, 3)
        self.assertEqual(x1 * x4, ())

    def test_f(self):
        x = [4,5,6]
        y = [2, 16,3]
        for i,j in zip(x,y):
            self.assertEqual(as10.f(i), j)

    def test_line(self):
        x = [1,2,3]
        y = [3,4,5]
        r1 = as10.mean(x),as10.mean(y)
        r2 = as10.sd(x), as10.sd(y)
        self.assertEqual(r1, (2.0, 4.0))
        self.assertEqual(r2,(1.0, 1.0))
        self.assertEqual(as10.r(x,y), 1.0)

if __name__=="__main__":
    unittest.main()

