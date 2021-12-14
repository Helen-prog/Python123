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

class Point:
    WIDTH = 5
    z = 100

    def __init__(self, x, y):
        self.__x = x
        self.__y = y



    # def __getattr__(self, name):
    #     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"

    # def __getattribute__(self, item):
    #     if item == "_Point__x":
    #         return 0
    #     else:
    #         return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError
        else:
            self.__dict__[key] = value

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coords(self, x, y):
        if Point.check_val(x) and Point.check_val(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def set_coords_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")

    def set_coords_y(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coords(self):
        return self.__x, self.__y

    def get_coords_x(self):
        return self.__x

    def get_coords_y(self):
        return self.__y

    def area(self):
        return (self.__x * self.__y) + self.z


p1 = Point(5, 10)
# print(p1.__x)
# print(p1._Point__x)
# print(p1.zzz)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# p1.z = 200
# Point.WIDTH = 10
print(p1.area())
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
