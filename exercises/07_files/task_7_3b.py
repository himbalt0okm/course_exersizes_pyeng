# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

user_number = input('Enter VLAN number: ')

with open("CAM_table.txt", 'r') as f:
    lines = f.readlines()
    result_lst = []
    i=1
    while i <=6:
        lines.pop(0)
        i += 1
        
    for line in lines:
        line = line.strip()
        line = line.split()
        if line[0] == user_number:
        #result_str = 
            result_str = [int(line[0]), line[1],line[3]]
            result_lst.append(result_str)
            result_lst.sort()
    for line in result_lst:
        line = '{:<9}{:<20}{:<0}'.format(str(line[0]), line[1],line[2])
        print(line)