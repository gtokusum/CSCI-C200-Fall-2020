import a2_assignment
import unittest

print("__________________________________________")
print("KEY")
print(". = passed")
print("F = failed on value") 
print("0 = unrecoverable error")
print("__________________________________________")


class TestA1(unittest.TestCase):
    def test_speed(self):
        for i,j in zip([25,35,45,70],[-5,0,0,5]):
            self.assertEqual(a2_assignment.speed(i),j)

    def test_F_C(self):
        for i,j in zip([-10,0,30,80],[14.0,32.0,86.0,176.0]):
            self.assertEqual(a2_assignment.F_C(i),j)

    def test_max(self):
        for i,j,k in zip([1,2,3],[3,2,1],[3,2,3]):
            self.assertEqual(a2_assignment.max(i,j),k)
 
    def test_ave(self):
        x = [5, 42, 39, 12, 48, 45, 37, 25, 50]
        self.assertEqual(round(a2_assignment.ave(x),2),round(33.666666666666664,2))

    def test_max_list(self):
        x = [5, 42, 39, 12, 48, 45, 37, 25, 50]
        self.assertEqual(a2_assignment.max_list(x),50)

if __name__=="__main__":
    unittest.main()