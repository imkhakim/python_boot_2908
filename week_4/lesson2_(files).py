#files

# file = open("test.txt", "r")

# print(type(file.read()))

# print(file.readline())

# counter = 0

# for i in file:
#     line = i.rstrip()
#     if line.startswith("From"):
#         print(line)

#file.close()
#print(counter)

# with open("test.txt", "r") as f:
#     print(f.read())

# with open("test.txt", "a") as f:
#     print(f.read())

# with open("tast.txt", "w") as f:
#     f.write("hello world!!!")


# with open("test.txt", "w") as f:
#     # for i in range(1, 100):
#     #     f.write(f'{i}\n')
#     f.writelines("sdfsdfdsfkkk")
#     f.seek(5)
#     f.writelines("nazi")
#     print(f.read())

with open("test.txt", "r+") as f:
    # for i in range(1, 100):
    #     f.write(f'{i}\n')
    f.writelines("sdfsdfdsfkkk")
    # f.seek(5)
    f.writelines("nazi")
    print(f.read())



