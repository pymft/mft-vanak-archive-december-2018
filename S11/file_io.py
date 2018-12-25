# read and write files

f = open('input.txt', 'r')

f.seek(5)
text = f.read(1)
print(text)




# text = f.read()  #
# print(text)
# line = f.readline()
# print(line)
#
# f.seek(4)
# lines = f.readlines()
# print(lines)

# f.seek()