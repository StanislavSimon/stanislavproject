from pprint import pprint

text = 'homework.txt'
file = open(text, 'r')

pprint(file.read())
file.close()