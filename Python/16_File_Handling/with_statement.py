# with the help of with statement you don't need to close the file it automatically close when you use with statement

with open("demo.txt", 'r') as f:

    a = f.read()
    print(a)