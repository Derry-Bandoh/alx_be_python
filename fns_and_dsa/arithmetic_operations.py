def perform_operation (num1: float,num2: float,operation: str) :
    match operation:
        case x if x == "add":
            results = num1 + num2
            print(results)
        case x  if x == "subtract":
            results = num1 - num2
            print(results)
        case x if x == "multiply":
            results = num1 * num2 
            print(results)
        case x if x == "divide":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                results = num1 / num2 
                print(results)
        case _:
            print("Invalid response")
    return results

            

            
