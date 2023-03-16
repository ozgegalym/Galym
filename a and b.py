# import math
# # for i in map(float,input("Введите три числа через пробел  : ").split()):
# #     if 1 <= i <= 3:
# #         print(f"Число {i} принадлежит интервалу [1, 3]")

# #1
# # def tr1(a,b):  
# #   c=math.sqrt(pow(a,2)+pow(b,2))
# #   return c
# # def tr2(x,y):
# #  z=math.sqrt(pow(x,2)+pow(y,2))
# #  return z
# # if tr1(5,7) > tr2(9,11):
# #     print("Первый треугольник  больше")
# # elif tr1(5,7) == tr2(9,11):
# #     print("треугольники равны ")
# # else:
# #     print("Второй треугольник  больше")

# #2
# def text(stroka):
#    stroka = stroka.split(" ")
#    for i in range(len(stroka)):
#       stroka[i] = ''.join(sorted(stroka[i]))
#       return (stroka)
# print (text("Stroka"))

# #3
# k = int(input())
# for i in range(1, k + 1):
#    n = len(str(i))
#    summ = 0
#    for j in str(i):
#        summ += int(j) ** n
#    if i == summ:
#        print(i, end=' ')

    
# #4
# def tang(a1, a2):
#    tan = a2 / a1
#    return tan
# x1 = int(input("введите х1  координату :"))
# x2 = int(input("введите х2  координату :"))
# y1 = int(input("введите y1  координату :"))
# y2 = int(input("введите y2  координату :"))
# z1 = int(input("введите z1  координату :"))
# z2 = int(input("введите z2  координату :"))
# if tang(x1, x2) < tang(y1, y2) < tang(z1, z2):
#    print(f'X({x1, x2})')
# elif tang(y1, y2) < tang(x1, x2) < tang(z1, z2):
#    print(f'Y({y1, y2})')
# else:
#    print(f'Z({z1, z2}')



# from random import randint
# n=int(input("Введите строк/столбцов матрицы = "))
# a=[[0 for i in range(n)] for j in range(n)]
# for i in range(n):
#     for j in range(n):
#         a[i][j]=randint(1,9)

# #1
# for i in range(n):
#     for j in range(n):
#         print(a[i][j],end=' ')
#     print()
# print("\n")
# for i in range(n):
#     for j in range(n):
#         print(a[j][i],end=' ')
#     print()
  

# sym="Матрицы симметричны"
# for i in range(n):
#     for j in range(i+1, n):
#         if a[i][j]!=a[j][i]:
#             sym='Матрицы не симметричны '
# print(sym)

# #2
# from random import randint
# n=int(input("Введите строк матрицы = "))
# m=int(input("Введите строк матрицы = "))
# a=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         a[i][j]=randint(10,99)

# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=' ')
#     print()
# print("\n")

  
# max=a[0][0]
# k = l = 0
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         if a[i][j] > max:
#             max= a[i][j]
#             k= i 
#             l = j 
# a[0], a[k] = a[k], a[0]
# a[0][0], a[0][l] = a[0][l], a[0][0]
# print("\n")
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=' ')
#     print()

#3
# from random import randint
# n=int(input("Введите строк матрицы = "))
# m=int(input("Введите строк матрицы = "))
# a=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         a[i][j]=randint(10,99)



# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=' ')
#     print()
# print("\n")

# temp_el = []
# for k in range(1, len( a[i][j]), 2):
#     # нахождение наименьшего элемента в строке
#     temp = min(a[i][j][k])
#     # добавление наименьшего элемента в список
#     temp_el.append(temp)

# # вывод результата
# print(temp_el)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],
#           [10, 11, 12]]

# smallest_elements=[]
# for i in range
# smallest_elements = []
# for i in range(1, len(matrix), 2):
#     smallest = min(matrix[i])
#     smallest_elements.append(smallest)

# print(smallest_elements)


# # #4
# from random import randint
# n=int(input("Введите строк матрицы = "))
# m=int(input("Введите строк матрицы = "))
# a=[[0 for i in range(m)] for j in range(n)]
# for i in range(n):
#     for j in range(m):
#         a[i][j]=randint(10,99)

# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=' ')
#     print()
# print("\n")

# max1 = max(map(max, a))
# ind_max1 = a.index(max(a))
# ind_max2 = a[ind_max1].index(max1)
 
# min1 = min(min(a))
# ind_min1 = a.index(min(a))
# ind_min2 = a[ind_min1].index(min1)
 
# a[ind_min1][ind_min2], a[ind_max1][ind_max2] = max1, min1
# print(a[ind_min1][ind_min2],a[ind_max1][ind_max2])
 
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=' ')
#     print()
  

# import pandas as pd

# # создание DataFrame со столбцом 'date' в формате строки даты
# df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
#                    'value': [10, 20, 30]})

# # преобразование строки даты в объект даты/времени
# df['date'] = pd.to_datetime(df['date'])

# # установка индекса временного ряда
# df = df.set_index('date')

# # преобразование значения временного ряда в числовой формат (если необходимо)
# df['value'] = pd.to_numeric(df['value'])

# # сортировка данных по дате/времени (если необходимо)
# df = df.sort_index()

#lab 6 
#1 esep

