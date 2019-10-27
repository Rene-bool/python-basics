# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("05_hw_04_text.txt") as my_f:
    my_list = []
    for line in my_f:
        my_list.append(line.split())
print(my_list)

i = 0
for elm in my_list:
    for elm in my_list[i]:
        if elm in my_dict:
            my_list[i][0] = my_dict.get(elm)
        else:
            continue
        i += 1
print(my_list)

with open("05_hw_04_tran.txt", "w") as write_f:
    i = 0
    while i < len(my_list):
        print(' '.join(my_list[i]), file=write_f)
        i += 1
