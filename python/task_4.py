# code 1:
# for i in range(1, 10):
#  if i % 2 == 0:
#    print(i * i)
### the code make variable "1" to run 
# between number 1 and 9 and check every time if "i"
# an even number and if it's even then print the number in a square ###

# Code 2:
# word = "hello"
# new_word = word[1:] + word[0]
# print(new_word)

### the code put the word "hello" in an variable named "word", 
# and then we defines new variable named "new_word" and puts in it the varible "word" except the
# first character and merge to it the first charcter from the variable "word"
# in the end itn print the varible "new_word" and it is the word "elloh"###

# Code 3:
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [n ** 2 for n in numbers if n % 2 == 1]
# print(squared_numbers)

### the output will be the square of the odds numbers ###

# Code 4:
    
# fruits = {"apple": 3, "banana": 5, "cherry": 2}
# total = 0
# for fruit in fruits:
#  total += fruits[fruit]
# print(total)

### the code will print the number 10, 
# the code calculating the values for every key summerize it in variable "total" ###

# code 5

# text = "Python"
# result = ""
# for char in text:
#  result = char + result
# print(result)

### the will be "nohtyP" (the reverse word "Python")
# the code run put each character from the variable "text" (the word "python" is in variable text) 
# and it put every character right before the proviouscharacter ###

# code 6

# set_a = {1, 2, 3}
# set_b = {2, 3, 4}
# result = set_a.symmetric_difference(set_b)
# print(result)

### the output will be {1, 4},
# the "symmetric_difference" return to the variable "result" the different values between the sets we provide him ###

#Code 7:

# def greet(name="stranger"):
#  print(f"Hello, {name}!")
# greet()
# greet("Alice")

### the code will print: "Hello, stranger!
# Hello, Alice!" 
# the purpose of the `name="stranger"` in this code is to sure if you are not put your name in the variable the code
# will still greet you ### 


#Code 8:

# sentence = "This is a simple sentence."
# count = sentence.count("s")
# print(count)

### the output will be "4".
# the code count how meny times the character "s" is in the variable "sentence" ###

#Code 9:
 
# x = 10
# y = 5
# z = x > y and y < 0 or x < 0
# print(z)

### the output will be "false".
# variable "z" check if variable "x" is greater then variable "y" and if variable "y" is smaller then 0, or
# varible "x" smaller then 0.
# if one of the conditions is met then the will be "True" if both conditions are not met then the output will be "False" ###

#Code 10:

# n = 1
# while n < 10:
#  print(n)
#  n += 3

### the output will be:
# 1
# 4
# 7
# while loop control the flow by defining that while the variable "n" is smaller then 10 stay
# in the loop until the varible "n" is not equal to 10 or bigger ###

# Code 11:

# values = (1, 2, 3)
# a, b, c = values
# print(a + b + c)

### the will be "6".
# we put in the variable "values" set with 3 numbers and then we define that "a" will be the firsr nuber in the set,
# "b" will be the second number and "c" will be the third number in the set ###

#Code 12:

# data = [10, 20, 30, 40, 50]
# print(data[-3])

### the output will be "30".
# the purpose of `-3` in the list indexing is to get third index from the end ###

#Code 13:

# info = {"name": "Alice", "age": 25}
# info["age"] = 26
# print(info)

### the code print "{'name': 'Alice', 'age': 26}".
# the line `info["age"] = 26` update the the value in key name "age" ###

#Code 14:

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [row[1] for row in matrix]
# print(result)

###  the output will be [2, 5, 8].
# the variable "metrix" has list with 3 lists in it.
# the variable "result" run in each list in the main list and print the second index###