

def find_maximum(l, lam):
    
    max = l[0]

    # Lets assume the length of the list l is > 1. Then...

    for i in range(len(l) - 1):
        max = lam(max, l[(i)])

        #if greater > max:
        #    max = greater

    return max

numbers = [3, 8, 2, 5, 1, 9, 4, 6, 7]

# Some help for this code was taken from the W3Schools.com webpage
# titled "Python Lambda" (the source is below.)
compare = lambda x, y: x if x > y else y

print(find_maximum(numbers, compare))


'''
Source: "Python Lambda", W3Schools.com

https://www.w3schools.com/python/python_lambda.asp
'''