from jinja2 import Environment, FileSystemLoader

subs = ["Культура", "Наука", "Политика", "Спорт"]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)

# html = '''
# {% macro list_users(users) %}
# <ul>
# {% for u in users -%}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor -%}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>
#         <li>weight: {{ user.weight }}</li>
#     </ul>
# {% endcall %}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)

# html = """
# {% macro input(name, placeholder, type='text') -%}
# <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro %}
#
# <p>{{ input("firstname", "Имя") }}</p>
# <p>{{ input("lastname", "Фамилия") }}</p>
# <p>{{ input("address", "Адрес") }}</p>
# <p>{{ input("phone", "Телефон", "tel") }}</p>
# <p>{{ input("email", "Почта", "email") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0},
# ]
#
# tpl = """
# {%- for u in users -%}
# {# {% filter upper %}{{ u.name }}{% endfilter %} #}
# {% filter string %}{{ u.year }} - {{ u.weight }}{% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17000},
#     {'model': 'Renault', 'price': 44000},
#     {'model': 'Wolksvagen', 'price': 21000},
# ]
#
# lst = [1, 2, 3, 4, 5, 6]
#
# tpl = "Суммарная цена автомобилей {{ cs | replace('model', 'brand') }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """
#
# """
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Житомир'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = '''<select name="cities">
# {% for c in cities -%}
#     {% if c.id > 3 -%}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == "Москва" -%}
#         <option>{{ c['city'] }}</option>
#     {% else -%}
#         {{ c['city'] }}
#     {% endif -%}
# {% endfor -%}
# </select>'''
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# link = "<a href='#'>Ссылка</a>"
#
# tm = Template("{{ link | e}}")
# msg = tm.render(link=link)
#
# print(msg)

# data = """{%raw%}Модуль Jihja вместо
# определения {{ name }}
# подставит соответствующее значение{%endraw%}
# """
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Привет {{ p.get_name() }}. ")
# msg = tm.render(p=per)
#
# print(msg)


# name = "Игорь"
# age = 28
# per = {'name': 'Игорь', 'age': 28}
#
# # tm = Template("Мне {{ p.age }} лет. Привет {{ p.name }}. ")
# tm = Template("Мне {{ p['age'] }} лет. Привет {{ p['name'] }}. ")
# msg = tm.render(p=per)
#
# print(msg)
