first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) >= 5]
print(first_result)

second_result = [(s_1, s_2) for s_1 in first_strings for s_2 in second_strings if len(s_2) == len(s_1)]
print(second_result)

sum_strings = first_strings + second_strings
third_result = {str_: len(str_) for str_ in sum_strings if len(str_) % 2 == 0}
print(third_result)