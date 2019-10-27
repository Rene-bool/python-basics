# 5) Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

my_f = input('Введите имя файла: ')
a = input('Введите нескольких чисел, разделённых пробелами: ').split()

with open(f'{my_f}.txt', 'w') as data_f:
	data_f.write(' '.join(a))
	
with open(f'{my_f}.txt', 'r') as data_f:
	content = data_f.read().split()

sum_f = 0
for el in content:
	sum_f += float(el)

print('Сумма чисел в файле:', sum_f)
