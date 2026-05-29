year = int(input())
offset = (year - 1984) % 60
animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]
animal = animals[offset % 12]
color = colors[(offset // 2) % 5]
print(f"{animal}, {color}")