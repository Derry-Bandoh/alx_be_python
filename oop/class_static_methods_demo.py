class Calculator:
    """
    A class demonstrating the use of class methods and static methods.
    
    This class contains both @staticmethod and @classmethod examples
    to show their differences and appropriate use cases.
    """
    
    # Class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to 'self' or 'cls' and behave like
        regular functions but belong to the class's namespace.
        
        Args:
            a (float/int): First number
            b (float/int): Second number
            
        Returns:
            float/int: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to the class (cls) and can access
        class attributes and other class methods.
        
        Args:
            cls: Reference to the class itself
            a (float/int): First number
            b (float/int): Second number
            
        Returns:
            float/int: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b