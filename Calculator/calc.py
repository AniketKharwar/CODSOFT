def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):e
    return a * b

def divide(a, b):
    if b == 0:
        return "⚠️ Can't divide by zero!"
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ That doesn't look like a number. Try again!")

def main():
    print("👋 Hey there! I'm your friendly calculator.")

    while True:
        print("\nWhat would you like to do?")
        print("➕ Add")
        print("➖ Subtract")
        print("✖️ Multiply")
        print("➗ Divide")
        print("❌ Exit")

        choice = input("\nType +, -, *, / or x to exit: ").strip()

        if choice.lower() == 'x':
            print("👋 Bye! Have a great day.")
            break
        elif choice in ['+', '-', '*', '/']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)

            print(f"\n✅ The result is: {result}")
        else:
            print("❓ I didn't understand that. Try using +, -, *, / or x.")

if __name__ == "__main__":
    main()
