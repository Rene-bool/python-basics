# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
x = abs(int(input("Введите целое положительное число: ")))
i = 10
x0 = 0
if x < 10:
    print("Заданное число состоит из одной цифры", x)
else:
    while x > 0:
        x1 = x % i
        a = [x0, x1]
        x1 = max(a)
        x = x // i
        if x == 0:
            break
        else:
            x0 = x % i
            a = [x0, x1]
            x0 = max(a)
            x = x // i
    print("Максимальная цифра в заданном числе:", max(a))
