# # try:
# #     n1 = 10
# #     n2 = 0
# #     print(n1/n2)
# # except ZeroDivisionError as chlp:
# #     print("bajanel enq 0-i, normal tiv gri")

# # try:
# #     n1 = int(input())
# #     n2 = int(input())
# #     print(n1 / n2)
# # except:
# #     print("Normal ban gri")
# # # except ZeroDivisionError as e:
# # #     print(e)
# # else:
# #     print("error texi chi unecel")
# # finally:
# #     print("Sa misht katarvum e")


# try:
#     n1 = int(input())
#     n2 = int(input())
#     print(n1 / n2)
# except ArithmeticError:
#     print("Normal ban gri")
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("error texi chi unecel")
# finally:
#     print("Sa misht katarvum e")

# x1 = 18

# print(x2)

# raise TypeError("Sxal type es tvel")

def my_len(s: str) -> int:
    if not isinstance(s, str):
        raise TypeError("sxal type es tvel")
    return len(s)

print(my_len(":hhh"))