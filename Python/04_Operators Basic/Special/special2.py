list1=["one","two","three"]
list2=["one","two","three"]

print(id(list1))
print(id(list2))

print(list1 is list2)                   #in Operator : Returns True if the given object present in the specified Collection

print(list1 is not list2)              #not in Operator : not in 🡺 Retruns True if the given object not present in the specified Collection 
print(list1 == list2) 


# output 
# ruhail@ruhail-Vostro-15-3568:/media/ruhail/1A78EFB678EF8EB7/Programming/Python/04 Operators Basic/Special$ python3 special2.py 
# 140021561779008
# 140021561856064
# False
# True
# True