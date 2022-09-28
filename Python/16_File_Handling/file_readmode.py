# Two types of file in python -
# 1. Text files (Ex. bxt)
# 2. Binary files (jpg, .dat)
# Python has several functions for reating, reading, updating, and deleting files.

# Read Default value. Opens a file for reading,
# error if the file does not exist

# "a"-Append Opens a file for appending, creates the file if it does not exist
# "w Write Opens a file for writing, creates the file if it does not exist
# "x" Create Creates the specified file, returns an error if the file exists




# Reading mode

# f = open('16_File_Handling/file.txt', 'r')
# myfile = f.read()
# print(myfile)
# f.close()




# read for given partcular range 
# f = open('16_File_Handling/file.txt', 'r')
# myfile = f.read(10)
# print(myfile)
# f.close()



# read line by line using readline() function
# f = open('16_File_Handling/file.txt', 'r')
# myfile = f.readline()
# print(myfile)
# f.close()




# read whole file content using for loop

f = open('16_File_Handling/file.txt', 'r')

for i in f:
    print(i)
