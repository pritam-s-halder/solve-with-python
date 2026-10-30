rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()

#Floyd's triangle
rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


# star patterns
rows = 5

for i in range(1, rows + 1):
    print("*" * i)

