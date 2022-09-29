# What is Exception?
# Exception is an abnormal condition in a program.


# Syntax
# try:
#   your main code.
# except Exception_name1:
#   code or you can print your own error message here.
# except Exception_name2:
#   code or you can print your own error message here.
# else:
#   if there is no exception then execute this block.




# class Calculator:
    
#     def display(self):
#         try:
#             self.a =  int(input("Enter First Number : "))
#             self.b =  int(input("Enter Second Number : "))
#             print("Total is : ",self.a/self.b)

#         except ValueError:
#             print("Error! Please Enter only Integer Value ")

#         except ArithmeticError:
#             print("Error! you are trying to divde wrong number")
    
# add = Calculator()
# add.display()


try:

    saving = 40000
    withdrawal = 30000

    if withdrawal>saving:
        raise Exception()
    
    else:
        cash = saving - withdrawal

except Exception:

    print("You have Insufficient Balance!")

else:

    print(withdrawal, "Has been debited")
    print("Your avalable balance is : ", cash)