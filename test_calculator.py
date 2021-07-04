

import unittest
from basic_calculator import calculator

class CalculatorTestCase(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculator().add(1, 2), 3, "Expected 3") 
        self.assertEqual(calculator().add(-67.91, 7687), 7619.09, "Expected 7619.09")
        self.assertEqual(calculator().add(140000, -2679.8477), 137320.1523, "Expected 137320.1523")
        
    def test_subtraction(self):
        self.assertEqual(calculator().subtract(4, 2), 2, "Expected 2") 
        self.assertEqual(calculator().subtract(-357723, 4566.2736), -362289.2736, "Expected -362289.2736") 
        self.assertEqual(calculator().subtract(6336.38628, 23827.532753), -17491.146473, "Expected -17491.146473") 
        
    def test_multiplication(self):
        self.assertEqual(calculator().multiply(4, 2), 8, "Expected 8") 
        self.assertEqual(calculator().multiply(3726382.732573, 236821.73636), 882488429069.8594, "Expected 882488429069.8594") 
        self.assertEqual(calculator().multiply(-23734.721, 63822.12546), -1514800341.4200969, "Expected -1514800341.4200969") 
    
    def test_division(self):
        self.assertEqual(calculator().divide(4, 2), 2, "Expected 2") 
        self.assertEqual(calculator().divide(62253.5326, 2636.7382638), 23.610053927112887, "Expected 23.610053927112887") 
        self.assertEqual(calculator().divide(-632734, 286382.62126), -2.209400826126093, "Expected -2.209400826126093") 
        

if __name__ == '__main__':
    unittest.main()