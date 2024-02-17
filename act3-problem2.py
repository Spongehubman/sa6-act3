

string_list = ['cat', 'grasshopper', 'bash', 'stash', 'aardvark',
                'cs3', 'archer', 'ton', 'goose', 'shell',
                'arctic', 'penguin']

# Reinforcement for lambda programming coding help came from the W3Schools.com webpage
# titled "Python Lambda" (the source is below.)
string_list.sort(key=lambda x: x)
string_list.sort(key=lambda x: len(x))

print(string_list)

'''
Source: "Python Lambda", W3Schools.com

https://www.w3schools.com/python/python_lambda.asp
'''