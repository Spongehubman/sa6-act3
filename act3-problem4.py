

my_list1 = [1, 2, 3, 5, 6, 8, 9,]
my_list2 = [0, 3, 4, 5, 7, 8, 9]

list_intersection = list(filter(lambda x, y: x == y, my_list1, my_list2))

print(list_intersection)