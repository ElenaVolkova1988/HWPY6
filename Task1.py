# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# # Пример:
# # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# import random

# my_list=[ ]
# for _ in range (5):
#     my_list.append(round(random.uniform(0,5),0))        # рандомное заполнение списка из 5 элементов
# sum = 0
# for i in range(len(my_list)):                           # во всем списке ищем нечетные позиции, если индекс делится на 2 с остатком, то нечетный
#     if i % 2 == 1:
#         sum += my_list[i]       
# print(f"{my_list} -> сумма элементов на нечётных позициях: {sum}")

my_list=[2, 3, 5, 9, 3]
print(my_list)

new_list=list(filter(lambda x:my_list.index(x)%2 != 0, my_list))
print(new_list)
print (sum(new_list))