class Calculator:

    def add(self, a, b):

        self.a = a
        self.b = b

        return a+b


sum = Calculator()

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

result = sum.add(a, b)

print("Total is : ", result)
