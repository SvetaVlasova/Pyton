# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(n, nd):
#     print(n*(10**nd))
#     n=n*(10**nd)+0.41
#     print(n)
#     n = n//1
#     print (n)
#     return n/(10**nd)
#
# print(my_round(2.1234567, 2))
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

#
# def lucky_ticket(ticket_number):
#    num=str(ticket_number)
#    list1=int(num[0])+int(num[1])+int(num[2])
#    list2=int(num[3])+int(num[4])+int(num[5])
#    if list1 == list2:
#      return True
#    else:
#       return False
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(123213))
# print(lucky_ticket(436751))
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
#
# def fib(n,m):
#     a,b=1,1
#     list=[1,]
#     print(list)
#     for i in range(m):
#          print(i)
#          # a,b=b,a+b
#            sum=b+a
#            a=b
#            b=sum
#           list.append(a)
#           print(list)
#     return list[n-1:m]
#
#
# print('fibonacci(1, 6): ',fib(1,16))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(list):
#    a=0
#    b=1
#    while b<len(list):
#        while a<(len(list)-1):
#            print (list[a],list[a+1] )
#            if list[a]<list[a+1]:
#                list[a],list[a+1]=list[a+1],list[a]
#            else:
#                a+=1
#        b+=1
#        a=0
#    return list
#
# k=sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
# print(k)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# def my_filter(condition,arg):
#     k=list()
#     for i in arg:
#         if condition(i)== 1:
#             k.append(i)
#         else:
#             continue
#     return k
#
# print(my_filter((lambda x: x>0), arg=[2, 10, -12, 2.5, 20, -11, 4, 4, 0]))



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1 = input('Введите координаты x1,y1: ')
k1=a1.split(',')
a2 = input('Введите координаты x2,y2: ')
k2=a2.split(',')
a3 = input('Введите координаты x3,y3: ')
k3=a3.split(',')
a4 = input('Введите координаты x4,y4: ')
k4=a4.split(',')
l1=int(k1[0])+int(k3[0])
l2=int(k1[1])+int(k3[1])
l3=int(k2[0])+int(k4[0])
l4=int(k2[1])+int(k4[1])
print(l1,l2,l3,l4)
if l1==l2 and l3==l4:
    print("ABCD - параллелограмм!")
else:
    print("ABCD не параллелограмм!")



