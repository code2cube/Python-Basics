while True:
    ask = input("Type one of the following: add, subtract, multiply, divide\n")

    num1 = input("What is the first number?\n")
    num2 = input("What is the second number?\n")
    end = "--------------------------------------------------------"
    credit = "Created by live2cube#0069"

    if str(ask) == "add":
        num1
        num2
        calc = float(num1) + float(num2)
        print(f"The total is {calc}")
        print(end)
        print(credit)
        print(end)

    if str(ask) == "subtract":
        num1
        num2
        calc = float(num1) - float(num2)
        print(f"The difference is {calc}")
        print(end)
        print(credit)
        print(end)

    if str(ask) == "multiply":
        num1
        num2
        calc = float(num1) * float(num2)
        print(f"The product is {calc}")
        print(end)
        print(credit)
        print(end)

    if str(ask) == "divide":
        num1
        num2
        calc = float(num1) / float(num2)
        print(f"The quotent is {calc}")
        print(end)
        print(credit)
        print(end)
