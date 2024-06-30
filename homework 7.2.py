text = 'homework.txt'
with open(text) as file:
    for line in file:
        print(line, end='')

 print(file.read()) #I/O operation on closed file.

"Чем оличается использование оператора with open() от простого использования file.close?"
"-Тем что в операторе with файл закрывается автоматически и не нужно использовать команду file.close"