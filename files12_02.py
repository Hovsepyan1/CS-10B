# try:
#     fd = open("test1.txt", "x")
# except FileExistsError:
#     print("File arden ka")
# help(FileExistsError)

# with open("test.txt", "r+") as fd:
#     print(fd.readlines())
#     fd.seek(0)
#     fd.write("Alexy petqa sus mna")

# fd = open("test_image.png", "rb")
# a = fd.read()
# fd1 = open("test_image1.png", "wb")
# fd1.write(a)


# Կարդալ ֆայլը և տպել բոլոր անունները։
# fd = open ("users.txt","r" )
# # print(fd.readlines())
# a = fd.readlines()
# for i in a:
#     parts = i.strip().split(",")
#     print(parts[1])

# Ավելացնել նոր user ֆայլի վերջում 👇
# 4,Emma,19

# fd=open("users.txt","a")
# fd.write("4,Emma,19")
# print("Vigen")

# Մուտք ընդունել id և տպել համապատասխան user-ը։
# a=input("Enter your ID: ")
# fd=open("users.txt","r")
# n=fd.readlines()
# for i in n:
#     parts=i.strip().split(",")
#     if parts[0]==a:
#         print(parts[1],parts[2])


# Փոխել id = 2 user-ի age → 30

fd = open("users.txt", "r")
for i in n:
    parts=i.strip