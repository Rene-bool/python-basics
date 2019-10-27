# 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("05_hw_03_text.txt") as my_f:
    sname_list = []
    sal_list = []
    for line in my_f:
        sname_list.append((line).split()[0])
        sal_list.append(float((line).split()[1]))
less_sal_list = []
for el in sal_list:
    if el < 20000:
        less_sal_list.append(sname_list[sal_list.index(el)])
print('Сотрудники с зарплатой менее 20000:', ', '.join(less_sal_list))
print('Средняя зарплата сотрудников: %.2f' % ((sum(sal_list)) / (len(sal_list))))

