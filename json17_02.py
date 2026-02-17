#json file = javascript object notation

# import json
# fd = open("data.json", "r+")
# data = json.load(fd)
# print(data)
# print(type(data))
# data['surname'] = 'Bond'
# print(data)
# fd.seek(0)
# json.dump(data, fd, indent=4)

# Տպել բոլոր user-ների անունները
# import json
# with open("data.json", "r") as fd:
#     data = json.load(fd)
#     # print(data)
#     # print(data['users'])
#     for i in data['users']:
#         print(i['name'])

# Ավելացնել նոր user․
# {"id": 4, "name": "Amelia", "age": 19}
# import json
# fd = open("data.json", "r+")
# dict = json.load(fd)
# dict['users'].append({"id": 4, "name": "Amelia", "age": 19})
# fd.seek(0)
# json.dump(dict, fd, indent=2)
# print(dict)
# fd.close()

# Մուտք ընդունել id և տպել համապատասխան user-ը։
idx = int(input("Enter id: "))
import json
fd = open("data.json", "r")
dict = json.load(fd)
for i in dict['users']:
    if i['id'] == idx:
        print(i['name'])

fd.close()