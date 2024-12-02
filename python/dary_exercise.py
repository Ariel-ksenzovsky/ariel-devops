# dictionaries
# #1
# my_dict = {
#     "name" : "Alice",
#     "age" : 25,
#     "city" : "New York"
# }

# print(my_dict)

# #2
# my_dict["job"] = "Engineer"

# print(my_dict)

# #3
# for key,value in my_dict.items():
#     print(f"{key} : {value}")

# #4
# def my_func(dictionary ,key):
#     for k,value in dictionary.items():
#         if k == key:
#             print(f"{value}")
        
# my_func(my_dict,"name")

# #5
# my_dict.pop("city")
# print(my_dict)


# functions
# 1

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Ariel"))

#2
# def greet(name = "Geust"):
#     return f"Hello, {name}!"

# print(greet())

# #3
# def add(a,b):
#     return a + b

# print(add(1,200))

# #4

# def factorial(x):
#     if x < 0:
#         return "error"
#     elif x == 0:
#         return 1
#     else:
#         return x*factorial(x-1)
    
# print(factorial(5))


# #5

# def doubled_numbers(*args):
#     doubled_list = []
#     for i in args:
#         doubled_list.append(i*2)
#     return doubled_list
        
# print(doubled_numbers(1,2,3,4,5,6))

#scope
#1
x = 10
# def print_number():
#     print(x)
    
# print_number()
# print(x)
#2
# def print_number():
#     print(x*2)
    
# print_number()
# print(x)

#3
# def num():
#     y = 10
#     print(y)
# num()
# print(y)

#4
# a = 12
# b = 13
# sum = 0
# def sum_numbers(a,b):
#     sum = a +b
#     return sum
# print(sum_numbers(14, 5))

#5
# def var(z):
#     if z <= 2:
#         z = 10
#     return z
# print(var(1))

#loops
#1
# list = [1,2,3,4,5]
# for i in list:
#     print(i)

#2
# count = 0
# while count < 5:
#     print(count)
#     count +=1
    
#3
# sum = 0
# list = [10,20,30,40,50]
# for i in list:
#     sum +=i
# print(sum)

# #4
# def multiplication_table(x):
#     list1 = [1,2,3]
#     for i in list1:
#         print(f"{x} * {i} = {x*i}")

# multiplication_table(3)

# #5
# print("Please print stop.")
# while input() != "stop":
#     print("Please print stop.")