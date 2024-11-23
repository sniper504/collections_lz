N = int(input("Введите значение N: "))

# Список для хранения ряда Фибоначчи
fib_list = [0, 1]

# Заполнение списка до элемента N
for i in range(2, N):
    fib_list.append(fib_list[-1] + fib_list[-2])

# Обработка элементов списка
processed_list = []
for num in fib_list:
    if num % 2 == 0:
        processed_list.append(num * 2)
    else:
        processed_list.append(num ** 2)

# Нахождение минимального и максимального элемента
min_elem = min(processed_list)
max_elem = max(processed_list)

# Длина списка
list_length = len(processed_list)

# Нахождение медианного значения
sorted_list = sorted(processed_list)
if list_length % 2 == 0:
    median = (sorted_list[list_length // 2 - 1] + sorted_list[list_length // 2]) / 2
else:
    median = sorted_list[list_length // 2]

# Подсчет элементов больше медианного значения
greater_than_median_count = len([x for x in processed_list if x > median])

# Вывод результатов
print("Список Фибоначчи:", fib_list)
print("Обработанный список:", processed_list)
print("Минимальный элемент:", min_elem)
print("Максимальный элемент:", max_elem)
print("Длина списка:", list_length)
print("Количество элементов больше медианного значения:", greater_than_median_count)
