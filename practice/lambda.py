# numbers = [1, 2, 3, 4, 5]

# user = list(map(lambda a: a * 2, numbers))
# print(user)



# numbers = [3, 8, 11, 14, 17, 20, 25]

# user = list(filter(lambda x: True if x % 2 == 0 else False, numbers))
# print(user)



# numbers = []

# user = input('Введите 5 чисел: ')
# numbers.append(user.split())

# print(numbers)



# words = ["python", "cat", "programming", "code", "computer"]

# sort = list(sorted(words, key=len))

# print(sort)



# numbers = [4, 15, 7, 22, 9, 31, 2, 18]

# func = list(filter(lambda x: True if x > 10 else False, numbers))

# print(func)



numbers = [3, 8, 12, 15, 20, 25, 30]

func = filter(lambda x: x > 10, numbers)
func2 = list(map(lambda a: a * 3, func))

print(func2)