def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

        choice = input("Choose operation (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input!")
            continue

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
