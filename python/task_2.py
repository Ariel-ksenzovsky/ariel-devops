# # tuples
# # question 1
# my_tuple = (1, 2, 3)
# print(my_tuple[1])

# # question 2
# person = ("ariel", "22", "ashdod")
# (name, age, city) = person
# print(name)
# print(age)
# print(city)

# # question 3
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# nested_tuple = tuple1 + tuple2
# print(nested_tuple[4])

# # question 4
# numbers = (1, 2, 3, 2, 4, 2)
# x = numbers.count(2)
# print(x)
# y = numbers.index(3)
# print(y)

# # Dictionaries
# # question 1
# student = {
#     "name" : "ariel",
#     "age" : 22,
#     "grade" : "A"
# }

# print(student["name"])
# student["school"] = "mekif h"
# print(student)
# # question 2
# student["age"] = 23
# print(student)
# student.pop("grade")
# print(student)
# if "grede" in student:
#     print("yes")
# else:
#     print("no")
# # question 3
# capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
# for x,y in capitals.items():
#     print("The capital of" + " " + x + "is" + " " + y)
# # question 4
# x = capitals.keys()
# y = capitals.values()
# z = capitals.items()
# print(x)
# print(y)
# print(z)

# x = capitals.get("Germany", "Not sound")
# print(x)

# # question 5

# def count_character(text):

#     char_count = {}
    
   
#     for x in text:
#         if x in char_count:
            
#             char_count[x] += 1
#         else:
           
#             char_count[x] = 1
    
    
#     return char_count

# text = "hello"

# count_character_result = count_character(text)

# for x, count in count_character_result.items():
#     print(f"'{x}': {count}")

# # sets
# # question 1
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)
# my_set.add(3)
# print(my_set)
# my_set.remove(2)
# print(my_set)

# # question 2
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# set_c = set_a.union(set_b)
# print(set_c)
# set_d = set_a.intersection(set_b)
# print(set_d)
# set_e = set_a.difference(set_b)
# print(set_e)
# set_f = set_a.symmetric_difference(set_b)
# print(set_f)

# # question 3
# numbers = [1, 2, 2, 3, 4, 4, 5]
# print(set(numbers))

# # question 4
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# if 3 in set_a:
#     print("yes")
# else:
#     print("no")

# print(6 not in set_b)

# # question 5
# my_set = {1, 2, 3, 4, 5}
# my_set2 = {4, 5, 6, 7, 8}
# my_set.update(my_set2)
# print(my_set)
# my_set.remove(6)
# print(my_set)

# my_set.discard(6)
# print(my_set)
# my_set.discard(9)
# print(my_set)
#
#
#