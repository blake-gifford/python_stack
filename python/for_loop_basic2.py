# 1
# def biggie_size(list):
#     for i in range(0,len(list)):
#         if list[i] > 0:
#             list[i] == "big"
#         return list
# print(biggie_size([-1, 3, 5, -5]))

# 2
# def count_positives(list):
#     positive = 0
#     for i in range(0, len(list),1):
#         if list[i] > 0:
#             positive += 1
#         if list[i] == len(list-1):
#             list[i] == positive
#             return list[i]
# print(count_positives([-1,1,1,1]))

# 3

# 1. function has to take in a list
# 2. returns the sum of all values of the list
# 3. write function
# 4. loop through
# 5.return the sum of all num in list

# def sum_total(list):
#     the_sum = 0
#     for i in range(0, len(list),1):
#         the_sum += list[i]
#     return the_sum
# print(sum_total([1,2,3,4]))

# 4

# 1.create function that takes in a list
# 2. add all the nums in the list up
# 3.find avg of the list
# 4.return avg

# def average(list):
#     sum = 0
#     for i in range(0, len(list),1):
#         sum += list[i]
#     return sum/5
#     print(sum)
# print(average([1,3,5,7,9]))

# 5

# 1.create function that takes a list
# 2. returns length of list
# 3. write a for loop

# def length(list):
#     print(len(list))
# print(length([1,2,3,4,5,6,7]))

# 6

# 1.create a function that takes a list
# 2.find the minimum value in the list
# 3.if the list is empty return false
# 4.write for loop and if statement

# def minimum(list):
#     min = 0
#     for i in range(0, len(list), 1):
#         if list[i] < list[i+1]:
#             min == list[i]
#         return min
#         print(min)
# print(minimum([1,2,3,4,5]))

# 7

# 1.create function that takes a list
# 2.return the max
# 3.if empty return false
# 4.use for loop and if statement

# def maximum(list):
#     max = 0
#     for i in range(0, len(list),1):
#         if list == [""]:
#             print("False")
#         if list[i] > list[i + 1]:
#             max == list[i]
#             return max
#             print(max)
#         return max
#         print(max)
# print(maximum([1,2,3,4,5]))
# print(maximum([""]))

# 8

# 1.create function that takes a list and returns a dict
# 2.return sum total
# 3.return avg
# 4.return min and max
# 5.for loop and if statements

# def unltimate_analyst(list):
#     dict_new = {}
#     avg = 0
#     for i in range(0, len(list),1):
#         print(dict_new)
#         if list[i] < list[i+1]:
#             min = list[i]
#             print(min)
#         if list[i] > list[i+1]:
#             max = list[i]
#             print(max)
#     dict_new = list
#     avg += list[i]
#     avg = avg/len(list)
#     print(avg)
#     print(len(list))
# print(unltimate_analyst([1,2,3,4,5]))
# i was really struggling with this one i will ask questions on it:)


# 9

# 1.create funciton that takes a list
# 2.return the same list reversed
# 3.dont make a second list
# 4.reverse for loop

def reverse_list(list):
    list1 = 0
    for i in range(len(list),-1):
        list[i] += list
    return list1
print(reverse_list([1,1,12,4]))


