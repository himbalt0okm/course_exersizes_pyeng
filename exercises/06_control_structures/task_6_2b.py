# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

address = input()
correct = False

while correct == False:    
    try:
        address_splited = address.split('.')
        if len(address_splited) != 4:
            correct = False
        else:
            for octet in address_splited:
                if not(0 <= int(octet) <= 255):
                    correct = False
                else:
                    correct = True
    except ValueError:
        correct = False
    finally:
        if correct == False:
            print('Неправильный IP-адрес')
            address = input()
            continue
    
if correct == True:
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
