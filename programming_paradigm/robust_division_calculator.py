def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Args:
        numerator: The dividend (can be string or numeric)
        denominator: The divisor (can be string or numeric)
    
    Returns:
        String containing either the result or an appropriate error message
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        
        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."