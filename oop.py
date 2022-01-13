# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coords(5, 10)
# # print(p1.__dict__)
# Point.set_coords(p1, 3, 8)
# p2 = Point()
# p2.set_coords(40, 80)
# p1.x = 5
# p1.y = 10
# print(type(p1))
# print(type(p1) == Point)
# print(isinstance(p1, Point))


# p1.x = 5
# p1.y = 10
# # p1.z = 20
# print(p1.x, p1.y, Point.x)
# # print(getattr(p1, "z", "False"))
# setattr(p1, "z", 7)
# print(hasattr(p1, "x"))
# print(hasattr(p1, "z"))
# delattr(p1, "z")

# print(p1.__dict__)
# print(p1.__dict__)
# print(Point.__dict__)
# p2 = Point()
# print(p2.x, p2.y)
# Point.x = 100
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))
# a = """Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
# """
# print(a)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "Street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем имя
#         """устанавливает имя"""
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Ирина")
# print(h1.get_name())
# h1.set_birthday("15.07.2002")
# print(h1.get_birthday())
# h1.print_info()

# class Person:
#     skill = 10  # квалификация сотрудника
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         res = f"Данные сотрудника: {self.name} {self.surname}"
#         print(res)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника {self.name}: {self.skill}")
#
#
# p1 = Person()
# p1.print_info("Viktor", "Reznik")
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info("Anna", "Dolgih")
# p2.add_skill(2)

# def sum_arg(a, b):
#     print(a + b)
#
#
# sum_arg(5, 2)
# sum_arg("Hello", "world")


# __магическийМетод__

# Специальные методы
# конструктор  __new__
# инициализатор  __init__
# деструктор  __del__


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# # p1.set_coords(2.3, 5.6)
# print(p1.get_coords())
# print(p1.__dict__)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# droid3 = Robot("PO")
# droid4 = Robot("P4")
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
# del droid4

# print("Численность роботов:", Robot.k)

# class Point:
#     WIDTH = 5
#     z = 100
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
#
#     # def __getattr__(self, name):
#     #     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"
#
#     # def __getattribute__(self, item):
#     #     if item == "_Point__x":
#     #         return 0
#     #     else:
#     #         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == "z":
#             raise AttributeError
#         else:
#             self.__dict__[key] = value
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#     def area(self):
#         return (self.__x * self.__y) + self.z
#
#
# p1 = Point(5, 10)
# print(p1.__x)
# print(p1._Point__x)
# print(p1.zzz)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# p1.z = 200
# Point.WIDTH = 10
# print(p1.area())
# p1.set_coords_x(100)
# p1.set_coords_y(50)
# print(p1.get_coords())
# print(p1.get_coords_x())
# print(p1.get_coords_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)
# print(p1.__x, p1.__y)
# p1.__x = 100
# p1.__y = "abc"
# print(p1.__x, p1.__y)

# Инкапсуляция
# x - public
# _x - protected
# __x - private

# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print('Длина прямоугольника', rec1.get_length())
# print('Ширина прямоугольника', rec1.get_width())
# print('Площадь', rec1.square())
# print('Периметр', rec1.perimetr())
# print('Гипотенуза', round(rec1.hypo(), 2))
# rec1.get_draw()

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Невервный формат данных")
#
#     def __get_coords_x(self):
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# # p1.coordX = 100
# # print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property   # геттер
#     def coords_x(self):
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Невервный формат данных")
#
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# del p1.coords_x
# p1.coords_x = 7
# print(p1.coords_x)
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Киллограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.kg)
# print(w.to_pounds())
# w.kg = "десять"
# print(w.to_pounds())


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# # def get_count():
# #     return Point.count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())
# print(p3.get_count())
# print(get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2021',
#     '30-12-2020',
#     '01.01.2021',
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_db()
#         # db = Date.string_to_db(date)
#         print(db)
#     else:
#         print("Неправильная дата или формат строки с датой")

# d = "16.12.2021"
# day, month, year = map(int, d.split("."))
# print(day, month, year)
# d = Date()
# date = d.from_string("16.12.2021")
# print(date.string_to_db())
# d1 = Date()
# date1 = d1.from_string("03.12.2020")
# print(date1.string_to_db())
# date2 = Date.from_string("15.10.2021")
# print(date2.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname  # фамилия владельца
#         self.num = num  # номер счета
#         self.percent = percent  # процент начисления
#         self.value = value  # сумма в рублях
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):  # редактирование курса рубля по отношению к долару
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):  # редактирование курса рубля по отношению к евро
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):  # смена владельца счета
#         self.surname = surname
#
#     def convert_to_usd(self):  # перевод в долары
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):  # перевод
#         eur_val = Account.convert(self.value, Account.rate_euro)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def add_persents(self):  # начисление процентов
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # снятие заданной суммы
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):  # вывод информации о счете
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_persents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         print("Инициализатор базового класса Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         # self.__width = 5
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.__width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# print(line.__dict__)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Значние ширины должно быть больше нуля")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Значние высоты должно быть больше нуля")
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         # return self.color
#         return self.width * self.height
#         # return self.border_new()
#
#
# rect = Rectangle(10, 20, "green", "1px solid gray")
# print(rect.area())
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.border)
# rect.width = 50
# print(rect.width)
# print(rect.area())


# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # плотность жидкости
#
#     def edit_density(self, val):  # изменение плотности
#         self._density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         res = m / self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v): # вычисление массы жидкости соотвертствующее заданному объему
#         res = v * self._density
#         print(f"Вес {v} m^3 {self._name} составляет {res} кг.")
#         return res
#
#     def print_info(self):
#         print(f"Жидкость {self._name} плотность = {self._density} kg/m^3.")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40.2), Point(100, 200))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self.__name = name
#         self.__density = density  # плотность жидкости
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, change_name):
#         self.__name = change_name
#
#     @property
#     def density(self):
#         return self.__density
#
#     @density.setter
#     def density(self, value):
#         self.__density = value
#
#     def edit_density(self, val):  # изменение плотности
#         self.__density = val
#
#     def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
#         res = m / self.__density
#         print(f"Объем {m} кг {self.__name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v):  # вычисление массы жидкости соотвертствующее заданному объему
#         res = v * self.__density
#         print(f"Вес {v} m^3 {self.__name} составляет {res} кг.")
#         return res
#
#     def print_info(self):
#         print(f"Жидкость {self.__name} плотность = {self.__density} kg/m^3,", end=" ")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m):  # переопределение вычисление объема жидкости, соответствующего заданной массе
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f"Объем алкоголя в {m} кг {self.name} составляет {v_alc} m^3.")
#         return v, v_alc
#
#     def calc_m(self, v):  # переопределение вычисление массы жидкости соотвертствующее заданному объему
#         m = super().calc_m(v)
#         m_alc = v * self.strength
#         print(f"Вес алкоголя {v} m^3 {self.name} составляет {m_alc} кг.")
#         return m, m_alc
#
#     def print_info(self):
#         super().print_info()
#         print(f"крепость = {self.strength:.0%}")
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)
#
# a.print_info()
# ===================================================================================
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# =============================================================================
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # f = ["Фамилия", "Имя", "Отчество"]
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))  # "ФамилияИмяОтчество"
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должне быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80)
# p1.fio = "Соболев Игорь Николаевич"
# p1.weight = 60
# p1.password = "4567 123456"
# p1.old = 35
# print(p1.__dict__)
# =========================================================================
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()
# line.set_coords(Point(3, 4), Point(1, 2))
# line.draw_line()

# ===========================================================
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):  # абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod
#
#
# # абстрактный класс
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигру")
#
#     @abstractmethod
#     def move(self):  # абстрактный метод
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()
# from math import pi
#
#
# class Table:
#
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# t.set_sides(2)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = Round_table(radius=10)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = Round_table(radius=20)
# t2.set_radius(60)
# print(t2.__dict__)
# print(t2.calc_area())
# ======================================================
# from math import sqrt
# from abc import ABC, abstractmethod
#
#
# class Root(ABC):
#     def __init__(self):
#         self.equation = ''
#         self.res = []
#
#     @abstractmethod
#     def calculate(self):
#         pass
#
#     def print(self):
#         if len(self.res) == 0:
#             print(f'The equation {self.equation} has no roots!')
#         elif len(self.res) == 1:
#             print(f'The root of {self.equation} is: {self.res[0]}')
#         else:
#             print(f'The roots of {self.equation} are: {",".join(map(str, self.res))}')
#
#
# class Linear(Root):
#     # ax + b = 0 -> x = -b/a
#     def __init__(self, a, b):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.equation = f'{a}x{b:+}=0'
#
#     def calculate(self):
#         res = round(-self.b / self.a, 2)
#         self.res.append(res)
#
#
# class Quadratic(Root):
#     # ax^2 + bx + c = 0 -> D = b^2 - 4ac -> x = (-b +/- vD) / (2a)
#     def __init__(self, a, b, c):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.c = c
#         self.equation = f'{a}x^2{b:+}x{c:+}=0'
#
#     def calculate(self):
#         d = self.b ** 2 - 4 * self.a * self.c
#         if d == 0:
#             x = round(-self.b / (2 * self.a), 2)
#             self.res.append(x)
#         elif d > 0:
#             x1 = round((-self.b + sqrt(d)) / (2 * self.a), 2)
#             x2 = round((-self.b - sqrt(d)) / (2 * self.a), 2)
#             self.res.extend([x1, x2])
#
#
# l_eq = Linear(3, 7)
# l_eq.calculate()
# l_eq.print()
# print()
# q_eq = Quadratic(1, -2, -3)  # roots: 3, -1
# q_eq.calculate()
# q_eq.print()
# # ================================================================== Андрей Валерьевич
# from abc import ABC, abstractmethod
# import math
#
#
# class Root(ABC):
#
#     @abstractmethod
#     def line(self, a, b):
#         if a == 0 and b == 0:
#             print('Бесконечность')
#         elif a != 0 and (b == 0 or a <= b):
#             print(f"The root of '3x+7=0' is: {round((-b / a), 2)}")
#         else:
#             raise TypeError('Корней нет')
#
#     @abstractmethod
#     def quad(self, a, b, c):
#         d = b ** 2 + 4 * a * c
#         if d > 0:
#             x1 = (b + math.sqrt(d)) / (2 * a)
#             x2 = (b - math.sqrt(d)) / (2 * a)
#             print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
#         elif d == 0:
#             x = b / (2 * a)
#             print(f"Корень = {x}")
#         else:
#             print("Корней нет")
#
#
# class Linear(Root):
#     def line(self, a, b):
#         super().line(a, b)
#
#     def quad(self, a, b, c):
#         super().quad(a, b, c)
#
#
# p1 = Linear()
# p1.line(3, 7)
# p2 = Linear()
# p2.quad(1, 2, 3)
# ================================================
# from abc import ABC, abstractmethod
# import math
#
#
# class Root(ABC):
#
#     @abstractmethod
#     def calc(self):
#         pass
#
#
# class Linear(Root):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def calc(self):
#         if self.a == 0 and self.b == 0:
#             print('Бесконечность')
#         elif self.a != 0 and (self.b == 0 or self.a <= self.b):
#             print(f"The root of '3x+7=0' is: {round((-self.b / self.a), 2)}")
#         else:
#             raise TypeError('Корней нет')
#
#
# class Quadratic:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def calc(self):
#         d = self.b ** 2 + 4 * self.a * self.c
#         if d > 0:
#             x1 = (self.b + math.sqrt(d)) / (2 * self.a)
#             x2 = (self.b - math.sqrt(d)) / (2 * self.a)
#             print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
#         elif d == 0:
#             x = self.b / (2 * self.a)
#             print(f"Корень = {x}")
#         else:
#             print("Корней нет")
#
#
# p1 = Linear(3, 7)
# p1.calc()
# p2 = Quadratic(1, 2, 3)
# p2.calc()
# ================================================

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')

# from abc import ABC, abstractmethod
#
#
# class IFather(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(IFather):
#     def display1(self):
#         print("Child Class")
#         print("Display 1 Abstract Method")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#         print("Display 2 Abstract Method")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Я являюсь связующим методом объекта внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод внутреннего класса")
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#             print(self.obj.name)
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# inner.inner_method()

# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print("Degree:", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print("Degree:", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# d2.display()

# class Geeksforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is an inner class of inner class")
#
#
# outer = Geeksforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class OS:
#     def system(self):
#         return "Windows 10"
#
#
# class CPU:
#     def make(self):
#         return "Intel"
#
#     def model(self):
#         return "Core-i7"

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         # self.os = self.OS()
#         # self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.OS()
# my_cpu = comp.CPU()
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#
#         def display2(self):
#             print("Inner of SubClass")
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is braking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.sleep()

# class A(object):
#     pass
#
#
# class AA(object):
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(AA):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(D.mro())

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Styles:
    def __init__(self, color="red", width=1):
        print("Инициализатор Styles")
        self._color = color
        self._width = width


class Pos:
    def __init__(self, sp: Point, ep: Point, *args):
        print("Инициализатор Pos")
        self._sp = sp
        self._ep = ep
        Styles.__init__(self, *args)


class Line(Pos, Styles):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
l1.draw()
