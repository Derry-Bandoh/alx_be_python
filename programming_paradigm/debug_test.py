from simple_calculator import SimpleCalculator

# Test basic instantiation and method call
calc = SimpleCalculator()
print("Calculator created successfully")

try:
    result = calc.add(2, 3)
    print(f"2 + 3 = {result}")
except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e)}")