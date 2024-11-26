print(list(range(1, 101)))


for i in range(1, 101):
    if not i % 7 == 0 and "7" not in str(i):
        print(i)



names = ["natan", "shay", "ronen"]
results = [name.upper() for name in names if "n" in name]

print(results)