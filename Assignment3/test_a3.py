import a3
import unittest

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")


class TestA3(unittest.TestCase):

    def test_y(self):
        self.assertEqual(a3.y(1000,0.02,10),1221.40275816017) 
        self.assertEqual(a3.y(500,1.4,5),548316.5792142292) 
        self.assertEqual(a3.y(7500,.09,3),9824.733380499354) 

    def test_M(self):
        self.assertEqual(a3.N(500,100,4),2.610734844882072e+176) 
        self.assertEqual(a3.N(250,30,2),2.8550184745392108e+28) 
        self.assertEqual(a3.N(100,14,1),120260428.41647768) 

    def test_N_t(self):
        self.assertEqual(a3.N_t(1000),72) 
        self.assertEqual(a3.N_t(75),69) 
        self.assertEqual(a3.N_t(50),54) 

    def test_K(self):
        self.assertEqual(a3.K(1),0.00692) 
        self.assertEqual(a3.K(2),0.00629) 
        self.assertEqual(a3.K(3),0.00495) 


    def test_r(self):
        self.assertEqual(a3.r(4),1219.53) 
        self.assertEqual(a3.r(5),1183.8) 
        self.assertEqual(a3.r(6),1158.17) 

    def test_p(self):
        self.assertEqual(a3.p(10),-1600) 
        self.assertEqual(a3.p(30),-400) 
        self.assertEqual(a3.p(50),4000) 

    def test_W(self):
        self.assertEqual(a3.W(10,1),5744) 
        self.assertEqual(a3.W(10,2),4015) 
        self.assertEqual(a3.W(20,1.5),6461) 

    def test_dep(self):
        self.assertEqual(a3.dep(20000,1000,5),3800.0) 
        self.assertEqual(a3.dep(10000,500,10),950.0) 
        self.assertEqual(a3.dep(40000,2000,3),12667.0) 

    def test_L(self):
        self.assertEqual(a3.L(33.8,512,0.515),995) 
        self.assertEqual(a3.L(30.8,512,0.515),826) 
        self.assertEqual(a3.L(25.8,512,0.515),580) 

    def test_q(self):
        self.assertEqual(a3.q(1,3,-4),(1.0,-4.0)) 
        self.assertEqual(a3.q(2,-4,3),(1+0.7071067811865476j,1-0.7071067811865476j)) 
        self.assertEqual(a3.q(9,12,4),(-0.6666666666666666, -0.6666666666666666)) 
        self.assertEqual(a3.q(3,4,2),(-0.6666666666666666+0.47140452079103173j, -0.6666666666666666-0.47140452079103173j)) 
    
    def test_checkout(self):
    
        x1 = [[1, 1.45, 1],[3, 4.24, 1], [2, 14.00, 0], [4, 1.25, 1]]
        x2 = [[3, 2.05, 1],[1, 4.74, 0], [2, 4.00, 1], [5, 4.25, 1]]
        x3 = [[1, 2.05, 0],[1, 4.74, 1], [2, 4.00, 0], [5, 4.25, 0]]
    
        self.assertEqual(a3.checkout(x1),48.51) 
        self.assertEqual(a3.checkout(x2),42.62) 
        self.assertEqual(a3.checkout(x3),36.37)    

    def test_e(self):

        s1 = [[1,0,0],[1,1,1],[1,1,0]]
        s2 = [[1]]
        s3 = [[0]]
        s4 = [[1,1],[1,1],[1,1],[1,0]]
        s5 = [[1],[0],[0]]
    
        self.assertEqual(a3.e(s1),3) 
        self.assertEqual(a3.e(s2),0) 
        self.assertEqual(a3.e(s3),1) 
        self.assertEqual(a3.e(s4),1) 
        self.assertEqual(a3.e(s5),2) 


if __name__=="__main__":
    unittest.main()

"""

    print(y(1000,0.02,10))
print(y(500,1.4,5))
print(y(7500,.09,3))
"""