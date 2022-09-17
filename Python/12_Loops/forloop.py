# Use of forloop 
# hardware = ['Monitor', 'Pointer', 'Mouse']

# for i in hardware:

#     print(i)


# forloop range function//         print table using range function
start = int(input("Enter Starting Point : "))
end = int(input("Enter ending Point : "))
skip = int(input("Enter skiping Point : "))

print(start, "table is : ")
for i in range(start, end, skip):
    print(i)