# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt', 'r') as f: 
    for line in f:
        r_dict = {'Prefix': '',               
                'AD/Metric':'' ,            
                'Next-Hop':'',              
                'Last update':'',           
                'Outbound Interface':''}
        
        line_list = line.split()
        r_dict['Prefix'] = line_list[1]
        r_dict['AD/Metric'] = line_list[2].replace('[', '').replace(']', '')
        r_dict['Next-Hop'] = line_list[4]
        r_dict['Last update'] = line_list[5]
        r_dict['Outbound Interface'] = line_list[6]
        #print(r_dict)
        for key in r_dict:
            print('{:<22}{:<15}'.format(key, r_dict[key]))
        print('\n')