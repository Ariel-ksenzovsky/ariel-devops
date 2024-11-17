# # If-Then Statements
# # qustion 1
# def how_old_are_you (age) :
#     if age >= 18:
#         print("welcome honey")
#     elif age == 17:
#         print("'Almost there!")
#     else:
#         print("go away little boy")

# how_old_are_you(16)

# # qustion 2
# def Even_or_Odd (number):
#     if number % 2 == 1:
#       print(f"the number {number} is odd ")
#     else:
#         print(f"the number {number} is even")

# Even_or_Odd(445)


# # qustion 3
# def Grading_System (score):
#     if score >= 90 and  score <= 100:
#         print("your grade is A")
#     elif score <= 89 and score >= 80:
#         print("your grage is B")
#     elif score <= 79 and score >= 70:
#         print("your grage is C")
#     elif score <= 69 and score >= 60:
#         print("your grage is D")
#     elif score < 60:
#         print("your grage is F")
#     else:
#         print("ERROR")

# Grading_System(100)

# # qustion 4
# def Positive_Negative_or_Zero(number):
#     if number > 0:
#         print(f"the number {number} is Positive")
#     elif number < 0:
#         print(f"the number {number} is Negative")
#     else:
#         print(f"the number {number} is Zero")

# Positive_Negative_or_Zero(0)

# # qustion 5
# def  Eligibility_for_Discount(age, student):
#     if age < 18 or student == "yes":
#         print("You are entitled to a discount")
#     else:
#         print("You are not entitled to a discount")

# Eligibility_for_Discount(16, "no")

# # For and While Loops
# # qustion 6
# for i in range(1, 11):
#     print(i)
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# # qustion 7

# sum = 0
# for num in range(1, 101):
#     sum = sum + num
# print(sum)

# # qustion 8
# def Multiplication_Table(number):
#  for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
# Multiplication_Table(20)

# # qustion 9
# list = ['red', 'green', 'blue', 'yellow']
# for i in list:
#     print(i)
    
# # qustion 10

# i = 10
# while i > 0:
#     print(i)
#     i -=1
# print('Liftoff')

# """# qustion 11

# import random
# number_to_guess = random.randint(1, 10)

# while True:
    
#     user_guess = int(input("Guess the number between 1 and 10: "))
    
#     if user_guess < number_to_guess:
#         print("Too low! Try again.")
#     elif user_guess > number_to_guess:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number!")
#         break
#     print(f'correct number was {number_to_guess}') """

# """# qustion 12
# total_sum = 0

# while True:
#     user_input = int(input("Enter a number (negative to stop): "))
    
#     if user_input < 0:
#         break 
    
#     total_sum += user_input

# print("The sum of all positive numbers entered is:", total_sum)"""

    
# # Functions
# # qustion 13

# def greet():
#     print("hello, world!")
# greet()


# # qustion 14

# def greeting(name):
#     print(f"hello, {name}")
# greeting("ariel")
# # qustion 15


# def square(num):
#     square.num = num ** 2
#     print(f"the result is {square.num}")
# square(4)


# # qustion 16

# def factorial(n):
#    result = 1
#    for i in range(1, n + 1):
#      result *= i
#    return result
# answer = factorial(0)
# print(answer)

# # qustion 17
# numbers = [1, 2, 3, 4, 4, 76, 78, 2]

# def find_max(lst):
#     if not lst:
#         return None 
    
#     max_value = lst[0]
    
#     for num in lst:
#         if num > max_value:
#             max_value = num
#     return max_value

# result = find_max(numbers)
# print(result)


# """# qustion 18
# def Temperature_Converter():
#   Celsius = int(input("How many degrees Celsius outside? "))
#   Fahrenheit = (Celsius * 1.8) + 32
#   print(f"{Celsius} celsius degrees equal to {Fahrenheit} degrees in Fahrenheit")
# Temperature_Converter()"""

# """# qustion 19
# def Palindrome_Checker():
#  word = str(input("what is the word you want to check? "))
#  if word == word[::-1]:
#          print(f"the word {word} is palindrome")
#  else:
#         print(f"the word {word} is not palindrome, pick another word" )
# Palindrome_Checker()"""

# # qustion 20
# list = [10, 11, 3, 34, 56, 100]
# def Sum_of_List():
#     sum = 0
#     for i in list:
#         sum += i
#     print(f"the sum of the list is {sum}")

# Sum_of_List()
    
# # qustion 21
def Prime_Checker(number):
    if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        print(f"the number {number} is Prime number")
    else:
        print(f"the number {number} is Composite number")
Prime_Checker(10)

# # qustion 22
# def Simple_Calculator(a, b, operation):
#     a = int(a)
#     b = int(b)
#     if operation == "+":
#       print(a + b)
#     elif operation == "-":
#       print(a - b)
#     elif operation == "*":
#       print(a * b)
#     else:
#      if b == 0:
#        print('you cant dived by zero')
#      else:
#       print(a / b)
# Simple_Calculator(10, 10, "+")