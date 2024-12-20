# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

address = input()
incorrect = False
try:
    address_splited = address.split('.')
    if len(address_splited) != 4:
        incorrect = True
    else:
        for octet in address_splited:
            if not(0 <= int(octet) <= 255):
                incorrect = True
except ValueError:
    incorrect = True
    
if incorrect == True:
    print('Неправильный IP-адрес')
else:
    if 1 <= int(address_splited[0]) <= 223:
        print('unicast')
    elif 224 <= int(address_splited[0]) <= 239:
        print('multicast')
    elif address == '255.255.255.255':
        print('local broadcast')
    elif address == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')