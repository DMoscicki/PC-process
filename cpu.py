import os, psutil
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Процессы

pid = psutil.pids()
print(f'Количество открытых хэндлов: {(pid)}')
time_user = int(input()) #ввод интервал
while time_user != 0:
    # pid = psutil.pids()
    p = psutil.Process()
    mu = p.memory_info()
    cpu = psutil.cpu_percent(interval=time_user)
    # print(len(pid))
    cpu_percent = (f"Загрузка процессора в %", ":", cpu)
    ws = (f"Working set",  ":", mu.wset)
    vms = (f"Private bytes",':', mu.vms)
    # print(''.join(map(str, cpu_percent)))
    # print(''.join(map(str, ws)))
    # print(''.join(map(str, vms)))
    f = open('info.txt', 'w')
    f.write(''.join(map(str, cpu_percent))+'\n')
    f.write(''.join(map(str, ws))+'\n')
    f.write(''.join(map(str, vms))+'\n')
    f.close()
    check_file = open('info.txt', 'r')
    for line in check_file:
        print(f'Got line: {line}')
    check_file.close()
print("Введите пожалуйста другое значение")

