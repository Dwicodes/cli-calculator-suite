import math

def evaluate_expression(expression):
    try:
        # Replace ^ with ** for exponentiation
        expression = expression.replace('^', '**')
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except Exception:
        return "Invalid expression!"

def main():
    print("Advanced Calculator (supports +, -, *, /, %, ^ and expressions like 3 + 2 * 5)")
    while True:
        expression = input("Enter expression (or type 'exit'): ")
        if expression.lower() == 'exit':
            print("Exiting...")
            break
        result = evaluate_expression(expression)
        print("Result:", result)

if __name__ == "__main__":
    main()
