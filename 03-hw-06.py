# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().


print('\n--- 1 способ ---\n')


def int_func(my_word):
	return my_word.title()


my_word = input("Введите слово в нижнем регистре: ")
print('Измененное слово: ', int_func(my_word))

my_words = input("Введите несколько слов в нижнем регистре разделяя их пробелом: ")
print('Измененные слова: ', int_func(my_words))

print(f'\n---Проверка сохранения оригинальности исходных данных---\n'
	  f'Слово: {my_word}\n'
	  f'Несколько слов: {my_words}\n--------------------------------------------------------')

print('\n--- 2 способ ---\n')


def int_func2(my_word):
	return my_word.capitalize()

	
print('Измененное слово: ', int_func2(my_word))

my_list = my_words.split()
i = 0
print('Измененные слова: ', end='')
while i < len(my_list):
    print(int_func2(my_list[i]), end=' ')
    i = i + 1
