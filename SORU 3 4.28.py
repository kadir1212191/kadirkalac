my_tuple = (0, 1, 2, "hi", 4, 5)
temp_list = list(my_tuple)
temp_list[3] = 3
my_tuple = tuple(temp_list)
print(my_tuple)
