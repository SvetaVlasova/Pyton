# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#
# import math
# def side(x1, x2):
#              return math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])** 2)
#
# class Triangle:
#     def __init__(self, A, B, C):
#       self.A = A
#       self.B = B
#       self.C = C
#       self.AB = side(self.A, self.B)
#       self.BC = side(self.B, self.C)
#       self.CA = side(self.C, self.A)
#
#     ###периметр фигуры
#     def perimeter(self):
#         return self.AB + self.BC + self.CA
#
#     #####площадь
#     def ploshad(self):
#         k = self.perimeter() / 2
#         return math.sqrt(k * (k - self.AB) * (k - self.BC)* (k - self.CA))
#
#     ###высота
#     def height(self):
#          return self.ploshad() / (self.AB / 2)
#
#
# line=Triangle((3,2),(6,7),(0,12))
# print(line.perimeter())
# print(line.ploshad())
# print(line.height())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
#
# import math
# def side(x1, x2):
#              return math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])** 2)
#
# class Trapeze:
#     def __init__(self, A, B, C,D):
#       self.A = A
#       self.B = B
#       self.C = C
#       self.D = D
#       self.AB = round(side(self.A, self.B),2)
#       self.BC = round(side(self.B, self.C),2)
#       self.CD = round(side(self.C, self.D),2)
#       self.DA = round(side(self.D, self.A),2)
#       self.AC_d = round(side(self.A, self.C),2)
#       self.BD_d = round(side(self.A, self.C),2)
#     ##периметр трапеции
#     def perimeter(self):
#           return round((self.AB + self.BC + self.CD + self.DA),2)
#     ##площадь через высоту
#     def plochad(self):
#         h=math.sqrt(self.AB**2-(((self.DA-self.BC)**2+self.AB**2-self.CD**2)/(2*(self.DA-self.BC)))**2)
#         return round(((self.DA+self.BC)/2 * h),2)
#
#     ###проверка, что трапеция равнобедренная
#     def check(self):
#         if self.AC_d == self.BD_d:
#             print("Трапеция равнобедренная!")
#         else:
#              print("Трапеция неравнобедренная!")
#
#
# line=Trapeze((0,0),(2,8),(12,8),(14,0))
# print("Периметр равен " + str(line.perimeter()))
# print("Сторона АВ = {}, BC = {}, CD = {}, DA = {} ".format(line.AB, line.BC, line.CD, line.DA))
# print("Площадь равна " + str(line.plochad()))
# line.check()


# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class People:
    def __init__(self, name, last_name, surname):
        self.name = name
        self.last_name = last_name
        self.surname = surname

    def get_name(self):
        return self.name + " " + self.last_name + " " + self.surname
    def short_name(self):
       return self.name + " " +  self.last_name[0] + "." + self.surname[0] + "."

    def __str__(self):
        return self.name + " " + self.last_name + " " + self.surname

#list=People('Василий', 'Иванович', 'Иванов')
#print(list.get_name())
# print (list.short_name())

class Student(People):
    class_room=[]
    def __init__(self, name, last_name, surname, mother, father, class_room ):
        super().__init__(name, last_name, surname)
        self.mother = mother
        self.father = father
        self.class_room = class_room

    def get_class_room(self):
        return  self.class_room

    def get_parents(self):
        return self.mother.get_name(), self.father.get_name()


# st =  Student('Василий', 'Иванович', 'Иванов', 'Анна Ивановна', 'Алексанр Семенович', '7а')
# print(st.get_class_room())
# print(st.short_name())
#print(st)


class Teacher(People):
     def __init__(self, name, last_name, surname, class_t, subject):
         super().__init__(name, last_name, surname)
         self.subject = subject
         self.class_t = class_t
     def get_subject(self):
         return self.subject
     def class_teah(self):
         return self.class_t




class_2=['1A','11B','7D','10B']

teachers = [Teacher('Иван', 'Иванович', 'Иванов',[class_2[0],class_2[3]],'Математика'),
            Teacher('Петр', 'Петрович', 'Петров',[class_2[0],class_2[2], class_2[3]], 'Литература'),
            Teacher('Сидор', 'Сидорович', 'Сидоров',class_2[0], 'Физика'),
            Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', [class_2[1],class_2[3],class_2[2]],'Рисование'),
            Teacher('Никита', 'Никитиевич', 'Никишин',class_2[3],'Биология')]


##print(teachers[1].get_subject())


#
# for i in teachers:
#     print(i.get_subject())




mother_father = [People('Светлана', 'Борисовна', 'Власова'),
                People('Элла', 'Николаевна', 'Забродина'),
                People('Александр', 'Романович', 'Власов'),
                People('Анастасия', 'Юрьевна', 'Клюшкина'),
                People('Сергей', 'Сергеевич', 'Забродин'),
                People('Андрей', 'Викторович', 'Клюшкин')]

students = [Student('Игорь', 'Cеменович', 'Забродин', mother_father[1], mother_father[4], class_2[0]),
            Student('Ольга', 'Романова', 'Власова', mother_father[0], mother_father[2], class_2[1]),
            Student('Александр', 'Сергеевич', 'Клюшкин', mother_father[3], mother_father[5], class_2[2])]


#вывод классов через учеников
# for i in students:
#     print(i.get_class_room())

###Получить список всех учеников в указанном классе
# for i in range(len(class_2)):
#     k = class_2[i]
#     print("Ученики в классе {}:".format(k))
#     list = [j.short_name() for j in students if j.get_class_room() == k]
#     print(list)

####Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)

for i in students:
    print("Ученик: {}".format(i.get_name()))
    kl=i.get_class_room()
    print("Класс: {}".format(kl))
    teach = [j.get_name() for j in teachers if i.get_class_room() in j.class_teah()]
    print("Учителя ученика: {}".format(teach))
    sub = [j.get_subject() for j in teachers if i.get_class_room() in j.class_teah()]
    print("Предметы: {}".format(sub))

# 4. Узнать ФИО родителей указанного ученика
# for i in students:
#     print("Родители ученика {}:".format(i))
#     print(i.get_parents())



# 5. Получить список всех Учителей, преподающих в указанном классе
# for i in range(len(class_2)):
#    k = class_2[i]
#    print(k)
#    teach = [j.get_name() for j in teachers if k in j.class_teah()]
#    print(teach)


