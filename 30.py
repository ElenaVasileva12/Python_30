# Заполните список элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a=int(input('Введите первый элемент: '))
d=int(input('Введите разность: '))
n=int(input('Введите количество элементов: '))

list1=[a+(i-1)*d for i in range(1,n+1)]
print(*list1)

# list1=list()
# for i in range(1,n+1):
#     i=a+(i-1)*d
#     list1.append(i)
# print(*list1)