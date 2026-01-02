import os
import subprocess
from random import randint
easy_base=[]
gaps_all_delete=[]
samsung_services=[]
current_directory = os.getcwd()
with open ('easy_base.txt','r') as file:
    easy_base=file.readlines()
with open ("gaps_all_delete.txt",'r') as file:
    gaps_all_delete=file.readlines()
with open ('samsung_services.txt','r') as file:
    samsung_services=file.readlines()
with open ('policy_status.txt','r') as file:
    policy_status=file.read()
    if 'Ознакомлен' not in policy_status:
        policy_user=input('Перед использованием ПО ознакомьтесь с условиями использованиями\n1 - Ознакомиться\nexit - Выйти\n>>>')
        if policy_user=='1':
            with open ('policy.txt','r') as file:
                policy=file.read()
                print(policy,'\n')
                policy_status_user=input('1 - С условиями согласен\nexit - С условиями не согласен\n>>>')
                if policy_status_user=='1':
                    with open ('policy_status.txt','w') as file:
                        file.write('Ознакомлен')
                else:
                    os.abort()
        else:
            os.abort()

#комманды
root_check_command='./adb shell su'
device_info_root_command='./adb shell su & ./adb shell cat /system/build.proc'

programm=True
start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
while programm:
    if start == '1':
        print('Устройства ADB:')
        os.system('./adb devices')
        print('Устройства Fastboot:')
        os.system('./fastboot devices')
        start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
    elif start == '2':
        delete_script=input('Выберите действие для смартфона\n1 - Общее удаление хлама из прошивки \n2 - Удаление гугл сервисов\n3 - Полное удаление сервисов samsung\n>>>')
        if delete_script=='1':
            for i in easy_base:
                subprocess.run(['./adb','shell','pm','uninstall','-k','--user 0',i])
            start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
        elif delete_script=='2':
            for i in gaps_all_delete:
                subprocess.run(['./adb','shell','pm','uninstall','-k','--user 0',i])
            start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
        elif delete_script=='3':
            for i in samsung_services:
                subprocess.run(['./adb','shell','pm','uninstall','-k','--user 0',i])
            start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
        else:
            start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
    elif start == '4':
        start_root=input('1 - Вывести подробную информацию об устройстве\nexit - Выйти\n>>>')
        if start_root == '1':
            os.system(device_info_root_command)
        start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
    elif start == '3':
        subprocess.run(['./adb', 'pull' ,'/sdcard/DCIM',current_directory])
        print('Передача файлов завершена')
        start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
    elif start == '5':
        print('Вы уверены? Данная функкция уничтожит вашу систему! Вы, вероятно, столкнетесь с bootloop! Использовать только в экстренных случаях')
        kill_or_not=input('Вы уверены? yes - подтвердить')
        if kill_or_not=='yes':
            os.system('./adb shell pm uninstall -k --user 0 android')
            print('Устройство уничтожено')
        start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')      
    elif start == 'exit':
        print('Прекращаем работу программы...')
        programm=False
    else:
        print('Действие не найдено')
        start=input('Выберите действие:\n1 - Подключенные устройства\n2 - Удаление приложений\n3 - Импорт фотографий и приложений\n4 - Функции ROOT\n5 - УБИТЬ УСТРОЙСТВО(НЕ ИСПОЛЬЗОВАТЬ!)\nexit - Выйти\n>>>')
