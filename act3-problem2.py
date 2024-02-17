

string_list = [('cat', 3), ('grasshopper', 11), ('bash', 4), ('stash', 5), ('aardvark', 8),
                ('cs3', 3), ('archer', 6), ('ton', 3), ('goose', 5), ('shell', 5),
                ('arctic', 6), ('penguin', 7)]


#string_list.sort(key=lambda x, y: if x[1] == y[1] else x[0])

string_list.sort(key=lambda x: x[0])
string_list.sort(key=lambda x: x[1])

print(string_list)