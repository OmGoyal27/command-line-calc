def add(num1: float, num2: float) -> float:
    return num1 + num2

def subtract(num1: float, num2: float) -> float:
    return num1 - num2

def multiply(num1: float, num2: float) -> float:
    return num1 * num2

def divide(num1: float, num2: float) -> float | str:  
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def power(num1: float, num2: float) -> float:
    return num1 ** num2

def modulo(num1: float, num2: float) -> float | str:
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 % num2

def square_root(num1: float, _: float = None) -> float | str:
    if num1 < 0:
        return "Cannot find square root of negative number"
    return num1 ** 0.5

def calculate(num1: float, num2: float, operation: str) -> float | str:
    match operation:
        case '+':
            return add(num1, num2)
        case '-':
            return subtract(num1, num2)
        case '*':
            return multiply(num1, num2)
        case '/':
            return divide(num1, num2)
        case '^':
            return power(num1, num2)
        case '%':
            return modulo(num1, num2)
        case 'sqrt':
            return square_root(num1)
        case _:
            return "Invalid operation"
        
operations = ['+', '-', '*', '/', '^', '%', 'sqrt']

def parse_input(user_input: str) -> tuple[float | str, float | str | None, str]:
    """Parse the user input and return num1, num2, and operation"""
    user_input = user_input.strip()
    
    # Handle special case for square root
    if user_input.startswith("sqrt "):
        try:
            num = float(user_input.split()[1])
            return num, None, "sqrt"
        except (ValueError, IndexError):
            return "Invalid input", None, "error"
    
    # Look for operation in input
    operation = None
    for op in operations:
        if op in user_input and op != "sqrt":  # Already handled sqrt above
            operation = op
            break
    
    if not operation:
        return "Invalid operation", None, "error"
    
    # Split input by operation
    parts = user_input.split(operation)
    if len(parts) != 2:
        return "Invalid input format", None, "error"
    
    try:
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return num1, num2, operation
    except ValueError:
        return "Invalid numbers", None, "error"

def main():
    print("=== Advanced Command Line Calculator ===")
    print("Supported operations: + - * / ^ % sqrt")
    print("Examples: 5 + 3, 10 / 2, 2 ^ 3, sqrt 16")
    print("Type 'exit' to quit, 'history' to see past calculations")
    
    history = []
    
    while True:
        user_input = input("\nEnter calculation: ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the calculator!")
            break
        
        if user_input.lower() == 'history':
            if not history:
                print("No calculations in history")
            else:
                print("\n=== Calculation History ===")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            continue
        
        num1, num2, operation = parse_input(user_input)
        
        if operation == "error":
            print(f"Error: {num1}")
            continue
            
        result = calculate(num1, num2, operation)
        
        if operation == "sqrt":
            display = f"sqrt({num1}) = {result}"
        else:
            display = f"{num1} {operation} {num2} = {result}"
            
        print(result)
        history.append(display)

if __name__ == "__main__":
    main()