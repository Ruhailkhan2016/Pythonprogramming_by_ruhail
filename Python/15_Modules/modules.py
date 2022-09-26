# Python Modules

# A module is a file containing functions which can be imported and used in our programs.
# You can use module by using two methods.
# Pre created module
# Using Built in modules -It is pre installed in python.
# Using External modules- You have to instal before using.


# Built in modules
# time module 
# import time;

# localtime = time.asctime(time.localtime(time.time()))

# print(localtime)



# calendar module 
# import calendar
# cal = calendar.month(2022, 8)
# print("\nCalender : \n", cal)



# Create own Module
# here we import our own module here.
import mymodule
# exp of square 
res = mymodule.sqrt(5)
print(res)


# exp of cube 
res = mymodule.cube(5)
print(res)