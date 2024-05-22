def print_params(a = 1, b = 'string', c = None):
    if c is None:
        c=[]
        c.append(a)
    print(c)

print_params()
print_params('Hello')
print_params(168)


# print_params()
# print_params(a = None, b = 25, c = [1, 2, 3 ])
# print_params (b = 25)
# print_params(c = [1, 2, 3 ])

# values_list = [1 , 'Hello' , True]
# values_dict = {'a': 1, 'b': 'string', 'c': True}
# print_params(*values_list)
# print_params(*values_dict)

# value_list_2 = (22 , 'Orange')
# print_params(*values_list_2, 42)
