import random

def task1(rows, columns):
#    rows = 5
#    columns = 5
    values = [[] for _ in range(rows)]
    for row in range(rows):
        offset = row * columns + 10
        for col in range(columns):
            values[row].append(random.randint(-10,10))
    for i in range(rows):
        for j in range(columns):
            print(values[i][j], end=" ")
        print()

    min_list = []
    max_list = []
    for c in range(rows):
        min_list.append(min(values[c]))
        max_list.append(max(values[c]))
    print("\nMin list:  ", min_list)
    print("\nMax list:  ", max_list)

# Calculate an average for columns
    mean_ = []
    for j in range(columns):
        s = 0
        for i in range(rows):
            s += values[i][j]
        mean_.append(s / rows)
    print("\nAn average:  ", mean)

def task4():
    total = 64
    g = total // 2 # number of gus
    k = total // 4 # number of krolik
    for i in range(g + 1):
        for j in range(k + 1):
            if i * 2 + j * 4 == 64:
                print(" Number of gus:  ", i, "   and   Number of krolik:   ", j)


def multiply_table():
    x = 10
    y = 10
    table = [[] for _ in range(x)]
    for i in range(1, x):
        for j in range(1, y):
            table[i].append(i * j)
        print(table[i])
    print()
multiply_table()

def task6():
    n = 4
    m = 5
    even = 0
    odd = 0
    task6_list = [[] for _ in range(n)]
#    print("\nUsed random list of integers:\n", task6_list)
    for x in range(n):
        for y in range(m):
            task6_list[x].append(random.randint(-10, 10))
    print("\nUsed random list of integers:\n", task6_list)
    for x in range(n):
        for y in range(m):
            if task6_list[x][y] % 2 == 0:
                even += 1
            else:
                odd += 1
    print("Number of even is:  ", even)
    print("Number of odd is:  ", odd)
    print("Check:  ", (len(task6_list) - even))



#task6()
#task4()
#task1(5, 6)
#multiply_table()