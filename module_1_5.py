immutable_var=(750,7.5,'Строчка',False)
print(immutable_var)
print(type(immutable_var))
#На основании урока "Изменяемые и неизменяемые объекты" переменные
#класса "tuple" являются неизменяемыми типами данных
#Следовательно изменить содержимое данного кортежа не возможно известными нам способами.
mutable_list=[740,64.2, 'Клеточка', True]
mutable_list.extend([mutable_list[1]*2])
print(mutable_list)