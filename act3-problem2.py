

string_list = ['cat', 'grasshopper', 'bash', 'stash', 'aardvark',
                'cs3', 'archer', 'ton', 'goose', 'shell',
                'arctic', 'penguin']


string_list.sort(key=lambda x: x)
string_list.sort(key=lambda x: len(x))

print(string_list)