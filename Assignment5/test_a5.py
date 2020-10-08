import a5
import unittest
import random as rn

print("__________________")
print("KEY")
print(". passed")
print("F,0,E did not pass")
print("__________________")

s1 = ['a','b','a','b','a','b','b','b']
s2 = [(1),(2),(3),(4)]
s3 = [1]
s4 = [1,2]
xlst = [s1,s2,s3,s4]
p1 = [0.375, 0.625]
p2 = [0.25, 0.25, 0.25, 0.25]
p3 = [1.0]
p4 = [0.5, 0.5]
plst = [p1,p2,p3,p4]
elst = [0.9544340029249649, 2.0, -0.0, 1.0]
test = []
for i in range(10):
    test.append(rn.randint(0,100))
s_list = sorted(test)

lrx1 = [0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1]
lrx2 = [0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0]

ms1 = [[4, 9, 2],[3,5,7],[8,1,6]]
ms2 = [[4, 9, 2],[3,5,7],[8,2,6]]

class MyTester(unittest.TestCase):

    def test_makeProbability(self):
        for i,j,k in zip(xlst, plst, elst):
            self.assertEqual(a5.makeProbability(i),j)
            self.assertEqual(a5.entropy(a5_s.makeProbability(i)),k)
    def test_magic(self):
            x = rn.randint(1,50)
            self.assertEqual(a5.magic(x),x)
    def test_occurrs_w(self):
            self.assertEqual(a5.occurs_w(1,[2]),False)                         
            self.assertEqual(a5.occurs_w(2,[3,2]),True)
    def test_occurrs_r(self):
            self.assertEqual(a5.occurs_r(1,[2]),False)                         
            self.assertEqual(a5.occurs_r(2,[3,2]),True)
    def test_remove_allw(self):
            self.assertEqual(a5.remove_allw(1,[1,1,2,1,2]),[2,2])
            self.assertEqual(a5.remove_allw(3,[1,1,2,1,2]),[1,1,2,1,2])
    def test_remove_allr(self):
            self.assertEqual(a5.remove_allr(1,[1,1,2,1,2]),[2,2])
            self.assertEqual(a5.remove_allr(3,[1,1,2,1,2]),[1,1,2,1,2])
    def test_bubble_sort(self):
            self.assertEqual(a5.bubble_sort(test),s_list)
    def test_rec_sort(self):
            self.assertEqual(a5.rec_sort(test),s_list)
    def test_lr(self):
            self.assertEqual(a5.lr(lrx1),6)
            self.assertEqual(a5.lr(lrx2),4)
    def test_is_magic(self):
            self.assertEqual(a5.is_magic(ms1), True)
            self.assertEqual(a5.is_magic(ms2), False)
            


if __name__=="__main__":
    unittest.main()

