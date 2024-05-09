#immutable_var = 1 , 4 , 9 ,8
#immutable_var1= 2 , 3 , 5 ,10
#print(immutable_var)
#print(immutable_var1)
#print(immutable_var1[0])
#immutable_var1[0]= 15
#print(immutable_var1[0])
#Кортеж неподдерживает обращение по элементам
#Traceback (most recent call last):
# File "C:\Users\locadmin\PycharmProjects\SimonPythonProject\.venv\homework module 1\homework4.py", line 6, in <module>
#immutable_var1[0]= 15
#~~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
mutable_list = ([6 , 7 , 8] ,'Modified')
print(mutable_list)
mutable_list[0]
print(mutable_list)
mutable_list[0][0] = 678
print(mutable_list[0])
print(len(mutable_list))

