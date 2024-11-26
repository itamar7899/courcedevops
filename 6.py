a = "itamar"

print(a * 5)

print(list(range(5)))
print(list(range(1, 50, 10)))
print(list(range(50, 10, -3)))



for i in range(5):
    print(a)

names = ["itamar", "inbal", "dor"]

for name in names:
    if name == "itamar":
        name = "roey"
    print(f"hello {name}")


for i in range(len(names)):
    print(f"hello {names[i]}")



current_name = input("what is your name ?")


while current_name != "quit":
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break
    print(f"hello {current_name}")
    current_name = input('what is your name:')
else:
    print("Thank for the playing")