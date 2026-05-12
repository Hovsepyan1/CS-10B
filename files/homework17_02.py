# Փոխել id = 2 user-ի age → 30
# Ֆայլը պետք է ամբողջությամբ rewrite անել։

# FILE = "users.txt"
# f = open( FILE, "r+")

# data = f.readlines()
# print(data) 

# for i in range(len(data)):
#     parts = data[i].strip().split(",")
#     print(parts) 
#     if parts[0] == '2':
#         parts[2] = "30"
#     data[i] = ",".join(parts) + "\n"
# print(data)
# f.seek(0)
# f.writelines(data)




# Տպել քանի user կա ֆայլում։
# print(len(open("users.txt", "r+").readlines()))



# Սորտ անել user-ներին ըստ age և գրել ֆայլի մեջ։


# f = open("users.txt" , "r+")
# data = f.readlines()
# for i in range(len(data)):
#     data[i] = data[i].strip().split(",")
# print(data)
# data.sort(key = lambda x : int(x[2]))
# print(data)
# f.seek(0)
# for i in range(len(data)):
#     data[i] = ",".join(data[i]) + "\n"
# print(data)
# f.writelines(data)





# Տպել բոլոր user-ներին որոնց age >= 21
f = open("users.txt" , "r")
data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].strip().split(",")
    # print(data[i])
    if data[i][2] >= "21":
        print(data[i][1])

