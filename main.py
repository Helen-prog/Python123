from car import electrocar

print("Создадим класс Автомобиль со свойствами бренд, модель, год выпуска и пробег. Он будет иметь метод\nвывода "
      "данных на экран. От него будет унаследован класс Электро автомобиль с мощностью батареи 100%.\n"
      "Работа с классами должна быть организована через пакет и модули.\n")
e = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
e.show_car()
e.description_battery()