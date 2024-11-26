# try:
#     a = 1 / 0
#
# except:
#
#     print("cant to division any number with zero")
#

# try:
#     x = 1
#
# finally:
#     print("finally")

my_file = open('homework4.txt', 'w')
my_file.close()

my_file = open('homework4.txt', 'w')
my_file.write("itamar")
my_file.close()

my_file = open('homework4.txt', 'r')
read = my_file.read()
print(read)
my_file.close()

my_file = open('homework4.txt', 'w')
my_file.write("איתמר")
my_file.close()

my_file = open('homework4.txt', 'r', encoding='utf-8')
read = my_file.read()
print(read)
my_file.close()


