num = int(input("Enter a number to check it is prime or not :"))

if num > 1:

    for i in range(2, num):

        if(num % i == 0):

            print(num, "is not prime")
            break
    else:

        print(num, " is prime")

else:

    print(num, "Number is not prime")