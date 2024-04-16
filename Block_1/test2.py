day, weight = int(input()), float(input())
if weight > 100 - day * 0.2:
    print(f'''Что-то пошло не так
#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - day * 0.2}''')
else:
    print(f'''Все идет по плану
#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {100 - day * 0.2}''')