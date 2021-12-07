# Name_new1 = "Elena"
# print("Hello,", Name_new1)
# age = 20
# print(age)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)  # 5 Hello 9.2

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)

# print("\tДокумент    \"myfirstscript.ru\"    находится по заданному пути:"
#       "\rD:\Python\projects")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
#
# print(s3 * 5)

# a = 2.456465465346546515312331
# print(a)
# print(type(a))

# print(6/2)  # 3.0
# print(7/2)  # 3.5
# print(7//2)  # 3

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num *= 5  # num = num * 5
# print(num)

# num = 9753
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# # print("num", num)
# print("Обратное число:", res)


# print(int(3.8))  # 3
# print(round(3.894, 2))  # 4

# name = "Igor"
# age = 28
# grade = 9.2
# print("It's %s, %d. Level: %.2f" % (name, age, grade))

# print("This is a {0}. It's {1}.".format("ball", "red"))

# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
#
# print(bool("Python"))  # True
# print(bool(" "))  # True
# print(bool(""))  # False
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# print("привет" > "Привет")
#
# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(not 9 - 9)

# v1 = (0 or 1) and (0 or 1)
# print(v1)


# if логическое выражение:
#     выражение

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")


# day = int(input("Введите день недели (цифрами): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели нет!")


# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "a < b"))

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)
# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")

# i = 0
# while True:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1


# kol = int(input("Введите количество чисел последовательности: "))
# ch = float(input("Введите число: "))
# min_ch = ch
# sum_ch = ch
# i = 1
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     i += 1
# print("Минимальное число: ", min_ch)


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collections:
#     print(element)

# for i in 'Hello':
#     print(i)
#
# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue':
#     print(j, 'color:', color)
#     j += 1

# for i in 'one', 'two', 1, 20, 0.3:
#     print(i)

# for i in range(n):
#     Тело цикла

# range(start, stop, step)
# for i in range(9, -1, -1):
#     print(i, end=" ")


# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# [результирующее выражение | цикл | опциональные условия]
# print([i * 2 for i in "Hello"])
# num = [i ** 3 for i in range(30) if i % 2 == 0]
# print(num)

# Списки
# num = [8, 3, 9, 4, 1]
# print(id(num))
# print(num)
# # print(type(num))
# # print(type(["one", "two", 2, 3.5, [1, 2, 3]]))
# print(num[0])
# print(num[-3])
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))
# print("Длина списка: ", len(num))

# s = [5] * 6
# print(s)
# b = list("Hello")
# print(b)

# n = list(range(10, 2, -2))
# print(n)
# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элеметов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Кол-во: ")))]
# print(a)

# a = list(range(10, 2, -2))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
#
# print()
# for j in a:
#     print(j, end=" ")

# ========================
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("---------------------------------")
# for i in my_list:
#     print(i ** 2, end=" ")
# print("\n---------------------------------")
# for i in range(len(my_list)):
#     my_list[i] = my_list[i] ** 2
#     print(my_list[i], end=" ")

# a = [input("-> ") for i in range(int(input("n = ")))]
# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in range(len(n)):
#     print(n[i])
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# print("Количество: ", k)
# print("Сумма: ", s)

# summa = k = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] != 0:
#         summa += a[i]
#         k += 1
# print(summa/k)

# Срезы - получение какой-то части списка, которая в свою очередь тоже является списком

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[8] = 18
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# s.append('add')
# print(s)
# # s1 = []
# # s1.extend([1, 2, 3])  # добавляет множество элементов
# # print(s1)
# # s1.extend('add')
# # print(s1)
# s.insert(1, 100)  # добавляет элемент в список в заданную позицию (первый параметр) и с узазанным значением
# # (второй парамер)
# print(s)

# s1 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
#
# s[7:] = []
# print(s)
# s.remove(0)  # удаляем элемен из списка с заданным значением, если элементов несколько, то удалится только
# # самый первый
# print(s)
# # s.remove(2)
# # print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop()  # возвращает элемен на указанной позиции, удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
#
# s.clear()  # удаляет из списка все имеющиеся в нем значения
# print(s)
#
# # del s[1]
# # print(s)
#
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3)  # считает количество значений "3" в списке
# print(num)
#
# ind = s.index(3, 3, -1)  # возвращает положение первого индекса
# print(ind)
#
# s_copy = s.copy()  # возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse()  # перестраивает элементы списка в обратном порядке
# print(s)

# s.sort(reverse=True)  # сортирует список, reverse=True - по убыванию
# print(s)

# sorted_s = sorted(s, reverse=True)
# print(sorted_s)
# print(s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# import random
# from random import random, randint, randrange
#
# print(random())  # [0.0, 1.0]
# print(randint(0, 9))
# print(randrange(0, 10, 2))

# import random as r
#
# print(r.randint(0, 5))
# print(r.randint(0, 5))
# print(r.randrange(0, 10, 2))
#
# cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(cities))
#
# s = [55, 66, 77, 88, 99, 66, 45, 78, 90]
# print(r.sample(s, 5))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
# print(round(r.uniform(10.5, 25.5), 2))
#
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print("Длина списка:", len(lst))
# print("Минимальное значение:", min(lst))
# print("Максимальное значение:", max(lst))
# print("Сумма:", sum(lst))
import copy
import random as r

# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print("Max:", max_1)
# mas1.remove(max_1)
# mas1.insert(0, max_1)
# print(mas1)

# mas1 = [r.randint(-20, 20) for i in range(10)]
# print(mas1)
# mas1.sort(reverse=True)
# print(mas1)


# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# min_l = min(mas1)
# print("Min:", min_l)
# ind_min_l = mas1.index(min_l)
# print("Index_min:", ind_min_l)
#
# # del mas1[0:ind_min_l]
#
# print(mas1[ind_min_l:])

# in - оператор принадлежности
# not in
# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)
# lst = ['1', 'a', '2', 'b', '3', 'c', '4', 'd']
# if 'a' in lst:
#     print("True")
# else:
#     print("False")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# lst_1 = [r.randint(0, 10) for i in range(n1)]
# lst_2 = [r.randint(0, 10) for j in range(n2)]
# print("Первый список:", lst_1)
# print("Второй список:", lst_2)
# lst_3 = lst_1 + lst_2
# print("Третий список:", lst_3)
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# for i in range(len(lst_2)):
#     if lst_2[i] not in lst_3:
#         lst_3.append(lst_2[i])
#
# print("Элементы обоих списков без повторений: ", lst_3)
#
# lst_3 = []
# for i in lst_1:
#     repeat = False
#     for j in lst_2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# for i in lst_2:
#     repeat = False
#     for j in lst_1:
#         if i == j:
#             repeat = True
#     if not repeat:
#         lst_3.append(i)
# print(lst_3)
#
# lst_3 = []
# for i in range(len(lst_1)):
#     if lst_1[i] in lst_2 and lst_1[i] not in lst_3:
#         lst_3.append(lst_1[i])
# print(lst_3)
#
# lst_3 = []
# lst_3 = [min(lst_1), min(lst_2), max(lst_1), max(lst_2)]
# print(lst_3)

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = users1
# users2.append("Виктория")
# print(users1)
# print(users2)
# print(id(users1))
# print(id(users2))
# # is - возвращает True, если оба операнда указывают на один и тот же объект
# # is not - возвращает True, если оба операнда указывают на разные объекты
# print(users1 is users2)
# import copy
# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = copy.deepcopy(users1)
# users2.append("Виктория")
# print(users1)
# print(users2)
# print(id(users1))
# print(id(users2))
# print(users1 is users2)
# import random
#
# listVal1 = [random.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# listVal2 = [random.randint(0, 10) for j in range(int(input("Введите размер первого списка: ")))]
# listVal3 = listVal1 + listVal2
# print("Список без повторений:")
# print(listVal1)
# print(listVal2)
# listVal5 = []
# listVal5 += [i for i in listVal1 if listVal1.count(i) == 1]
# listVal5 += [i for i in listVal2 if listVal2.count(i) == 1]
# print(listVal5)
# print("Общие элементы")
# listVal6 = [i for i in listVal1 if i in listVal2]
# print(listVal6)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m[1][2])
# # m[row][col]
# print(m)

# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# square = [[x**2 for x in row] for row in m]
# for row in square:
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = [[x for x in range(y, y+10)] for y in range(10)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# Преобразовать матрицу таким образом, чтобы строки с нечетными индексами были упорядочены по убыванию, а с четными
# по возрастанию

# m = [
#     [2, 5, 8],
#     [8, 5, 6],
#     [9, 4, 1],
#     [1, 2, 4],
#     [7, 5, 6]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# for i in range(len(m)):
#     if (i+1) % 2 == 0:
#         m[i].sort()
#     else:
#         m[i].sort(reverse=True)
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# import random as r
#
# w, h = 5, 4
# m = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

from math import *

# radius = 2
# print(pi * (radius ** 2))

# sqrt = sqrt(2)
# print(sqrt)
# num1 = ceil(3.2)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# num = -5.24
# print("Модуль числа: ", fabs(num))
#
# a = -14
# b = -8
# c = 4
# print("Наибольший общий делитель: ", gcd(a, b, c))
#
# num_list = [0.3, 0.3, 0.3]
# print("Сумма", fsum(num_list))
# print("Сумма", sum(num_list))
# # decimal
# print(degrees(3.12159))
# print(radians(180))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))

# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print(sqrt((a ** 2) + (b ** 2)))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# sec = time.time()
# print("Секунды с начала эпохи:", sec)
# local_time = time.ctime(sec)
# print("Местное время:", local_time)
# res = time.localtime(sec)
# print("Locatime:", res)
# print("Год:", res.tm_year)
# print("Месяц:", res.tm_mon)
# print("День месяца:", res.tm_mday)
# print("Часы:", res.tm_hour)  # c 0 до 23
# print("Минуты:", res.tm_min)  # c 0 до 59
# print("Секунды:", res.tm_sec)  # c 0 до 61
# print("День недели:", res.tm_wday)  # c 0 до 6
# print("День года:", res.tm_yday)  # c 1 до 366
# print("Учет перехода на летнее время:", res.tm_isdst)  # 0 или 1 или -1
#
# print((time.strftime("Today is %B %d, %Y", time.localtime(456127987))))
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 0.5
# print("Program started...")
# time.sleep(pause)
# print(str(pause) + " seconds.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(1)
# finish = time.monotonic()
# res = finish - start
# print("Program time: " + str(res) + " seconds.")

# print((time.strftime("Сегодня: %B %d, %Y")))
#
# local_time = time.ctime(sec)
# print("Местное время:", local_time)


# def hello(name, word):
#     print("Hello,", name, ". Say " + word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", 'hello')

# def get_sum(a, b):
#     return a * b
#
#
# # x = 2
# # y = 3
# # res = get_sum(x, y)
# print(get_sum(2, 3))
# print(get_sum(2.6, 4))
# print(get_sum("abc", 2))
# get_sum(str(x), "aaa")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(19, "+", "-")
# symbol(17, "X", "0")
#
#
# def paint_my(n, first, second):
#     for i in range(n):
#         print(first if i % 2 == 0 else second, end="")
#     print()
#
#
# paint_my(9, "+", "-")
# paint_my(7, "X", "O")
# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         pass
#
#
# print(maxmin(10, 5))
# print(maxmin(5, 15))

# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#     print()
#
#
# fib(22)
# fib(61)
# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def get_sum(a, b=2, c=1, d=0):  # аргументы по умолчанию
#     return a + b + c + d
#
#
# print(get_sum(1, 5, c=5, d=2))
# x, y, z = 1, 5, 6
# print(get_sum(1, 5, 2, 2))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(x, y, d=z))  # именованные (ключевые) параметры

# def check_passwd(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#         return True
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки")
#         return True
#
#
# check_passwd("igor", '12345')
# check_passwd("igor", '12345igor', check_username=False)
# check_passwd("igor", '12345name')
# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 != 0:
#             s += a
#         n //= 10
#     return s
#
#
# print("Сумма четных элементов:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных элементов:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, "\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23)

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))


# a1 = [1, 2, 3]
# print(id(a1))
# a1.append(4)
# print(a1)
# print(id(a1))
# a1[1] = "Hello"
# print(a1)
# print(id(a1[1]))

# s = "Hello"
# print(id(s))
# s += "World"  # s = s + "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# st = "Hello"
# print(id(st))
# st = st[1:-1]
# print(st)
# print(id(st))

# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(id(a1))
# print(id(a2))
# y = a1
# print(id(y))
# print(a1 is a2)
# print(a1 is y)
# a1[0] = 0
# print(a1)
# print(y)

# x = [1, 2, 3]
# print(id(x))
# x += [4, 5]
# print(x)
# print(id(x))


# def add_number(n):
#     print("Внутри функции:", n, "=", id(n))
#     n = n + [4]
#     print("После присваивания:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

# кортеж (typle)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# # упаковка кортежа
# a1 = (5,)
# print(a1)
# c = 1, 2, 3
# print(type(c))
# print(c)
#
# t1 = tuple("hello")
# print(t1)

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])
# a[1] = 3

# s1 = tuple([int(input("-> ")) for i in range(5)])
# print(s1)

# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)
# import random as r

# mas = tuple([r.randint(0, 100) for i in range(10)])
# print(mas)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# # print(t3.index("a"))
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("Такого символа нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             f = tpl.index(el)
#             s = tpl.index(el, f+1) + 1
#             return tpl[f:s]  # ptl[1:5]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# import random as r
#
#
# def ran(a, b):
#     return tuple(r.randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))
# def func(lst):
#     a = []
#     [a.append(i) for i in reversed(lst) if i not in a]
#     return tuple(a)
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)

#
# contries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(contries)
# for country in contries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "насление =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)


# a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# b = []
# c = []
# for i in a:
#     if i != 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 b.append(i)
#                 break
#         else:
#             c.append(i)
# print(c)
# print(b)
# print("Min", min(c))
# print("Max", max(b))

# Множества - set()
# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
# a = set('1231')
# print(a)
# c = ["red", "green", "green", "blue", "purple"]
# col = set(c)
# print(col)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = list({i for i in numbers if i % 2 == 0})
# print(num)

# c = {"red", "green", "blue", "purple"}
# print("green" not in c)

# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r1 if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  # добавление элемента
# print(a)
# a.remove(4)  # удаление элемента
# print(a)
# b = 2
# if b in a:
#     a.remove(b)
# print(a)
#
# a.discard(1)  # удаление элемента без генерации исключения, если элемент отсутвует
# print(a)
#
# a.pop()  # удаление первого элемента
# print(a)
#
# a.clear()  # полная очистка
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = b | a
# a.update(b)
# a |= b
# c = a.intersection(b)
# c = a < b
# c = a.copy()
# print(c)
# print(b)

# drawing = {'Marina', "Jenya", "Sveta"}
# music = {'Kostya', 'Jenya', "ilya"}
#
# one = drawing ^ music
# two = drawing & music
# drawing = drawing - two
# print("Only one hobby: ", one)
# print("Both hobbies: ", two)
# print("Drawing: ", drawing)

# тип frozenset (замороженное множество)
# s = frozenset({i**2 % 4 for i in range(10)})
# print(s)

# r1 = set('ABCD')
# b = {frozenset({i+j for j in r1.difference({i})}) for i in r1}
# print(b)

# def superset(s1, s2):
#     if s1 > s2:
#         print("Объект", s1, "являтся чистым супермножеством")
#     elif s1 == s2:
#         print("Множества равны")
#     elif s1 < s2:
#         print("Объект", s2, "являтся чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#
#
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
#
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)

# a = [2, 7, 0, 3, 1, 5, -13, 100]
# b = [2, 7, 0, 3, 1, 5, -13, 13]
# c = [26]
# d = [99, 99, 100, 34, -39]
# w = [99, 39, 26, 99, 100, 34]


# a = [2, 7, 0, 3, 1, 5, -13, 100]
# b = [2, 7, 0, 3, 1, 5, -13, 13]
# c = [26]
# d = [99, 99, 100, 34, -39]
# w = [99, 26, 99, 100, 39, 34]
#
#
# def ch(lst):
#     g = []
#     for i in lst:
#         if i > 0 and i % 13 == 0:
#             g.append(i)
#
#     if not g:
#         return "no numbers"
#
#     u = max(g)
#     return u
#
#
# print("{0} -> {1} ".format(a, ch(a)))
# print("{0} -> {1} ".format(b, ch(b)))
# print("{0} -> {1} ".format(c, ch(c)))
# print("{0} -> {1} ".format(d, ch(d)))
# print("{0} -> {1} ".format(w, ch(w)))

# Словари (dict)
# a = [1, 2, 3, 4]

# b = {"one": 1, "two": 2}
# print(b)

# d = {}
# print(d)
# print(type(d))
# d1 = dict()
# print(d1)
#
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)
#
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {str(a): a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4["2"])
# d4["2"] = 15
# print(d4)
# d4["5"] = 4**2
# print(d4)

# d5 = {0: "text1", "one": 40, (1, 2.3): 'кортеж', "two": [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5["two"][1])
# print(d5[(1, 2.3)])
# del d5[(1, 2.3)]
# print(d5)
#
# print("one" in d5)
# print("a" in d5)
#
# print(d5.keys())
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "=", d6[key])

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# for k in range(1, 5):
#     d[k] = input("-> ")
# dictTest = {i: input("-> ") for i in range(1, 5)}
# print(dictTest)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# print(len(d6))

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals["Испания"] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны " + country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием: " + country)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# iter

# d = {"A": 1, "B": 2, "C": 3}
# print(list(d.values()))  # список значений


# d.update([('R', 7), ('Q', 9)])
# print(d)
# d.update([('A', 20), ('B', 40)])
# print(d)

# item = d.setdefault("S", 5)  # устанавлявает элемент по умолчанию
# print(item)
# print(d)

# item = d.popitem()  # удаляет случайную пару ключ: значение
# print(item)
# print(d)


# value = d.get("B")  # получение значения по заданному ключу
# print(value)
# print(d)
#
# new = d.items()  # список пар ключей и значений
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys()  # список ключей словаря
# print(a)

# item = d.pop("S", 5)
# print(item)
# print(d)


# d2 = d.copy()
# print("d =", d)
# print("d2 =", d2)
#
# d2["B"] = 5
# d["E"] = 7
# print("d =", d)
# print("d2 =", d2)


# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {i: d[i] for d in [x, y] for i in d}
# # z = x | y
# # z = x.copy()
# # print(z)
# # z.update(y)
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop("salary")
# print(d)
# print(new_d)

# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(f'{a}')
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(f'\t{y}: {a[x][y]}')
# print('\t', y, ':', a[x][y])


# a = {'один': (1, 2, 3), 'два': 2, 'три': 3, 'четыре': 4}
# d = {value: key for key, value in a.items() }
# print(d)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)

# value = input('-> ')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
#
# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))
# try:
#     print(m[(2, 0)])
# except KeyError:
#     print(0)

# if (2, 0) in m:
#     print(m[(2, 0)])
# else:
#     print(0)

# SciPy

# list()
# a = {1: "Rectangle", 2: "Triangle", 3: 'Circle'}
#
# value = list(a.values())  # список значений словаря
# print(value)
#
# k = list(a.keys())  # список ключей словаря
# print(k)
#
# par = list(a.items())  # список пар (ключ: значение)
# print(par)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip
# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# c = [4.6, 4.0, 9.2]
# d = zip(a, b , c)


# print(list(zip(range(5), range(5))))

# a = {12: "Dec", 1: "Jan", 2: "Feb"}
# b = {3: "Match", 4: "April", 5: "May"}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# ls = [2, 1, 4, 3]
# n = ['b', 'd', 'a', 'c']
#
# a = sorted(zip(ls, n))
# print(a)
# a = list(zip(ls, n))
# print(a)
# a.sort()
# print(a)
# a = list(zip(n, ls))
# print(a)
# a.sort()
# print(dict(a))

# month = ["January", "February", "March"]
# total = [52000.00, 51000.00, 48000.00]
# prod = [46800.00, 45900.00, 43200.00]
#
# for t, p, m in zip(total, prod, month):
#     profit = t - p
#     print("Общая прибыль в", m, "=", profit)

# one = {'apple': 0.04, 'orange': 0.35, 'pepper': 0.25}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "-> ", v)

# data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
# for i, val in enumerate(data, 1):
#     print(i, ":", data[val])
#
# d = {"1": {'a': 1, 'b': 2, 'c': 3},
#      "2": {'a': 10, 'b': 20, 'c': 30}}
# for i, k in enumerate(d, 10):
#     print(i, ") key = ", k, ", value = ", d[k], sep="")

# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))
# print(next(itr, "STOP"))

# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))

# a = [1, 2, 3]
# b = [4, 5, *a, 6]
# print(b)

# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(4, 6, a=1, b=3, c=5))
# print(func())
# print(func(w="Python"))

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#     # return sum(params)
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))

# def print_scores(student, *scores):
#     print("Имя студента:", student)
#     for s in scores:
#         print(s, end=" ")
#     print()
#
#
# print_scores("Валентин", 100, 90, 88, 92, 99)
# print_scores("Роман", 96, 20, 33, 56)
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2 != 0):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))

# def info(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# info(firstname="Irina", lastname="Sharma", age=22, phone="1234567898")
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru", country="Russia", age=25, phone="45464121317")

# def func(name, *args, **kwargs):
#     print(args[0])
#     print(kwargs['one'])
#
#
# func("Irina", 1, 2, 3, 4, odd=True, one="1", three="3")

#     print("Name :", name)
#     for pet, name in pets.items():
#         print(pet, ":", name)
#
#
# pet_names("Jonathan", dog="Brock", fish=["Larry", "Curly", "Molly"], turtle="Shelldon")
#
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}
# print(z)

# name = "Tom"
# print(name)
#
#
# def hi():
#     global name
#     name = "Sam"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# print(name)
# bye()

# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# print(x)

# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x =", x)
#         return a + x
#
#     return wrap()
#
#
# print(add_five(5))

# x = 4
#
#
# def func():
#     a = 3
#     print(x + a)
#
#
# func()

# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world")
# outer_func("star")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренней функции:", a + b)
#
#     print("Значение внешней переменной a:", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# def fn():
#     global t
#     a = 30
#     print("global:", x)
#     print(a)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#         return
#     inner()
#     print(a)
#     t = a
#     return
#
# fn()
#
# z = x + t
# print(z)

# def fn1():
#     x1 = 25
#
#     def fn2():
#         # x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print('fn2.x1 =', x1)
#
#     fn2()
#     print('fn1.x1 =', x1)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#     # x = 5
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(x)
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print("result =", result)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# # print("s =", s)
# print(rect_paral_square(5, 8, 2))
# # print("s =", s)
# print(rect_paral_square(1, 6, 8))
# # print("s =", s)

# closure (замыкание)
# def increment(n):
#     def inner_increment(x):
#         return n + x
#     return inner_increment
#
#
# a = increment(12)
# print(a(5))
# print(increment(12)(5))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classfilter(lower, upper):
#     def class_strudent(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_strudent
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
#
# obj2 = func(5, 2)
# print(obj2.sub())
#
# obj3 = func(5, 2)
# print(obj3.mul())

# print((lambda x, y: x + y)(1, 2))
#
# # func = lambda x, y: x + y
# # print(func(1, 2))
# # print(func("a", "b"))
#
# print((lambda x, y: (x ** 2) + (y ** 2))(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# print(summ(10, 20, 30))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1("a", "b"))

# c = (lambda x: x*2,
#      lambda x: x*3,
#      lambda x: x*4)
#
# for t in c:
#     print(t('abc'))
#
#
# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: (lambda x: x + n))
#
#
# f = inc(42)
# print(f(0))
# print(f(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))
#
# print((lambda x: (lambda y: (lambda z: x+y+z)))(2)(4)(6))
# sum3 = (lambda x: lambda y: lambda z: x+y+z)
# print(sum3(2)(4)(6))
#
#
# def f1(x):
#     def f2(y):
#         def f3(z):
#             return x + y + z
#
#         return f3
#     return f2
#
#
# print(f1(2)(4)(6))

# d = {'c': 4, 'b': 15, 'a': 10}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[0])
# print(list_d)
# print(dict(list_d))

# players = [
#     {'name': 'Антон', "last name": 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', "last name": 'Бодня', 'raiting': 10},
#     {'name': 'Федор', "last name": 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', "last name": 'Семенов', 'raiting': 6},
# ]
# d_players = list(players.items())
# print(d_players)
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res)
# res = sorted(players, key=lambda item: item['raiting'])
# print(res)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# b = a[3](5, 12)
# print(b)

# a = {'one': lambda x: x-1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday'),
# }
#
# d[2]()
# import math
#
# area = {
#     "Circle": lambda r: math.pi * r * r,
#
# }
#
# print("Площадь окружности: ", area['Circle'](2))

# TRUE if условие else FALSE

# print((lambda a, b: a if a > b else b)(15, 13))

# min_1 = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(min_1(4, 8, 5))

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# # lst2 = list(map(mul, lst))
# # print(lst2)
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# res = list(map(round, areas, range(1, 7)))
# print(res)

# st = "hello"
# res = list(map(lambda x: x, st))
# print(res)

# t = ('asdfg', 'asd', 'asde', 'fd', 'aqs')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
#
# import random as r
#
# lst = [r.randint(1, 40) for i in range(10)]
# print(lst)

# a = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: not s % 15, a)))

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)

# a = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], a))
# print(m)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(help(square))
# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительноен число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(3, 6))
# print(cylinder.__doc__)
# print(max.__doc__)

# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper(n, m):
#         print('*' * 20)
#         func(n, m)
#         print('*' * 20)
#     return func_wrapper
#
#
# @my_decorator
# def func_test(a, b):
#     print(a * b)
#
#
# # test = my_decorator(func_test)
# # test()
# func_test(2, 5)

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def deco(fn):
#     counter = 0
#
#     def wrapper():
#         nonlocal counter
#         fn()
#         counter += 1
#         print('Вызов функции', counter)
#
#     return wrapper
#
#
# @deco
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         print(args)
#         print(kwargs)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# @args_decorator
# def one(a, b):
#     print(a + b)
#
#
# @args_decorator
# def two(a, b, c, d, e, f, g):
#     print(a * b * c * d * e * f * g)
#
#
# one(2, 3)
# two(2, 3, 4, 7, 9, 6, 4)
# two(2, 3, 7, 6, 8, 2, 3)

# def args_decorator(arg1, arg2):
#     print("Я создаю декоратор. Аргументы:", arg1, arg2)
#
#     def my_decorator(func):
#         print("Я - декоратор. Аргументы", arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print("Я - обертка вокруг декорируемой функции")
#             func(arg1, arg2)
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_decorator
#
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_name(first, last):
#     print("Меня зовут: ", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwards):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Типы данных не соответветствуют")
#
#             for k in kwargs:
#                 if type(f_kwards[k]) != kwargs[k]:
#                     raise TypeError("Типы данных не соответветствуют")
#
#             return fn(*f_args, **f_kwards)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2("Hello, ", "world", "!"))
# print(typed_fn3("Hello, ", "world! ", z=5))
# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world("Hi!")
# hello_world2("world!")

# print(1)

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(bin(19))  # двоична система
# print(oct(19))  # восьмиричная
# print(hex(19))  # шестнадцатеричная
#
# print(0b1010)
# print(0o12)
# print(0xFF)

# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * -3)
#
# print(e in "I am learn Python")
# print(e in "I am learn Java")
#
# s = "Hello"
# print(s[2:len(s)-2])
# print(s[4:0:-2])
# print(s[0:4])
# print(s[::-1])

# s = 'abcdefgh'
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, -1)])

# print(u"Hello")
# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')
# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# import math
# print(f"Значение числа pi: {math.pi:.2f}")
#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")

# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f'Мы живем на планете {planets[2]}')
#
# planet = {"name": "Земля", "radius": 6378000}
# print(f"Планета {planet['name']}. Раудиус {planet['radius']/1000}км.")
#
# print(f"13 / 3 = {round(13/3)}")

# name = "друг"
# prof = "программист"
# lang = "Python"
#
# message = (
#     f"Привет {name}. "
#     f"Ты {prof}. "
#     f"На языке {lang}."
# )
#
# print(message)
# a = 74
# print(f"{{{{{74}}}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)

# s = "5"
# s1 = "2"
# print(sum(s, s1))

# print(ord('a'))  # 97
# print(ord('#'))  # 35
#
# print(ord('у'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# mystr = "Test string for me"
# arr = [ord(x) for x in mystr]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in (input("-> "))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")
# print()
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))


# список
# кортеж
# словарь
# множество

# s = "hello, WORLD! I am learning Python. 123@!"
# print(s.capitalize())  # первый символ преобразуется в верхний регист, все остальные преобразовываются в нижний
# print(s.lower())  # преобразует все символы в нижний регист
# print(s.upper())  # преобразует все символы в верхний регист
# print(s.swapcase())  # меняет регистр символов на противоположный
# print(s.title())  # преобразует первые буквы всех слов в заглавные
# print(len(s))
# print(s.count("l", 0, 15))  # возвращает количество вхождений подстроки в строку
# print(s.find("cPython", 3))  # возвращает первый индекс, который соответствует элементу, начиная с начала строки
#
# str1 = input("Введите вда слова через пробел: ")
# a = str1[str1.find(" ") + 1:]
# b = str1[:str1.find(" ")]
# print(a)
# print(b)
# print(b + "&" + a)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)


# num = "ab12c59p7dq"
# digits = []
# for i in num:
#     if 48 <= ord(i) <= 57:
#         digits.append(int(i))
# print(digits)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         pass
# print('digits =', digits)

# print(s.index("Python"))  # возвращает первый индекс, который соответствует элементу, начиная с начала строки,
# # возвращает ValueError если совпадение не найдено
# print(s.index("cPython"))

# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# first = s.index('(')
# second = s.index(')')
# print(s[first + 1:second])
# print(s[s.find('(') + 1:s.find(')')])
# s = "hello, WORLD! I am learning Python. 123@!"
# print(s.rfind("l", 3, 16))
# print(s.rindex("al"))

# s = 'aaaaaaafaaaaaaafaaaaaaa'
# s = 'aaaaaffaaaaaafaaaaaafaaaaafaaaaaaa'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))

# s = input('Введите строку: ')
# if s.count('f') == 0:
#     pass
# elif s.count('f') == 1:
#     first = s.find('f')
#     print(first)
# else:
#     first = s.find('f')
#     second = s.rfind('f')
#     print(first, second)
# h = 'fSend heri yulio hertino ftfdf'
# jjj = []
# j = -1
# for i in h:
#     j += 1
#     if i == 'f':
#         jjj.append(j)
# print(jjj)

# s = "hello, WORLD! I am learning Python. 123@!"
# print(s.endswith("hello", 0, 5))  # определяет, заканчивается ли строка заданной подстрокой

# print(''.isalnum())  # определяет, состоит ли стока из букв и цифр
# print('AAC%njk'.isalnum())  # определяет, состоит ли стока из букв, не присутствуют служебные символы символы
# print('45645'.isdigit())  # определяет состоят ли стока из цифр
# print("in".isidentifier())  # является ли стока допустимым идентификатором
#
# print('abc'.islower())  # определяет, являются ли буквенные символы стоки строчными
# print(' \t \n '.isspace())  # определяет состоят ли стока из пробельных символов
#
# print("Hello".istitle())  # определяет начинается ли строка с заглваной буквы
# print("HELLO".isupper())  # определяет состоит ли строка с заглваных букв
#
# print('py'.center(10))  # выравнивает сроку по центру
# print('       https://www.python.org/      '.lstrip())  # обрезает заданные символы с левой стороны, если символы не
# # заданы, то удает пробельные символы слева
# print('       https://www.python.org/'.rstrip('org/'))  # обрезает заданные символы с правой стороны, если символы не
# # заданы, то удает пробельные символы справа
# print('https://www.python.org/'.lstrip('htps:/').rstrip("/"))
# print('    https://www.python.org/    '.strip())  #обрезает заданные символы с левой и с правой стороны, если символы не
# # заданы, то удаляет пробельные символы с обоих сторон

# s = "Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования."
# print(s.replace("Nuthon", "Python"))  # заменяет вхождение подстроки в строке

# s = "Замените в этой строке все появления буквы \"о\" на букву \"О\", кроме первого и последнего вхождения."
# s = s.replace('о', 'О')
# print(s)

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  # объединили список в строку
# print("...".join(['1', '99']))
# print()  # H:e:l:l:o
#
# print(":".join("Hello"))
#
# print("Строка разделенная пробелами".split())
# print('www.python.org'.rsplit(".", 1))
#
# a = input("-> ").split()
# print(a)

# stroka = input("Введите ФИО - ").split()
# print(stroka)
#
#
# def ren(inp):
#     return inp[0] + " " + inp[1][0] + ". " + inp[2][0] + "."
#
#
# print(ren(stroka))
# import re


# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта."
# reg = 'я'
# print(s.find(reg))  # 15
# # find() - в строку будет искать шаблон и возвращать индекс первого вхождения подстроки в строке. Если шаблон не
# # найден, то будет возвращать значение "-1"
# print(reg in s)
#
# print(re.findall(reg, s))  # возаращает список, содержащий все совпадения с регулярным выражением
# print(re.findall("12", s))
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# reg = 'Я'
# print(re.match(reg, s))  # поиск по заданному шаблону вначале строки
# reg = r"я"
# print(re.split(reg, s, 1))  # возвращает список, в которм строка разбита по шаблону
# print(re.sub(reg, "!", s))  # заменяет совпадения указанным текстом
# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 2565"
# reg = '[12][09][0-9][0-9]'
# print(re.findall(reg, s))
# s = "Ели[-ели]."
# reg = r'[А-Яа-яё\[\].-]'
# print(re.findall(reg, s))
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# [^abc] - возвращает совпадение для любого символа, кроме заданных
# s = "Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 25_65"
# reg = r'\Dпаден'
# print(re.findall(reg, s))
# \d - одна любая цифра [0-3]
# \w - буква, цифра, символ подчеркивания (_)
# \s - один пробельный символ (включая табуляцию и перенос строки)
# \D - все кроме цифр
# \W - все кроме букв, цифр, символа подчеркивания (_)
# \S - все кроме пробелов
# \A - ищет символ в начале строки
# \Z - ищет символ в конце строки
# \b

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта. 25_65"
# reg = r'20*'
# print(re.findall(reg, s))

# количество повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения", re.sub("-", ":", re.sub("#.*", "", s)))
#
# # Заменить дефисы на точки

# s = "12 сентября 2021 года"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = "МИ Д - Министерство иностранных дел, ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасности"
# reg = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта."
# reg = r'я'
# print(re.findall(reg, s, flags=re.IGNORECASE))
#
# print(re.findall(r'\d+', "12 + ۴"))
# print(re.findall(r'\d+', "12 + п", flags=re.ASCII))

# re.DEBUG
# re.LOCALE
# re.DOTALL

# text = r'''
# Торт
# с вишней1
# вишней2
# '''
# print(re.findall(r'Торт.с', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))

# print(re.findall('''
#                 [\w.-]+
#                 @ # разбиваем по @
#                 [\w.-]+
#                 ''', "test@mail.ru", re.VERBOSE))

# s = "author=Пушкин А.С.; title = Евгений Онегин; price    =200; год= 1831"
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))


# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python_master_master'))

# жадные (greedy) - захватывают максимально возможное число символов
# ? - ленивые (lazy) - захватывают минимально возможное число символов

# *?, +?, ??
# {n, m}?, {, m}?, {n,}?


# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# # print(re.findall('<.*?>', text))
# print(re.search('<.*?>', text).group())

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img[^>]*>"
# print(re.findall(reg, s))

# text = "Python[16] (питон[17] или пайтон[18])[19][20]"

# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5, qw"
# reg = r"[a-z]+\d*"
# print(re.findall(reg, s, re.I))
# print(re.search(reg, s, re.I).group())

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = "31-11-1999"
# reg = r"([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9][0-9]|[2][0][0-9][0-9])"
# print(re.findall(reg, a))

# 192.168.222.255
# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "Базовый JS прост. Продвинутый Python сложен. Базовый Python прост."
# # reg = r'[а-яё]+(?= Python)'
# # reg = r'Базовый(?! Python)'
# # reg = r'(?<=Базовый )\w{2,6}'
# reg = r'(?<!Продвинутый )Python'
# print(re.findall(reg, s, re.IGNORECASE))

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# reg = r'\w+(?<!Людовик)VI'
# print(re.findall(reg, s, re.IGNORECASE))


# s = "1X, Text ABC 123 A1B2C3"
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s))
#
# s1 = "text from #START# till #END#"
# reg1 = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg1, s1))
#
# s2 = "12_34__56"
# reg2 = r'\d+(?=_(?!_))'
# print(re.findall(reg2, s2))

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print("Строка: ", m[0])
# print("Цифры: ", m[1])
# print("Буквы: ", m[2])

# s = "Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "google.com and google.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# def is_roman_number(num):
#     pattern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
#     if re.search(pattern, num):
#         return True
#     return False
#
#
# print(is_roman_number('MMDCCLXXIII'))
# print(is_roman_number('CCCMMVIIVV'))
# print(is_roman_number('CVI'))

# Рекурсия
# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25
# def sum_list(lst):
#     if len(lst) == 1:  # базовый случай
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]   # E
#
#
# print(to_str(254, 10))  #

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count

# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count

# def union(s):
#     if not s:  # s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ["Bob", ["chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(union(names))
# print(count_items(names))


# print(type(names) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# print(len(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("   Hello \tWorld Hi  "))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# # print(binary_search(lst, 3))
# print(binary_search(lst, 8))

# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         # print(array)
#         # print("-" * 40)
#
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     # print("l", l)
#     # print("r", r)
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)


# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         print(gap, "Список:", s)
#         gap //= 2
#
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)

# f = open(r"D:\pythonProject4\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(*f)
# print(f)

# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()


# f = open("test.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines(16))
# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
# count = 0
# for line in f:
#     count += 1
# print(count)
# f.close()
# f.writelines(lines)
# f = open('xyz.txt', 'a')
# # print(f.write('New text.'))
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# import codecs

# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# my_file.close()
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# print(f.read(3))
# print(f.tell())  # 3
# print(f.seek(1))  # 1
# print(f.read())
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789\ndsasdfsdfs'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")
#
# with open(file_name, 'r', encoding="utf-8") as f:
#     file_lst = f.read().split()
#
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))

# file_name = "test1.txt"


# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r") as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("test1.txt"))
#
#
# file_name = 'res_1.txt'
# lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть!']
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(' '.join(lst))

# file_name = 'res_1.txt'
# lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть!']
#
#
# def open_file_and_find_max(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         file_lst = f.read().split(' ')
#         max_len = max(len(i) for i in file_lst)
#         new_lst = []
#         for i in file_lst:
#             if len(i) == max_len:
#                 new_lst.append(i)
#         return new_lst
#
#
# print(open_file_and_find_max(file_name))
# def func(file):
#     with open(file, "r") as f:
#         lst = f.read().split()
#         m = max(len(i) for i in lst)
#         print([i for i in lst if len(i) == m])
#
#
# func("test1.txt")

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("one.txt", 'w') as f:
#     f.write(text)
#
# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line, end="")

# os
# os.path

import os

# print("Текущая директория", os.getcwd())  # возвращает текущую директорию (там где *.py)
# print(os.listdir())  # возвращает список директорий и файлов, находящихся в текущей директории (по умолчанию) или в директории по указанному пути
# os.mkdir("folder")  # создает директорию по указанному пути
# os.mkdir("folder1.folder2")
# os.makedirs("folder1/folder2/folder0/folder3/folder4/folder5")  # создаст конечную директорию и также промежуточные папки, если их не # существует

# os.remove("xyz.txt")  # удаляет файл
# os.rename("folder", "test")  # переименовывает файл или папку.
# os.rename("folder1/folder2/ts1.txt", "ts.docx")
# os.renames("text/new_text/tx.txt", "text.txt")  # переименовывает и перемещает файл, создавая промещуточные директории, если их нет

# os.rmdir("test")  # удаляет пустую директорию. Если директория не существует или она не пустая будет ошибка

#  возвращает имена объектов в дереве директорий, обходя это дерево сверху вниз (topdown=True) или снизу вверх (topdown=False)
# for root, dirs, files in os.walk("folder1", topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# for root, dirs, files in os.walk("Work", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

# for root, dirs, files in os.walk("Folder", topdown=True):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f"Директория {root} удалена.")


import os.path

# print(os.path.split(r"D:\pythonProject4\folder1\folder2\folder0\folder3\folder4\folder5\file.txt"))
# # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r"folder5\file.txt"))
# # возаращает имя директории
# print(os.path.basename(r"folder5\file.txt"))
# # возващает имя файла
# print(os.path.join('files', r"D:\pythonProject4", "/folder1", "folder2", "file.txt"))
# # соединяет один или несколько компонентов пути с учетом особенностей OS

# dirs = [r"Work\F1", r"Work\F2\F21"]
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     "Work": ['w.txt'],
#     r"Work\F1": ['f11.txt', 'f12.txt', 'f13.txt'],
#     r"Work\F2\F21": ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, "w").close()
#
# file_with_text = [r'Work\w.txt', r"Work\F1\f12.txt", r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)

# print(os.path.exists(r'D:\pythonProject4\Work\w.txt'))
# # проверяет путь на существование (True - если путь существует)
#
# print(os.path.getctime(r'D:\pythonProject4\text.txt'))  # возвращает время создания файла
# print(os.path.getatime(r'D:\pythonProject4\text.txt'))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(r'D:\pythonProject4\text.txt'))  # возвращает время последнего изменения файлу
# print(os.path.getsize(r'text.txt'))  # возвращает размер файла в байтах

# import time
#
# path = r'C:\Program Files\Adobe\Adobe Photoshop CC 2017\Photoshop.exe'
# # path = "text.txt"
# size = os.path.getsize(path)
# kb = size // 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
# print("Размер:", kb, "KB")
# print("Дата последнего использования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Дата последнего редактирования:", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# print(os.path.normcase("C:/User/admin/Documents"))
# # нормализует регист пути и слеши
# print(os.path.relpath(r"D:\pythonProject4/test1.txt"))
# # возвращает относительный путь
#
# print(os.path.isfile(r"D:\pythonProject4/test1.txt"))
# # возващает True, если концом пути является сущесвтвующий файл
#
# print(os.path.isdir(r"D:\pythonProject4"))
# # возващает True, если концом пути является сущесвтвующая директория

# dir_name = "Work"
#
# objs = os.listdir(dir_name)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")


# def print_tree(root):
#     for rot, dirs, files in os.walk(root, topdown=True):
#         if rot == root:
#             for i in dirs:
#                 print(i, "-dir")
#             for j in files:
#                 print(j, "-file",os.path.getsize(rot+"\\"+j), "byte")
#
#
# print_tree("Work")

# print("Hello")
import re
print("Вносим изменения в склонированный проект")

print("Новые изменения")

s = "google.com and google.ru"
reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
print(re.sub(reg, r'http://\1', s))

