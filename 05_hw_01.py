# 1) Создать программно файл в текстовом формате, записать в него построчно данные, 
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


my_f = input('Введите имя файла: ')
with open(f"{my_f}.txt", "w") as write_f:
    while True:
        my_input = input('Введите информацию построчной для записи в файл \n'
                         '(для окончания записи - оставьте строку пустой, нажмите Enter): ')
        if len(my_input) > 0:
            write_f.writelines(f'{my_input}\n')
        else:
            break
