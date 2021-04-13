

# # 1.
# # x = [ [5,2,3], [10,8,9] ] 
# # students = [
# #      {'first_name':  'Michael', 'last_name' : 'Jordan'},
# #      {'first_name' : 'John', 'last_name' : 'Rosales'}
# # ]
# # sports_directory = {
# #     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
# #     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# # }
# # z = [ {'x': 10, 'y': 20} ]


# # x[1][0] = 15
# # print(x[1][0])
# # print(x)

# # students[0]["last_name"] = "bryant"
# # print(students)

# # sports_directory["soccer"][0] = "andres"
# # print(sports_directory)

# # z[0]["y"] = 30
# # print(z)



# # 2.
# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# # iterateDictionary(students) 
# # # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel
# # cop

# def iterateDictionary(my_list):
#     for item in my_list:
#         print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")
# iterateDictionary(students)

# # 3.

# def iterateDictionary2(key_name, some_list):
#     for item in some_list:
#         print(item(key_name))
# iterateDictionary2("last_name", students)



# 4

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dict):
    for key in some_dict:
        my_value_list = some_dict[key]
        print(f"{len(my_value_list)} {key.upper()}")
        for item in my_value_list:
            print(item)
print_info(dojo)


# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
