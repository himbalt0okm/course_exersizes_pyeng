# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess
import ipaddress

def ping_ip_addresses(ip_list):
    reachable = []
    unreachable = []

    for ip in ip_list:
        try:
            # Проверяем, является ли адрес валидным IP
            ipaddress.ip_address(ip)

            # Выполняем ping
            result = subprocess.run(['ping', '-c', '3', '-n', ip], 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL)

            if result.returncode == 0:
                reachable.append(ip)
            else:
                unreachable.append(ip)
        except ValueError:
            print(f"Неверный IP-адрес: {ip}")
            continue

    return (reachable, unreachable)
