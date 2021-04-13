# 1
def countdown(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    return list
print(countdown(12))


# 2
def print_return(num_list):
    print(num_list[0])
    return num_list[1]
print(print_return([1,2]))

# 3
def first_plus_length(list):
    # return the sum of the first value + length of list
    # list1 = [1,2,3,4,5]
    sum = list[0] + len(list)
    return sum
print(first_plus_length([1,2,3,4,5]))
print(first_plus_length([44,2,3,4,5]))
print(sum)

# 4
def greater_than_second(my_list):
    list = []
    for i in range(0, len(list), 1):
        if my_list[1] > my_list[i]:
            list.append(i)
        return list
print(greater_than_second([1,2,3,4,5,6,7]))

# im getting "none" as an output and im not sure why?

# 5
def length_value(size,value):
    list = []
    int1 = size
    int2 = value
    for i in range(0,int1,1):
        list.append(int2)
    return list
print(length_value(6,2))

