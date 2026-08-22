# match значение:
#     case вариант_1:
#         ...
#     case вариант_2:
#         ...
#     case вариант_3:
#         ...
#     case _: <-- это как else в операторе if
#         ...
# case "a" | "b":
        # ...


# Если необходимо сравнивать выражение с кортежем неопределенной длины, то можно поставить *

# def print_data(user):
#     match user:
#         case ("Tom", 37, *rest):
#             print(f"Rest: {rest}")
#         case (name, age, *rest):
#             print(f"{name} ({age}): {rest}")
 
 
# print_data(("Tom", 37))
# print_data(("Tom", 37, "Google"))
# print_data(("Bob", 41, "Microsoft", "english"))




# Если параметр *rest нам не важен, то просто ставим подшаблон *_

# def print_data(user):
#     match user:
#         case ("Tom", 37, *_):
#             print("Default user")
#         case (name, age, *_):
#             print(f"{name} ({age})")
 
 
# print_data(("Tom", 37))
# print_data(("Tom", 37, "Google"))
# print_data(("Bob", 41, "Microsoft", "english"))





