import psutil
import os
from time import sleep
import datetime
import subprocess
from pathlib import Path

nowstrp = '%Y-%m-%d %H:%M:%S'
file_path = os.path.join(Path(__file__).parent, 'log.txt')

def log(date_,resource):
    with open(file_path, 'a') as file:
        file.write(f'{date_} : {resource}\n')
with open (file_path, 'w+') as file:
    file.write('')
    
user = ''
print(f'\033[32m\t{'-'*15}Monitoramento do Computador{'-'*15}\033[m')

print('1 - Verificar CPU')
print('2 - Verificar memória')
print('3 - Verificar espaço no disco')
print('4 - QUIT')

while user != 4:
    user = int(input('Digite a opção: '))

    if user == 1:
        now__ = datetime.datetime.now()
        sleep(1)
        cpu = psutil.cpu_stats()
        print(f'CPU switches: {cpu.ctx_switches}')
        print(f'CPU interrupts: {cpu.interrupts}')
        print(f'CPU soft interrupts: {cpu.soft_interrupts}')
        print(f'Syscalls: {cpu.syscalls}')
        cpupercent = psutil.cpu_percent()
        print(f'Uso da CPU: {cpupercent}%')
        if 95 > cpupercent > 85 :
            print('\033[31mSua CPU está sobre carregada.\033[m')
        if cpupercent > 95:
            print('\033[31mDesligue seu computador imediatamente!\033[m')
        
        log(date_=datetime.datetime.strftime(now__, nowstrp), resource=cpu)
        
    elif user == 2:
        now__ = datetime.datetime.now()
        memory = psutil.virtual_memory()
        sleep(1)
        print(f'Total de memória: {memory.total} bytes')
        print(f'Memória disponível: {memory.available} bytes')
        print(f'Uso da memória: {memory.percent}%')
        log(date_ = datetime.datetime.strftime(now__,nowstrp), resource=memory)
        if memory.percent > 90:
            print('\033[31mSua memória está sobrecarregada!\033[m')
    elif user == 3:

        cmdsub = subprocess.run('fsutil volume diskfree C:', text=True, shell= True, encoding='cp850')

    elif user == 4:
        quit()
    
    else:
        print('Opção inválida, por favor digite novamente.')