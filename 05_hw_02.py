# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить 
# подсчет количества строк, количества слов в каждой строке.

with open("05_hw_02_text.txt") as my_f:
    i = 0
    for line in my_f:
        i += 1
        if len(line.split()) == 0:
            print(f'Строка № {i} пуста')
        elif len(line.split()) == 1:
            print(f'Строка № {i} содержит {len(line.split())} слово')
        elif len(line.split()) in range(2, 5):
            print(f'Строка № {i} содержит {len(line.split())} слова')
        else:
            print(f'Строка № {i} содержит {len(line.split())} слов')

if i == 0:
    print('Текстовый файл пуст')
elif i == 1:
    print(f'Текстовый файл содержит {i} строку')
elif i in range(2, 5):
    print(f'Текстовый файл содержит {i} строки')
else:
    print(f'Текстовый файл содержит {i} строк')
