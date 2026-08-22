# newlist = [expression for item in iterable (if condition)]


# numbers = [-3, -2, -1, 0, 1, 2, 3]
# positive_numbers = [n for n in numbers if n > 0]
  
# print(positive_numbers)



# numbers = [1, 2, 3, 4, 5]

# result = [i ** 2 for i in numbers]

# print(result)



# numbers = [1, 2, 3, 4, 5, 6]

# result = [i for i in numbers if i % 2 == 0]

# print(result)



# numbers = [-5, 10, -3, 7, -8]

# result = [0 if i < 0 else i for i in numbers]

# print(result)



# фильтрует список
# [i for i in numbers if i > 0]

# заменяет/преобразует элементы
# [0 if i < 0 else i for i in numbers]



# numbers = [i for i in range(1, 11)]

# print(numbers)



# names = ["alex", "bob", "john"]

# result = [name.upper() for name in names]

# print(result)



# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = [i for row in numbers for i in row]

# print(result)



# 1. Обычный
# [что_делаем for i in список]
# 2. С фильтрацией
# [что_делаем for i in список if условие]
# 3. С if/else
# [значение_если_да if условие else значение_если_нет for i in список]
# 4. С вложенным циклом
# [что_делаем for i in список for j in i]


