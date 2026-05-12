# fd = open("test.txt", mode = 'r')

# #modes
# #r - read
# #w - write
# #a - append 

# print(fd.read())
#fd = file descriptor 
# fd = open("test.txt", mode = "w")
# fd.write("Hello world")

# fd = open("test.txt", mode = "r")
# fd.write("\nHello world")
# print(fd.read(5))
# print(fd.tell())
# print(fd.read(10))
# print(fd.tell())
# fd.seek(101)
# print(fd.read(10))
# print(fd.tell())
# modes
#r+ = read + write
#w+ = write + read
#x = exclusive

fd = open("test.txt", mode = "r+")
fd.seek(5)
# fd.write(" Hello world ")
print(fd.readline())
print(fd.readline())
print(fd.readlines())
help(fd)