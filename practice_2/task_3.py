# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input()
height = input()


#Ваш кол
# Запрашиваем у пользователя вес и рост
weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))

# Рассчитываем индекс массы тела (BMI)
bmi = weight / height**2

# Выводим результат
print(f"Ваш индекс массы тела (BMI): {bmi:.2f}")
