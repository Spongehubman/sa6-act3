
numbers = [1, 2, 3, 4, 5]

# Some help for this function code was taken from the W3Schools.com webpage
# titled "Python Lambda" (the source is below.)
def choose():

    n = input("Choose a variable: ")

    # Let's assume that the value of n is always an integer. Then...
    return int(n)


# Some help for the lambda statements below was taken from and inspired from the W3Schools.com webpage
# titled "Python Lambda" (the source is below.)
multiply = lambda x: x ** choose()
power_list = list(map(lambda x: multiply(x), numbers))


print(power_list)

# For instance, if n = 4, then the output will be [1, 16, 81, 256, 625]


'''
Source: "Python Lambda", W3Schools.com

https://www.w3schools.com/python/python_lambda.asp
'''