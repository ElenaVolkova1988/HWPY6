# # 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 6782 -> 23
# # 0,56 -> 11

# n=input("Введите число:")
# n_lst = list( str(n) )
# n_sum = 0
# for i in range( len(n_lst) ):
#     if i != ".":
#         n_sum += int( n_lst[i] )
# print( n_sum )   


print(list(map(lambda x: sum(int(i) for i in str(x)),list(map(int,input("Введите число: ").split())))))