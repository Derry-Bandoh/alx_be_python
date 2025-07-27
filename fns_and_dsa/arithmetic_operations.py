"""Module providing a function for arithmetic operations"""
def perform_operation (num1 ,num2 ,operation) :
    match operation:
        case x if x == "add":
            results = num1 + num2
            
        case x  if x == "subtract":
            results = num1 - num2
            
        case x if x == "multiply":
            results = num1 * num2 
            
        case x if x == "divide":
            if num2 == 0:
                results = "Cannot divide by zero"
                
            else:
                results = num1 / num2 
                
        case _:
            results = "Invalid response"
    return results