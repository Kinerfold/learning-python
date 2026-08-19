# словарь
# for key, value in dictionary

# dictionary = { ключ1:значение1, ключ2:значение2, ....}



# users = {1: "Tom", 2: "Bob", 3: "Bill"}
# emails = {"tom@gmail.com": "Tom", "bob@gmai.com": "Bob", "sam@gmail.com": "Sam"}


# objects = dict()



# users_list = [
#     ["+111123455", "Tom"],
#     ["+384767557", "Bob"],
#     ["+958758767", "Alice"]
# ]
# users_dict = dict(users_list)
# print(users_dict)



# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }

# получаем элемент с ключом "+11111111"
# print(users["+11111111"])      # Tom

# установка значения элемента с ключом "+33333333"
# users["+33333333"] = "Bob Smith"
# print(users["+33333333"]) 


# get(key, default)


# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
 
# user1 = users.get("+55555555")
# print(user1)
# user2 = users.get("+33333333", "Unknown user")
# print(user2)
# user3 = users.get("+44444444", "Unknown user")
# print(user3)


# pop(key, default)


# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# key = "+55555555"
# user = users.pop(key)
# print(user)
 
# user = users.pop("+4444444", "Unknown user")
# print(user)



# users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
# students = users.copy()
# print(students)



# users = {"+1111111": "Tom", "+3333333": "Bob"}
 
# users2 = {"+2222222": "Sam", "+6666666": "Kate"}
# update() объединяет 2 словаря
# users.update(users2)
 
# print(users)
# print(users2)



# перебор ключ и значений
# keys()


# for key in users.keys():
#     print(key)


# valuse() перебор только значений


# for value in users.values():
#     print(value)



