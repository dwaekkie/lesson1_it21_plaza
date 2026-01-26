print("Welcome to the Calculator!")
while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    op = input("Choose operation (+, -, *, /) or q to quit: ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        prit("Result:", num1 - num2)

