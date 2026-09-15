# Exercise 3: Swapping the First and Last Elements of a List
my_list = [4, 3, 6, 1, 7]

if len(my_list) > 1:
    temporary_value = my_list[0]
    my_list[0] = my_list[len(my_list) -1]
    my_list[len(my_list) -1]= temporary_value

print(my_list)