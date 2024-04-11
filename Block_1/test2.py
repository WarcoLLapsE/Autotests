from string import ascii_lowercase
from string import digits


nick = input()
flag = True
if not nick.startswith('@'):
    flag = False
if len(nick) < 5 or len(nick) > 15:
    flag = False
for i in nick[1:]:
    if i in ascii_lowercase or i in digits:
        continue
    else:
        flag = False
        break
if flag:
    print('Correct')
else:
    print('Incorrect')
