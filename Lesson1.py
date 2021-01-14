"""
1. Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. б)
Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код,
откроет дверь с первой попытки?
3. В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
Какова вероятность того, что все извлеченные детали окрашены?
4. В лотерее 100 билетов. Из них 2 выигрышных.
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""
from math import factorial


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def arrangements(n, k):
    return int(factorial(n) / factorial(n - k))


def permutations(n):
    return int(factorial(n))


print("Из колоды в 52 карты извлекаются случайным образом 4 карты. ")
print("a) Найти вероятность того, что все карты – крести. ")
print("умножаем вероятности последовательного выбора крести P = 13/52 * 12/51 * 11/50 * 10/49 = ",
      13 / 52 * 12 / 51 * 11 / 50 * 10 / 49)
print("б)Найти вероятность, что среди 4-х карт окажется хотя бы один туз.")
print(" вероятность вытащить туз = 1 - вероятноеть не вытащить туз: 1 - 48 / 52 * 47 / 51 * 46 / 50 * 45 / 49 = ",
      1 - 48 / 52 * 47 / 51 * 46 / 50 * 45 / 49)
print()

print("На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.")
print("Код содержит три цифры, которые нужно нажать одновременно.")
print("Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?")
print(" P = 1/combinations(10, 3) = ", 1 / combinations(10, 3))
print()

print("В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.")
print("Какова вероятность того, что все извлеченные детали окрашены?")
print(" P = 9/15 * 8/14 * 7/13 = ", 9 / 15 * 8 / 14 * 7 / 13)
print()

print("В лотерее 100 билетов. Из них 2 выигрышных.")
print("Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?")
print(" P = 2/100 * 1/99 = ", 2/100 * 1/99)
