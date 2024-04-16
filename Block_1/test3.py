car_number = input()
possible_letters = 'АВЕКМНОРСТУХ'
print(car_number[0] in possible_letters)
print(car_number[1:4].isdigit())
print(car_number[4:6].split())
print(car_number[6:7] == '_')
print(car_number[7:].isdigit())
