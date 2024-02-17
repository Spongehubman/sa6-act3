

my_list_combined = [[1, 2, 3, 5, 6, 8, 9,], [0, 3, 4, 5, 7, 8, 9]]

my_list_1 = [1, 2, 3, 5, 6, 8, 9]
my_list_2 = [0, 3, 4, 5, 7, 8, 9]


# Some help for this code was taken from the W3Schools.com webpage
# titled "Python Lambda" (the source is below.)
list_intersection = list(filter(lambda x: x in my_list_2, my_list_1))

print(list_intersection)

'''
Source: "Python Lambda", W3Schools.com

https://www.w3schools.com/python/python_lambda.asp
'''