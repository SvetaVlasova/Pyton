# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
#
# import os
#
# path_dir =[('dir_' + str(i + 1)) for  i in range(9)]
# print(path_dir)
#
# def make_dir(dir_name):
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.mkdir(dir_path)
#         print('директория {} создана'.format(dir_name))
#     except FileExistsError:
#         print('директория {} уже существует'.format(dir_name))
#
#
# for i in path_dir:
#     make_dir(i)
#
#
# def remove_dir(dir_name):
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.rmdir(dir_path)
#         print('директория {} удалена'.format(dir_name))
#     except FileExistsError:
#         print('директория {} не удалить'.format(dir_name))
#
#
# for i in path_dir:
#     remove_dir(i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# import os
# files = os.listdir(path=os.getcwd())
# print(files)
#
# #--------------------------------------------------
#
# def list_dir(main_path):
#     for i in os.listdir(main_path):
#         print(i)
#
# main_path=os.getcwd()
# list_dir(main_path)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# import shutil
# import sys
#
# def copy_file(file,file_new):
#     shutil.copy(file,file_new)
#
# file=sys.argv[0]
# print(file)
# file_new=file+'.backup'
# print(file_new)
# copy_file(file,file_new)

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("change_dir <dir_name> - переход в директорию")
    print("list_dir <dir_name> - вывести содержимое директории")
    print("make_dir <dir_name> - создать папку с именем")
    print("remove_dir <dir_name> - удалить папку с именем")


def change_dir():
    try:
        os.chdir(dir_name)
        print("Успешно перешел в директорию:", dir_name)
    except:
        print ("Такой директории нет!")




def list_dir():
     for i in os.listdir():
         print(i)


def make_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def remove_dir():
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(dir_name))
    except FileExistsError:
        print('директория {} не удалить'.format(dir_name))


do = {
    "help": print_help,
    "change_dir": change_dir,
    "list_dir": list_dir,
    "make_dir": make_dir,
    "remove_dir": remove_dir
}
try:
      dir_name = sys.argv[2]

except:
       dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
           do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
