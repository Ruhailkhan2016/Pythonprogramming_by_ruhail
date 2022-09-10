# Dictionary is a unordered squence of items. it is a mutable data type. dictionary have key and values pair. we can create dictionary with {} curly brackets

mobile = {

    "brand" : "Nokia",
    "Model" : "TA- 1053",
    "Year" : "2018"
 }


# access particular values of key 
# x = mobile["brand"]
# print(x)

# Change Method how to change key's values
# mobile['Year'] = '2019'
# print(mobile)

# length method 
# print(len(mobile))


# add Method 
# mobile["Color"] = "White"
# print(mobile)

# Remove Method 
# mobile.pop("Model")
# print(mobile)


# del Method 
# del mobile["Year"]
# print(mobile)

# clear Method 
# mobile.clear()
# print(mobile)


# Copy Mothod 

Phone = mobile.copy()
print(Phone)
print(mobile)