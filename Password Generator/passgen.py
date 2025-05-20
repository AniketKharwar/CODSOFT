import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = list(string.ascii_lowercase)
    
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not chars:
        return "⚠️ You need to choose at least one character type!"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def yes_or_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("❗ Please type 'y' or 'n'.")

def main():
    print("🔐 Welcome to Password Generator \n")

    try:
        length = int(input("🔢 How long do you want your password to be? (e.g., 12): "))
        if length <= 0:
            print("❌ Password length must be a positive number.")
            return
    except ValueError:
        print("❌ That doesn't look like a valid number.")
        return

    use_upper = yes_or_no("🔠 Include UPPERCASE letters?")
    use_digits = yes_or_no("🔢 Include numbers?")
    use_symbols = yes_or_no("🔣 Include special symbols?")

    password = generate_password(length, use_upper, use_digits, use_symbols)

    print("\n✅ Here's your secure password:")
    print(f"👉 {password}")
    print("📌 Don't forget to copy and store it somewhere")

if __name__ == "__main__":
    main()
