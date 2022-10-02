#palindrom number program for integer

# num = int(input("Enter number to check it is palindrome : "))

# temp = num
# reverse = 0

# while(num>0):

#     dig = num % 10
#     reverse = reverse * 10 + dig
#     num = num // 10

# if(temp == reverse):

#     print(temp, "Is palindrom")

# else: 

#     print(temp, "Is not plaindrom")



#palindrom number program for string

num = input("Enter any string to check it is plindrome : ")
reverse = num[::-1]


if (num == reverse):

    print("it is palindrome")

else:

    print("it is not palindrome")
