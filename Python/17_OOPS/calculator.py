class Calculator:

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def add(self):

        return self.a + self.b
    
    def sub(self):

        return self.a - self.b
    
    def mul(self):

        return self.a * self.b
    
    def divide(self):

        return self.a / self.b



a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
result = Calculator(a, b)

choice = 1
while(choice != 5):

    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


    choice = int(input("Enter your Choice : "))
    if (choice == 1):
        print("Addition of two number is : ", result.add())

    elif (choice == 2):
        print("Subtraction of two number is : ", result.sub())

    elif (choice == 3):
        print("Multiplication of two number is : ", result.mul())

    elif (choice == 4):
        print("Division of two number is : ", result.divide())
    

    elif (choice == 5):
        print("Thanks for Using Calculator!")

    else:

        print("Wrong Choice!!")
