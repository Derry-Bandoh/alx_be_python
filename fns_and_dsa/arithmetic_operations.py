"""
Module for performing basic arithmetic operations.

This module provides a function to perform addition, subtraction, 
multiplication, and division operations on two numbers.
"""

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float or str: The result of the arithmetic operation, or an error message for division by zero
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        case _:
            return "Invalid operation"

            

            
