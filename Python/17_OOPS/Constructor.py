class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

        print("Total is : ",a+b)


a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

sum = Calculator(a, b)

