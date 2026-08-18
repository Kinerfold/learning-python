# range(start, stop, step)

# с range нужны для перебирки чисел. без range нужно, чтобы перебирать объекты, пройтись по объектам



# for i in range(1, 6):
#     print('Шаг', i ** 2)



# for i in range(1, 21):
#     print(i)



# for i in range(1, 16):
#     if i % 2:
#         print(i)



# for i in range(1, 11):
#     print(i * 5)



# for i in range(10, 0, -1):
#     print(i)



# total = 0

# for i in range(1, 11):
#     total = total + i

# print(total)



# for i in range(1, 21):
#     if i % 2:
#         print(i, ' - нечётное')
#     elif i % 2 == False:
#         print(i, ' - чётное')



# count = 0

# for i in range(1, 101):
#     if i % 5 == 0:
#         count = count + 1

# print(count)



# user = {
#     "name": "Alex",
#     "age": 18,
#     "city": "Moscow"
# }

# функция enumarate() получает одновременно ключ и значение

# for key, value in enumerate(user, start=1):
#     print(key, '-', value)



# numbers = [10, 45, 23, 87, 54, 87, 12, 65]

# second = numbers[0]
# first = numbers[1]

# for number in numbers:
#     if number > first:
#         second = first
#         first = number
#     elif number > second and number != first:
#         second = number
        
# print(second)



# user = input('Введите строку: ')

# result = ''

# for word in user:
#     result = word + result

# print(result)



# numbers = [34, 7, 56, 2, 99, 41, 18]

# minimum = numbers[3]

# for number in numbers:
#     if number < minimum:
#         minimum = number
        
# print(minimum)




# user = input('Введите числа: ')


# split() разделяет строку на пробелы
# map() применяет int к каждому элементу
# list() создаёт обычный список

# numbers = list(map(int, user.split()))

# count = 0
# total = 0
# even = 0
# odd = 0

# maximum = numbers[0]
# minimum = numbers[0]

# for number in numbers:
#     count += 1
#     total += number

#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1

#     if number > maximum:
#         maximum = number

#     if number < minimum:
#         minimum = number

# average = total / count

# print('Количество:', count)
# print('Сумма:', total)
# print(f'Среднее: {average:.2f}')
# print('Максимум:', maximum)
# print('Минимум:', minimum)
# print('Чётных:', even)
# print('Нечётных:', odd)