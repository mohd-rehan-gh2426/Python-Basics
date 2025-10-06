#1.String :

# String can be enclosed in "" or ''

#2.Numbers :

# There are two types of number:
"""
Integers.
Floating Point numbers
"""

#3.Boolean : True or False

#4.List : Collection of items:

"""
=> Enclosed with [] brackets.
=> The items in the list can be of any datatype.
=> A list contains the items of different datatypes in single list as well.
=> list is mutable
"""
# fruits = ['aam','kela','angur',2]
# fruits[2] = 1 # changing the item of a list
# print(fruits)

#5.Tuple 

"""
=> Enclosed with () brackets.
=> Tuples are immutable
=> The items in the tuple can be of any datatype.
=> A tuple contains the items of different datatypes in single tuple as well.

"""

# veggies = ('kanda','aaloo','began',1,2,3)
# # veggies[2] = 0 #this line will throw an error
# print(veggies)

#6.Dictionary : It is a collection of key and value pairs.
"""
=> All the immutable dataypes in python can become the keys in dictionary, 
mutable datatypes can't become the keys in dictionary in python


"""

# employDict = {
#     "name" : "Rehan",
#     "exp" : 2,
#     "isMarried" : False
# }

# print(employDict)


#7.Set : it is an unordered Collection of uninque items.

"""
=> Enclosed with {}.
=> Allow only duplicate value
"""

test_set = {'rehan',2,'pani',4,True,6,'soap','rehan',4}
print(test_set)