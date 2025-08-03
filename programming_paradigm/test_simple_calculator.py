import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        
        # Test negative and positive
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        
        # Test negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(-2, 3), -5)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        
        # Test decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the division method."""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        
        # Test division resulting in decimal
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 2), -3.0)
        self.assertEqual(self.calc.divide(6, -2), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Test decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

if __name__ == "__main__":
    unittest.main()